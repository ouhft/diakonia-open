#!/usr/bin/python
# coding: utf-8
import io

from xml.dom.minidom import Document
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = "Generates an XML document compliant with the v1.6.0 NHIC TRA xsd"

    def handle(self, *args, **options):
        with io.open('tests.xml', mode='wb') as xml_file:
            # Fetch the data for output
            organs = []  # Organ.objects.all()

            # Prepare the output document basics
            xml_doc = Document()  # https://docs.python.org/3/library/xml.dom.minidom.html

            def _create_element_with_text(parent_element=None, element_name="", element_text="", required=True):
                if element_text is None or element_text is "":
                    if not required:
                        return
                    element_text = ""
                new_element = xml_doc.createElement(element_name)
                new_element.appendChild(xml_doc.createTextNode(str(element_text)))
                parent_element.appendChild(new_element)

            def _create_element_with_date(
                    parent_element=None,
                    element_name="",
                    element_date=timezone.now(),
                    required=True
            ):
                if element_date is None and not required:
                    return
                element_date_string = element_date.strftime("%Y-%m-%d") if element_date is not None else ""
                new_element = xml_doc.createElement(element_name)
                new_element.appendChild(xml_doc.createTextNode(element_date_string))
                parent_element.appendChild(new_element)

            def _create_element_with_datetime(
                    parent_element=None,
                    element_name="",
                    element_datetime=timezone.now(),
                    required=True
            ):
                if element_datetime is None and not required:
                    return
                element_date_string = element_datetime.strftime("%Y-%m-%dT%H:%M:%S%z") if element_datetime is not None else ""
                # Need to reformat the timezone offset to an xml compliant string with a colon in it
                if element_date_string is not "" and element_date_string[-5] in ["+", "-"]:
                    element_date_string = element_date_string[:-2] + ":" + element_date_string[-2:]
                new_element = xml_doc.createElement(element_name)
                new_element.appendChild(xml_doc.createTextNode(element_date_string))
                parent_element.appendChild(new_element)

            for organ in organs:
                node_record = xml_doc.createElement('record')
                node_record.attributes['xmlns:xsi'] = "http://www.w3.org/2001/XMLSchema-instance"
                node_record.attributes['xsi:noNamespaceSchemaLocation'] = "NHIC_TRA_1.6.0.xsd"

                # METADATA
                node_record_metadata = xml_doc.createElement('metadata')
                _create_element_with_text(node_record_metadata, "form-name", "NHIC-Transplantation")
                _create_element_with_text(node_record_metadata, "form-version", "1.6.0")
                _create_element_with_text(node_record_metadata, "date", timezone.now().strftime("%Y-%m-%d"))
                _create_element_with_text(node_record_metadata, "nhic_tra_245", "RJ1")
                node_record.appendChild(node_record_metadata)

                # RECIPIENTS
                node_record_recipient = xml_doc.createElement('recipient')
                _create_element_with_text(
                    node_record_recipient,
                    "recipient_ID",
                    "R_{0}".format(organ.recipient.patient.psuedo_id),
                    required=True
                )

                node_record_recipient_demographics = xml_doc.createElement('demographics')
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_0",
                    organ.recipient.patient.psuedo_id,
                    required=True
                )
                odt_number = organ.recipient.patient.nhsbt_odt_number
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_19",
                    odt_number if odt_number is not None else "0000000000",
                    required=True
                )
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_6",
                    organ.recipient.patient.date_of_birth.year,
                    required=True
                )
                try:
                    outer_postcode = organ.recipient.patient.address.outer_postcode
                except AttributeError:
                    outer_postcode = None
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_8",
                    outer_postcode,
                    required=False
                )
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_14",
                    organ.recipient.patient.gender,
                    required=False
                )
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_14-1",
                    organ.recipient.patient.gender_translated,
                    required=False
                )
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_15",
                    organ.recipient.patient.ethnicity,
                    required=False
                )
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_15-1",
                    organ.recipient.patient.ethnicity_translated,
                    required=False
                )
                try:
                    gp_surgery_name = organ.recipient.patient.gp_surgery.name
                except AttributeError:
                    gp_surgery_name = None
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_16",
                    gp_surgery_name,
                    required=False
                )
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_17",
                    organ.recipient.patient.blood_group,
                    required=False
                )
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_17-1",
                    organ.recipient.patient.blood_group_translated,
                    required=False
                )
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_18",
                    organ.recipient.patient.blood_rhesus,
                    required=False
                )
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_18-1",
                    organ.recipient.patient.blood_rhesus_translated,
                    required=False
                )
                _create_element_with_text(
                    node_record_recipient_demographics,
                    "nhic_tra_20",
                    "RENAL REGISTRY NUMBER",
                    required=False
                )
                _create_element_with_date(
                    node_record_recipient_demographics,
                    "nhic_tra_21",
                    organ.recipient.patient.date_of_death,
                    required=False
                )
                node_record_recipient.appendChild(node_record_recipient_demographics)

                node_record.appendChild(node_record_recipient)

                # DONORS
                node_record_donor = xml_doc.createElement('donor')
                _create_element_with_text(
                    node_record_donor,
                    "donor_ID",
                    "D_{0}".format(organ.donor.patient.psuedo_id),
                    required=True
                )

                node_record_donor_demographics = xml_doc.createElement('demographics')
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_243",
                    organ.donor.patient.psuedo_id,
                    required=True
                )
                odt_number = organ.donor.patient.nhsbt_odt_number
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_40",
                    odt_number if odt_number is not None else "0000000000",
                    required=True
                )
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_27",
                    organ.donor.patient.date_of_birth.year,
                    required=False
                )

                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_35",
                    organ.donor.patient.gender,
                    required=False
                )
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_35-1",
                    organ.donor.patient.gender_translated,
                    required=False
                )
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_36",
                    organ.donor.patient.ethnicity,
                    required=False
                )
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_36-1",
                    organ.donor.patient.ethnicity_translated,
                    required=False
                )
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_38",
                    organ.donor.patient.blood_group,
                    required=False
                )
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_38-1",
                    organ.donor.patient.blood_group_translated,
                    required=False
                )
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_39",
                    organ.donor.patient.blood_rhesus,
                    required=False
                )
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_39-1",
                    organ.donor.patient.blood_rhesus_translated,
                    required=False
                )
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_41",
                    "RENAL REGISTRY NUMBER",
                    required=False
                )
                _create_element_with_text(
                    node_record_donor_demographics,
                    "nhic_tra_42",
                    "AGE IN YEARS",
                    required=False
                )
                node_record_donor.appendChild(node_record_donor_demographics)

                node_record.appendChild(node_record_donor)

                # TRANSPLANTS
                node_record_transplant = xml_doc.createElement('transplant')
                _create_element_with_text(
                    node_record_transplant,
                    "recipient_IDREF",
                    "R_{0}".format(organ.recipient.patient.psuedo_id),
                    required=True
                )
                _create_element_with_text(
                    node_record_transplant,
                    "donor_IDREF",
                    "D_{0}".format(organ.donor.patient.psuedo_id),
                    required=True
                )

                # NB: Tranplant-details is not my typo, this is from the XSD!
                node_record_transplant_transplantdetails = xml_doc.createElement('tranplant-details')
                _create_element_with_datetime(
                    node_record_transplant_transplantdetails,
                    "nhic_tra_66",
                    organ.recipient.start_time,
                    required=True
                )

                node_record_transplant.appendChild(node_record_transplant_transplantdetails)

                node_record.appendChild(node_record_transplant)

                xml_doc.appendChild(node_record)

            # Write the accumulated output
            xml_file.write(xml_doc.toprettyxml(encoding="utf-8"))
