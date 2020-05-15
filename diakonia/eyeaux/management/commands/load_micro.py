#!/usr/bin/python
import pytz

from django.core.management.base import LabelCommand
from django.utils import timezone

from diakonia.eyeaux.excel_utils import NHSBTworkbook, int_as_str
from diakonia.eyeaux.models import PSSPerson, PSSmicroResult
from diakonia.eyeaux.forms import PSSPersonForm, PSSmicroResultForm


class Command(LabelCommand):
    help = "Load a specified PSS-Micro provided spreadsheet of data"

    def handle_label(self, label, **options):
        # Generate some stats for feedback
        start_time = timezone.now()
        end_time = None
        total_rows = 0
        created_count_person = 0
        created_count_result = 0
        update_count_person = 0
        update_count_result = 0

        if label.split(".")[-1] != "xlsx":
            raise Exception("This is not an xlsx file")
        print("Workbook ({0}) is about to load".format(label))

        # Load the xlsx file with the raw data
        workbook = NHSBTworkbook()
        if not workbook.load_xlsx(label):
            raise Exception("xlsx file failed to load")
        total_rows = workbook.worksheet.max_row
        print("Workbook is now loaded. {0} rows were found".format(total_rows))

        # Iterate through the data, creating or updating records in NHSBTRecords
        for row_index in range(2, total_rows+1):
            row_data = workbook.load_row(row_index)
            # print("DEBUG: Row data for row {0} is loaded".format(row_index))

            def cell_value_by_id(column_id=1):
                return workbook.worksheet.cell(row=row_index, column=column_id).value

            def cell_value_by_title(column_name=""):
                return row_data[column_name.lower()]

            nhsnumber_value = cell_value_by_title('nhsnumber')
            person, created = PSSPerson.objects.get_or_create(
                nhsnumber=nhsnumber_value,
                defaults={
                    'nhsnumber': nhsnumber_value
                }
            )
            created_count_person += 1 if created else 0

            form_data = {
                'nhsnumber': cell_value_by_title("nhsnumber"),
                'mrn': cell_value_by_title("mrn"),
                'sex': cell_value_by_title("sex"),
                'forename': cell_value_by_title("forename"),
                'surname': cell_value_by_title("surname"),
                'birthdate': cell_value_by_title("birthdate"),
                'deathdate': cell_value_by_title("deathdate"),
                'ethnic_group': cell_value_by_title("ethnic group"),
            }
            person_form = PSSPersonForm(data=form_data, instance=person)
            if person_form.is_valid():
                if person_form.has_changed():
                    update_count_person += 1
                    person = person_form.save()
            else:
                print("Person Form #{0} is INVALID".format(row_index))
                print(person_form.errors)

            # Now get the data components
            collection_dt = cell_value_by_title('collectiondatetime')
            collection_dt = pytz.utc.localize(collection_dt) if collection_dt is not None else None
            testcode = cell_value_by_title('testcode')
            record, created = PSSmicroResult.objects.get_or_create(
                person=person,
                collection_datetime=collection_dt,
                testcode=testcode,
                defaults={
                    'person': person,
                    'collection_datetime': collection_dt,
                    'testcode': testcode
                }
            )
            created_count_result += 1 if created else 0
            # Need to map the row headings to the data model headings
            form_data = {
                'person': person.id,
                'collection_datetime': collection_dt,
                'accession_number': cell_value_by_title("accessionnumber"),
                'testcode': testcode,
                'batch_test_code': cell_value_by_title("batchtestcode"),
                'result_trans': cell_value_by_title("result trans"),
                'result_modifiers': cell_value_by_title("result modifiers"),
                'res_composed_text': cell_value_by_title("res composed text"),
                'result_method': cell_value_by_title("result method")
            }
            data_form = PSSmicroResultForm(data=form_data, instance=record)
            if data_form.is_valid():
                if data_form.has_changed():
                    update_count_result += 1
                    record = data_form.save()
            else:
                print("Data Form #{0} is INVALID".format(row_index))
                print(data_form.errors)

            # Provide some feedback
            if row_index % 50 == 0:
                print("Row {0} of {1} imported".format(row_index, total_rows))
                print("{0:06.2f}% Complete at {1:%Y-%m-%d %H:%M:%S}".format(
                    (row_index/total_rows)*100,
                    timezone.now()
                ))

        end_time = timezone.now()
        print("Import completed:")
        print("  Started: {0:%Y-%m-%d %H:%M:%S}. Finished: {1:%Y-%m-%d %H:%M:%S}.".format(start_time, end_time))
        print("  New:     Person:{0}   Result:{1}.".format(created_count_person, update_count_person))
        print("  Updated: Person:{0}   Result:{1}.".format(created_count_result, update_count_result))
        print("  Total rows: {0}".format(total_rows))
