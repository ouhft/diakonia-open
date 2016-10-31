#!/usr/bin/python
# coding: utf-8
from datetime import datetime

from django.core.management.base import LabelCommand
from django.utils import timezone

from diakonia.eyeaux.excel_utils import NHSBTworkbook, int_as_str
from diakonia.eyeaux.models import NHSBTRecord, NHSBTFile, NHSBTLog
from diakonia.eyeaux.forms import NHSBTRecordForm


class Command(LabelCommand):
    help = "Load a specified nhsbt provided spreadsheet of data"

    def handle_label(self, label, **options):
        # Generate some stats for feedback
        start_time = timezone.now()
        end_time = None
        total_rows = 0
        created_count = 0
        update_count = 0

        if label.split(".")[-1] != "xlsx":
            raise Exception("This is not an xlsx file")
        print("Workbook ({0}) is about to load".format(label))

        # Load the xlsx file with the raw data
        workbook = NHSBTworkbook()
        if not workbook.load_xlsx(label):
            raise Exception("xlsx file failed to load")
        total_rows = workbook.worksheet.max_row

        filename = label.split("/")[-1]
        extract_date = datetime.strptime(filename.split("_")[-1][:-5], "%d%b%Y")
        file, created = NHSBTFile.objects.get_or_create(
            filename=filename,
            extract_date=extract_date,
            defaults={
                'filename': filename,
                'extract_date': extract_date
            }
        )
        print("Workbook is now loaded. {0} rows were found".format(total_rows))

        # Iterate through the data, creating or updating records in NHSBTRecords
        for row_index in range(2, total_rows+1):
            row_data = workbook.load_row(row_index)
            # print("DEBUG: Row data for row {0} is loaded".format(row_index))

            def cell_value_by_id(column_id=1):
                return workbook.worksheet.cell(row=row_index, column=column_id).value

            def cell_value_by_title(column_name=""):
                return row_data[column_name.lower()]

            # Get or create a record by using the compound key of DonorID an RecipID
            donor_id = int_as_str(cell_value_by_title("DONOR_ID"))
            recipient_id = int_as_str(cell_value_by_title("RECIP_ID"))

            record, created = NHSBTRecord.objects.get_or_create(
                donor_id=donor_id,
                recip_id=recipient_id,
                defaults={
                    'donor_id': donor_id,
                    'recip_id': recipient_id
                }
            )
            created_count += 1 if created else 0

            data_form = NHSBTRecordForm(data=row_data, instance=record)
            if data_form.is_valid():
                if data_form.has_changed():
                    update_count += 1
                    record = data_form.save()

                    log = NHSBTLog()
                    log.file = file
                    log.record = record
                    log.changed_fields = ", ".join(data_form.changed_data)
                    log.save()

            else:
                print("Form #{0} is INVALID".format(row_index))
                print(data_form.errors)

            # Provide some feedback
            if row_index % 50 == 0:
                print("Row {0} of {1} imported".format(row_index, total_rows))
                print("{0:06.2f}% Complete at {1:%Y-%m-%d %H:%M:%S}".format(
                    (row_index/total_rows)*100,
                    timezone.now()
                ))

        end_time = timezone.now()
        print("Import completed: Started: {0:%Y-%m-%d %H:%M:%S}. Finished: {1:%Y-%m-%d %H:%M:%S}. New: {2}. Updated: {3}. Total: {4}".format(
            start_time, end_time, created_count, update_count, total_rows
        ))
