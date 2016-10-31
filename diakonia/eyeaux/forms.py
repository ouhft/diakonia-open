#!/usr/bin/python
# coding: utf-8
from django import forms
import pytz

from .models import NHSBTRecord, PSSPerson, PSSmicroResult, PSSlimsResult
from .excel_utils import int_as_str


class NHSBTRecordForm(forms.ModelForm):
    class Meta:
        model = NHSBTRecord
        fields = [
            'recip_forename',
            'recip_surname',
            'rdob',
            'rnhs_no',
            'rpostcode',
            'recip_residence',
            'rsex',
            'rethnic',
            'rbg',
            'rrhesus',
            'recip_id',
            'rdod',
            'donor_forename',
            'donor_surname',
            'ddob',
            'dnhs_no',
            'donor_postcode',
            'dresidence',
            'dsex',
            'dethnic',
            'dbg',
            'drhesus',
            'donor_id',
            'dage',
            'dcod',
            'dhtlv',
            'dsyphilis',
            'dpast_alcohol_abuse',
            'dpast_cardio_disease',
            'dpast_diabetes',
            'dpast_drug_abuse',
            'dpast_hypertension',
            'dpast_liver_disease',
            'dpast_other',
            'dpast_other_details',
            'dpast_smoker',
            'dpast_smoker_amount',
            'dpast_tumour',
            'dpast_uti',
            'dpast_family_diabetes',
            'dpast_family_diabetes_type',
            'dial_at_tx',
            'dial_at_tx_type',
            'dial_start_date',
            'dial_end_date',
            'no_prev_tx',
            'tx_date',
            'rec_unit',
            'rhosp_no',
            'dtype',
            'rltnship',
            'relationship_details',
            'laterality',
            'tx_type',
            'local',
            'faildate',
            'aitx_type',
            'cit_hrs',
            'fwit',
            'swit',
            'amm',
            'bmm',
            'drmm',
            'recip_hla_sample_date',
            'recip_first_a_broad',
            'recip_first_a_split',
            'recip_second_a_broad',
            'recip_second_a_split',
            'recip_first_b_broad',
            'recip_first_b_split',
            'recip_second_b_broad',
            'recip_second_b_split',
            'recip_first_c_broad',
            'recip_first_c_split',
            'recip_second_c_broad',
            'recip_second_c_split',
            'recip_first_dr_broad',
            'recip_first_dr_split',
            'recip_second_dr_broad',
            'recip_second_dr_split',
            'recip_first_dp_broad',
            'recip_first_dp_split',
            'recip_second_dp_broad',
            'recip_second_dp_split',
            'recip_first_dq_broad',
            'recip_first_dq_split',
            'recip_second_dq_broad',
            'recip_second_dq_split',
            'donor_hla_sample_date',
            'donor_first_a_broad',
            'donor_first_a_split',
            'donor_second_a_broad',
            'donor_second_a_split',
            'donor_first_b_broad',
            'donor_first_b_split',
            'donor_second_b_broad',
            'donor_second_b_split',
            'donor_first_c_broad',
            'donor_first_c_split',
            'donor_second_c_broad',
            'donor_second_c_split',
            'donor_first_dr_broad',
            'donor_first_dr_split',
            'donor_second_dr_broad',
            'donor_second_dr_split',
            'donor_first_dp_broad',
            'donor_first_dp_split',
            'donor_second_dp_broad',
            'donor_second_dp_split',
            'donor_first_dq_broad',
            'donor_first_dq_split',
            'donor_second_dq_broad',
            'donor_second_dq_split',
            'cyclosporin',
            'mycophenolate_mofetil',
            'other_immuno_drug',
            'immuno_text',
            'prednisolone_prednisone',
            'tacrolimus',
            'azathioprine',
            'alg_atg',
            'okt3',
            'rcmv',
            'rhiv',
            'debv',
            'dtoxo',
            'dhiv',
            'dgf',
            'resume_dialysis_date',
            'rheight',
            'rweight',
            'serum3',
            'scdate3',
            'serum12',
            'scdate12',
            'serum24',
            'scdate24',
            'serum36',
            'scdate36',
            'serum48',
            'scdate48',
            'serum60',
            'scdate60',
            'rbhv',
            'rhcv',
            'dhbcab',
            'dhbsag',
            'dhcv',
            'egfr3',
            'egfr12',
            'egfr24',
            'egfr36',
            'egfr48',
            'egfr60',
        ]

    def clean_recip_id(self):
        recip_id = self.cleaned_data['recip_id']
        return int_as_str(recip_id)

    def clean_donor_id(self):
        donor_id = self.cleaned_data['donor_id']
        return int_as_str(donor_id)

    def clean(self):
        cleaned_data = super(NHSBTRecordForm, self).clean()
        # Insert Clean up code
        return cleaned_data


class PSSPersonForm(forms.ModelForm):
    class Meta:
        model = PSSPerson
        fields = [
            'nhsnumber',
            'mrn',
            'sex',
            'forename',
            'surname',
            'birthdate',
            'deathdate',
            'ethnic_group'
        ]


class PSSlimsResultForm(forms.ModelForm):
    class Meta:
        model = PSSlimsResult
        fields = [
            'person',
            'collection_datetime',
            'test_name',
            'min_range',
            'max_range',
            'units',
            'value_string',
            'value_number'
        ]

    def clean_collection_datetime(self):
        dt_value = self.cleaned_data['collection_datetime']
        if dt_value.tzinfo is not None and dt_value.tzinfo.utcoffset(dt_value) is not None:
            return dt_value
        return pytz.utc.localize(dt_value)



class PSSmicroResultForm(forms.ModelForm):
    class Meta:
        model = PSSmicroResult
        fields = [
            'person',
            'collection_datetime',
            'accession_number',
            'testcode',
            'batch_test_code',
            'result_trans',
            'result_modifiers',
            'res_composed_text',
            'result_method',
        ]

    def clean_collection_datetime(self):
        dt_value = self.cleaned_data['collection_datetime']
        if dt_value.tzinfo is not None and dt_value.tzinfo.utcoffset(dt_value) is not None:
            return dt_value
        return pytz.utc.localize(dt_value)
