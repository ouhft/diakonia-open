#!/usr/bin/python
# coding: utf-8
from __future__ import absolute_import, unicode_literals
from lxml import etree
from .models import NHSBTRecord


def psuedo_id(record_id, donor=False):
    """
    For nhic_tra_Pseudo_ID - Pseudo ID of the Patient (Recipient). This is a code which is
    anonymous to those looking at the dataset, but which can be used to look up the real identity
    of the patient. Length 5-32.

    :return: String, fixed for this record of length 10. Starts "OUH-", then 6 numbers
    """
    from django.utils.crypto import get_random_string
    record = NHSBTRecord.objects.get(pk=record_id)
    if donor:
        while record._psuedo_id_d is "":
            new_string = get_random_string(6, allowed_chars='1234567890')
            test_string = "OUH-{0}".format(new_string)
            if not NHSBTRecord.objects.filter(_psuedo_id_d=test_string).exists():
                record._psuedo_id_d = test_string
                record.save()
        return record._psuedo_id_d
    else:
        while record._psuedo_id_r is "":
            new_string = get_random_string(6, allowed_chars='1234567890')
            test_string = "OUH-{0}".format(new_string)
            if not NHSBTRecord.objects.filter(_psuedo_id_r=test_string).exists():
                record._psuedo_id_r = test_string
                record.save()
        return record._psuedo_id_r


def outer_postcode(postcode):
    postcode_trimmed = postcode if postcode is not None else ""
    if postcode_trimmed is not "":
        postcode_trimmed = postcode_trimmed.split()[0]
    return postcode_trimmed


def gender_translated(raw_gender):
    return "9"


def ethnic_translated(raw_ethnic):
    return "Z"


def blood_group_translated(raw_bg):
    return "UNKNOWN"


def blood_rhesus_translated(raw_rhesus):
    return "UNKNOWN"


def translate_datetime(dt_string):
    element_date_string = dt_string.strftime("%Y-%m-%dT%H:%M:%S%z") if dt_string is not None and dt_string != "" else ""
    # Need to reformat the timezone offset to an xml compliant string with a colon in it
    if element_date_string is not "" and element_date_string[-5] in ["+", "-"]:
        element_date_string = element_date_string[:-2] + ":" + element_date_string[-2:]
    return element_date_string


def add_hla_mismatches(a, b, dr):
    total = 0
    try:
        total = int(a)
    except ValueError:
        pass
    except TypeError:  # e.g. None
        pass
    try:
        total += int(b)
    except ValueError:
        pass
    except TypeError:  # e.g. None
        pass
    try:
        total += int(dr)
    except ValueError:
        pass
    except TypeError:  # e.g. None
        pass
    return str(total)


def sentence_from_value(label, value):
    if value is not None and value is not "" and value is not ".":
        return "{0}=[{1}]".format(label, value)
    return ""


def year_from_date(datestring):
    if datestring is not None and datestring is not "":
        return str(datestring.year)
    return "0000"


def translate_yes_no(inputstring):
    if inputstring.lower() == "yes":
        return "Y"
    elif inputstring.lower() == "no":
        return "N"
    return ""


def translate_serology(inputstring):
    if inputstring.lower() in ["negative", "positive", "not reported", "not tested", "result awaited", "unknown"]:
        return inputstring
    # We also have "Indeterminate"
    return ""


def cleanup(element):
    if etree.iselement(element):
        for e in list(element):
            if len(e):
                e = cleanup(e)
                # Remove empty branches
                if not len(e):
                    element.remove(e)
            else:
                # Remove empty nodes
                if e.text == "" or e.text == ".":
                    element.remove(e)
    return element



