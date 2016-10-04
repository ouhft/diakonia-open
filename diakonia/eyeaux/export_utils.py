#!/usr/bin/python
# coding: utf-8
from __future__ import absolute_import, unicode_literals

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
