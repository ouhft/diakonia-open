#!/usr/bin/python
# coding: utf-8
import pytz
import datetime

from django.core.management.base import LabelCommand
from django.utils import timezone

from diakonia.eyeaux.excel_utils import ReadOnlyWorkbook, int_as_str
from diakonia.eyeaux.models import PSSPerson, PSSlimsResult
from diakonia.eyeaux.forms import PSSPersonForm, PSSlimsResultForm


class Command(LabelCommand):
    help = "Load a specified PSS-LIMS provided spreadsheet of data"

    def handle_label(self, label, **options):
        # Generate some stats for feedback
        start_time = timezone.now()
        end_time = None
        row_index = 1
        created_count_person = 0
        created_count_result = 0
        update_count_person = 0
        update_count_result = 0

        if label.split(".")[-1] != "xlsx":
            raise Exception("This is not an xlsx file")
        print("Workbook ({0}) is about to load".format(label))

        # Load the xlsx file with the raw data
        workbook = ReadOnlyWorkbook()
        if not workbook.load_workbook(filename=label, column_count=15):
            raise Exception("xlsx file failed to load")
        print("Workbook is now loaded.")

        # Iterate through the data, creating or updating records in NHSBTRecords
        for raw_row in workbook.get_rows():
            if row_index == 1:
                continue  # Skip the first row

            row_data = workbook.load_row(row=raw_row)
            print("DEBUG: Row data = {0}".format(row_data))

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
                'nhsnumber': nhsnumber_value,
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
                print("Person Form #{0} is INVALID".format(nhsnumber_value))
                print(person_form.errors)

            # Now get the data components
            collection_dt = cell_value_by_title('collectiondatetime')
            # NB: These datetime strings have 7 microsecond digits opposed to the expected 6, and some are naive
            collection_dt = datetime.datetime.strptime(collection_dt, "%Y-%m-%d %H:%M:%S.0%f") if type(collection_dt) is not datetime.datetime else collection_dt
            collection_dt = pytz.utc.localize(collection_dt) if collection_dt.tzinfo is None else collection_dt
            testname = cell_value_by_title('testname')

            record, created = PSSlimsResult.objects.get_or_create(
                person=person,
                collection_datetime=collection_dt,
                test_name=testname,
                defaults={
                    'person': person,
                    'collection_datetime': collection_dt,
                    'test_name': testname
                }
            )
            created_count_result += 1 if created else 0
            # Need to map the row headings to the data model headings
            form_data = {
                'person': person.id,
                'collection_datetime': collection_dt,
                'test_name': testname,
                'min_range': cell_value_by_title("minrange"),
                'max_range': cell_value_by_title("maxrange"),
                'units': cell_value_by_title("units"),
                'value_string': cell_value_by_title("value"),
                'value_number': cell_value_by_title("numbervalue")
            }
            data_form = PSSlimsResultForm(data=form_data, instance=record)
            if data_form.is_valid():
                if data_form.has_changed():
                    update_count_result += 1
                    record = data_form.save()
            else:
                print("Data Form is INVALID")
                print(data_form.errors)

            row_index += 1
            # Provide some feedback
            if row_index % 50 == 0:
                print("Row {0} imported at {1:%Y-%m-%d %H:%M:%S}".format(row_index, timezone.now()))

        end_time = timezone.now()
        print("Import completed:")
        print("  Started: {0:%Y-%m-%d %H:%M:%S}. Finished: {1:%Y-%m-%d %H:%M:%S}.".format(start_time, end_time))
        print("  New:     Person:{0}   Result:{1}.".format(created_count_person, update_count_person))
        print("  Updated: Person:{0}   Result:{1}.".format(created_count_result, update_count_result))
        print("  Total rows: {0}".format(row_index))
