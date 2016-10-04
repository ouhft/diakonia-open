#!/usr/bin/python
# coding: utf-8
import io

from xml.dom.minidom import Document
from lxml import etree
from lxml.builder import ElementMaker

from django.core.management.base import BaseCommand
from django.utils import timezone

from diakonia.eyeaux.models import NHSBTRecord
from diakonia.eyeaux.export_utils import psuedo_id, outer_postcode, gender_translated, ethnic_translated
from diakonia.eyeaux.export_utils import blood_group_translated, blood_rhesus_translated


class Command(BaseCommand):
    help = "Generates an XML document compliant with the v1.7.0 NHIC TRA xsd"

    def handle(self, *args, **options):
        with io.open('diakonia/eyeaux/tmp/tests.xml', mode='wb') as xml_file:
            xml_file.write(b'<?xml version="1.0" encoding="UTF-8"?>\n<!-- Output from Diakonia:eyeaux App -->\n')

            # Fetch the data for output
            records = NHSBTRecord.objects.filter(id__lt=11)

            xmlns = "https://www.w3.org/2009/01/xml.xsd"
            xsi = "http://www.w3.org/2001/XMLSchema-instance"
            nhic_xsd = "NHIC_TRA_1.7.0.xsd"

            for record in records:
                node_record = etree.Element("record", nsmap={'xsi': xsi})
                node_record.set("{"+xsi+"}noNamespaceSchemaLocation", nhic_xsd)

                # METADATA
                node_metadata = etree.SubElement(node_record, "metadata")
                etree.SubElement(node_metadata, "form-name").text = "NHIC-Transplantation"
                etree.SubElement(node_metadata, "form-version").text = "1.7.0"
                etree.SubElement(node_metadata, "date").text = timezone.now().strftime("%Y-%m-%d")
                etree.SubElement(node_metadata, "nhic_tra_245").text = "RJ1"  # Unconfirmed enumeration

                # RECIPIENT
                node_recipient = etree.SubElement(node_record, "recipient")
                etree.SubElement(node_recipient, "recipient_ID").text = "R_"+psuedo_id(record.id, False)

                # Recipient - DEMOGRAPHICS
                node_recipient_demographics = etree.SubElement(node_recipient, "demographics")
                etree.SubElement(node_recipient_demographics, "nhic_tra_0").text = "R_"+psuedo_id(record.id, False)
                etree.SubElement(node_recipient_demographics, "nhic_tra_19").text = record.recip_id
                etree.SubElement(node_recipient_demographics, "nhic_tra_6").text = str(record.rdob.year)
                etree.SubElement(node_recipient_demographics, "nhic_tra_8").text = outer_postcode(record.rpostcode)
                etree.SubElement(node_recipient_demographics, "nhic_tra_14").text = record.rsex
                etree.SubElement(node_recipient_demographics, "nhic_tra_14-1").text = gender_translated(record.rsex)
                etree.SubElement(node_recipient_demographics, "nhic_tra_15").text = record.rethnic
                etree.SubElement(node_recipient_demographics, "nhic_tra_15-1").text = ethnic_translated(record.rethnic)
                # etree.SubElement(node_recipient_demographics, "nhic_tra_16").text = ""  # GP Surgery Unknown
                etree.SubElement(node_recipient_demographics, "nhic_tra_17").text = record.rbg
                etree.SubElement(node_recipient_demographics, "nhic_tra_17-1").text = blood_group_translated(record.rbg)
                etree.SubElement(node_recipient_demographics, "nhic_tra_18").text = record.rrhesus
                etree.SubElement(node_recipient_demographics, "nhic_tra_18-1").text = blood_rhesus_translated(record.rrhesus)
                # etree.SubElement(node_recipient_demographics, "nhic_tra_20").text = ""  # Recipient Renal Registry Unknown
                if record.rdod is not None:
                    etree.SubElement(node_recipient_demographics, "nhic_tra_21").text = record.rdod.strftime("%Y-%m-%d")

                """
                # Recipient - BIOPSY
                node_recipient_biopsy = etree.SubElement(node_recipient, "biopsy")
                etree.SubElement(node_recipient_biopsy, "nhic_tra_267").text = ""  # Biopsy of Native, Pre-implantation, Explanted or Transplant Kidney?
                etree.SubElement(node_recipient_biopsy, "nhic_tra_203").text = ""  # Date of BIOPSY either NATIVE or performed on a TRANSPLANT
                etree.SubElement(node_recipient_biopsy, "nhic_tra_204").text = ""  # Biopsy report
                etree.SubElement(node_recipient_biopsy, "nhic_tra_205").text = ""  # Biopsy report ID
                # Banff Code
                node_recipient_biopsy_banff_code = etree.SubElement(node_recipient_biopsy, "banff-code")
                etree.SubElement(node_recipient_biopsy_banff_code, "nhic_tra_206").text = ""
                etree.SubElement(node_recipient_biopsy_banff_code, "nhic_tra_206-1").text = ""
                # Banff symptom category
                node_recipient_biopsy_banff_symptom_category = etree.SubElement(node_recipient_biopsy, "banff-symptom-category")
                etree.SubElement(node_recipient_biopsy_banff_symptom_category, "nhic_tra_207").text = ""
                etree.SubElement(node_recipient_biopsy_banff_symptom_category, "nhic_tra_207-1").text = ""
                etree.SubElement(node_recipient_biopsy_banff_symptom_category, "nhic_tra_208").text = ""
                # Karpinski score
                node_recipient_biopsy_karpinski_score = etree.SubElement(node_recipient_biopsy, "karpinski-score")
                etree.SubElement(node_recipient_biopsy_karpinski_score, "nhic_tra_75").text = ""
                etree.SubElement(node_recipient_biopsy_karpinski_score, "nhic_tra_76").text = ""
                etree.SubElement(node_recipient_biopsy, "nhic_tra_266").text = ""  # Diagnoses made by the Histopathologist from the Biopsy Report
                """

                # Recipient - POST-TRANSPLANT-FOLLOWUP
                node_recipient_followup = etree.SubElement(node_recipient, "post-transplant-followup")
                node_recipient_followup_height = etree.SubElement(node_recipient_followup, "height")
                etree.SubElement(node_recipient_followup_height, "nhic_tra_127").text = ""  # Measurement
                etree.SubElement(node_recipient_followup_height, "nhic_tra_128").text = ""  # Unit
                etree.SubElement(node_recipient_followup_height, "nhic_tra_129").text = ""  # Datetime
                node_recipient_followup_weight = etree.SubElement(node_recipient_followup, "height")
                etree.SubElement(node_recipient_followup_weight, "nhic_tra_130").text = ""  # Measurement
                etree.SubElement(node_recipient_followup_weight, "nhic_tra_131").text = ""  # Unit
                etree.SubElement(node_recipient_followup_weight, "nhic_tra_132").text = ""  # Datetime
                node_recipient_followup_bps = etree.SubElement(node_recipient_followup, "blood-pressure-systolic")
                etree.SubElement(node_recipient_followup_bps, "nhic_tra_241").text = ""  # Measurement
                etree.SubElement(node_recipient_followup_bps, "nhic_tra_251").text = ""  # Unit
                etree.SubElement(node_recipient_followup_bps, "nhic_tra_252").text = ""  # Datetime
                node_recipient_followup_bpd = etree.SubElement(node_recipient_followup, "blood-pressure-diastolic")
                etree.SubElement(node_recipient_followup_bpd, "nhic_tra_242").text = ""  # Measurement
                etree.SubElement(node_recipient_followup_bpd, "nhic_tra_253").text = ""  # Unit
                etree.SubElement(node_recipient_followup_bpd, "nhic_tra_254").text = ""  # Datetime
                node_recipient_followup_dgf = etree.SubElement(node_recipient_followup, "dgf")
                etree.SubElement(node_recipient_followup_dgf, "nhic_tra_124").text = record.dgf
                etree.SubElement(node_recipient_followup_dgf, "nhic_tra_124-1").text = ""
                node_recipient_followup_dialysis_modality = etree.SubElement(node_recipient_followup, "dialysis-modality")
                etree.SubElement(node_recipient_followup_dialysis_modality, "nhic_tra_125").text = ""  # Period
                etree.SubElement(node_recipient_followup_dialysis_modality, "nhic_tra_125-1").text = ""  # Translated
                etree.SubElement(node_recipient_followup_dialysis_modality, "nhic_tra_126").text = ""  # Datetime
                node_recipient_followup_hla = etree.SubElement(node_recipient_followup, "height")
                etree.SubElement(node_recipient_followup_hla, "nhic_tra_136").text = ""  # Datetime
                etree.SubElement(node_recipient_followup_hla, "nhic_tra_137").text = ""  # Locus
                etree.SubElement(node_recipient_followup_hla, "nhic_tra_138").text = ""  # Value
                etree.SubElement(node_recipient_followup_hla, "nhic_tra_139").text = ""  # result(typed)

                # Recipient - MEDICAL-HISTORY
                node_recipient_history = etree.SubElement(node_recipient, "medical-history")
                etree.SubElement(node_recipient_history, "nhic_tra_55").text = ""  # YesNo
                etree.SubElement(node_recipient_history, "nhic_tra_59").text = ""  # Int
                etree.SubElement(node_recipient_history, "nhic_tra_65").text = ""  # str
                etree.SubElement(node_recipient_history, "nhic_tra_65-1").text = ""  # Enum
                node_recipient_history_comorbidity = etree.SubElement(node_recipient_history, "comorbidity")
                etree.SubElement(node_recipient_history_comorbidity, "nhic_tra_63").text = ""  # condition
                etree.SubElement(node_recipient_history_comorbidity, "nhic_tra_64").text = ""  # Datetime
                node_recipient_history_family = etree.SubElement(node_recipient_history, "family-history")
                etree.SubElement(node_recipient_history_family, "nhic_tra_60").text = ""  # diagnosis
                etree.SubElement(node_recipient_history_family, "nhic_tra_61").text = ""  # Datetime
                etree.SubElement(node_recipient_history_family, "nhic_tra_62").text = ""  # relationship
                etree.SubElement(node_recipient_history_family, "nhic_tra_62-1").text = ""  # Enum
                node_recipient_history_dialysis = etree.SubElement(node_recipient_history, "dialysis-modality")
                etree.SubElement(node_recipient_history_dialysis, "nhic_tra_56").text = ""  # modality
                etree.SubElement(node_recipient_history_dialysis, "nhic_tra_56-1").text = ""  # Enum
                etree.SubElement(node_recipient_history_dialysis, "nhic_tra_57").text = ""  # Datetime
                etree.SubElement(node_recipient_history_dialysis, "nhic_tra_58").text = ""  # Datetime
                node_recipient_history_esrd = etree.SubElement(node_recipient_history, "esrd")
                etree.SubElement(node_recipient_history_esrd, "nhic_tra_52").text = ""  # str
                etree.SubElement(node_recipient_history_esrd, "nhic_tra_53").text = ""  # Datetime
                etree.SubElement(node_recipient_history_esrd, "nhic_tra_54").text = ""  # str

                # Recipient - DRUG-PRESCRIPTIONS
                node_recipient_prescriptions = etree.SubElement(node_recipient, "drug-prescriptions")
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_117").text = ""  # str
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_117-1").text = ""  # str
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_118").text = ""  # Datetime
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_119").text = ""  # Datetime
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_120").text = ""  # Datetime
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_121").text = ""  # str
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_122").text = ""  # str
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_123").text = ""  # str
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_123-1").text = ""  # str
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_256").text = ""  # str
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_257").text = ""  # str
                etree.SubElement(node_recipient_prescriptions, "nhic_tra_258").text = ""  # str

                # Recipient - CLINICAL-EVENT
                node_recipient_clinical_event = etree.SubElement(node_recipient, "drug-prescriptions")
                etree.SubElement(node_recipient_clinical_event, "nhic_tra_140").text = ""  # Datetime
                etree.SubElement(node_recipient_clinical_event, "nhic_tra_141").text = ""  # str

                # Recipient - SEROLOGY
                node_recipient_serology = etree.SubElement(node_recipient, "serology")
                node_recipient_serology_cmv = etree.SubElement(node_recipient_serology, "cmv")
                etree.SubElement(node_recipient_serology_cmv, "nhic_tra_97").text = ""  # str
                etree.SubElement(node_recipient_serology_cmv, "nhic_tra_98").text = ""  # Datetime
                node_recipient_serology_ebv = etree.SubElement(node_recipient_serology, "ebv")
                etree.SubElement(node_recipient_serology_ebv, "nhic_tra_99").text = ""  # str
                etree.SubElement(node_recipient_serology_ebv, "nhic_tra_100").text = ""  # Datetime
                node_recipient_serology_vzv = etree.SubElement(node_recipient_serology, "vzv")
                etree.SubElement(node_recipient_serology_vzv, "nhic_tra_101").text = ""  # str
                etree.SubElement(node_recipient_serology_vzv, "nhic_tra_102").text = ""  # Datetime
                node_recipient_serology_toxoplasma = etree.SubElement(node_recipient_serology, "toxoplasma")
                etree.SubElement(node_recipient_serology_toxoplasma, "nhic_tra_103").text = ""  # str
                etree.SubElement(node_recipient_serology_toxoplasma, "nhic_tra_104").text = ""  # Datetime
                node_recipient_serology_hiv = etree.SubElement(node_recipient_serology, "hiv")
                etree.SubElement(node_recipient_serology_hiv, "nhic_tra_105").text = ""  # str
                etree.SubElement(node_recipient_serology_hiv, "nhic_tra_106").text = ""  # Datetime
                node_recipient_serology_hep = etree.SubElement(node_recipient_serology, "hep")
                etree.SubElement(node_recipient_serology_hep, "nhic_tra_230").text = ""  # str
                etree.SubElement(node_recipient_serology_hep, "nhic_tra_280").text = ""  # Datetime
                etree.SubElement(node_recipient_serology_hep, "nhic_tra_231").text = ""  # str
                etree.SubElement(node_recipient_serology_hep, "nhic_tra_281").text = ""  # Datetime
                etree.SubElement(node_recipient_serology_hep, "nhic_tra_232").text = ""  # str
                etree.SubElement(node_recipient_serology_hep, "nhic_tra_282").text = ""  # Datetime

                # Recipient - URINE-TEST
                node_recipient_urine = etree.SubElement(node_recipient, "urine-test")
                node_recipient_urine_dip = etree.SubElement(node_recipient_urine, "urine-dip")
                etree.SubElement(node_recipient_urine_dip, "nhic_tra_188").text = ""  # Datetime
                etree.SubElement(node_recipient_urine_dip, "nhic_tra_189").text = ""  # char(30)
                etree.SubElement(node_recipient_urine_dip, "nhic_tra_190").text = ""  # char(30)
                etree.SubElement(node_recipient_urine_dip, "nhic_tra_191").text = ""  # char(30)
                etree.SubElement(node_recipient_urine_dip, "nhic_tra_192").text = ""  # char(30)
                etree.SubElement(node_recipient_urine_dip, "nhic_tra_193").text = ""  # char(30)
                etree.SubElement(node_recipient_urine_dip, "nhic_tra_194").text = ""  # char(30)
                etree.SubElement(node_recipient_urine_dip, "nhic_tra_195").text = ""  # char(30)
                node_recipient_urine_albumin = etree.SubElement(node_recipient_urine, "albumin-test")
                etree.SubElement(node_recipient_urine_albumin, "nhic_tra_197").text = ""  # Datetime
                etree.SubElement(node_recipient_urine_albumin, "nhic_tra_198").text = ""  # char(30)
                etree.SubElement(node_recipient_urine_albumin, "nhic_tra_199").text = ""  # str
                node_recipient_urine_microalbumin = etree.SubElement(node_recipient_urine, "microalbumin-test")
                etree.SubElement(node_recipient_urine_microalbumin, "nhic_tra_200").text = ""  # Datetime
                etree.SubElement(node_recipient_urine_microalbumin, "nhic_tra_201").text = ""  # char(30)
                etree.SubElement(node_recipient_urine_microalbumin, "nhic_tra_202").text = ""  # str
                node_recipient_urine_protein_creatine = etree.SubElement(node_recipient_urine, "protein-creatine-ratio")
                etree.SubElement(node_recipient_urine_protein_creatine, "nhic_tra_239").text = ""  # char(30)
                etree.SubElement(node_recipient_urine_protein_creatine, "nhic_tra_276").text = ""  # str
                etree.SubElement(node_recipient_urine_protein_creatine, "nhic_tra_277").text = ""  # datetime
                node_recipient_urine_albumin_creatine = etree.SubElement(node_recipient_urine, "albumin-creatine-ratio")
                etree.SubElement(node_recipient_urine_albumin_creatine, "nhic_tra_240").text = ""  # char(30)
                etree.SubElement(node_recipient_urine_albumin_creatine, "nhic_tra_278").text = ""  # str
                etree.SubElement(node_recipient_urine_albumin_creatine, "nhic_tra_279").text = ""  # datetime

                # Recipient - BLOOD-TEST
                node_recipient_blood = etree.SubElement(node_recipient, "blood-test")
                node_recipient_blood_serum = etree.SubElement(node_recipient_blood, "serum-creatine")
                etree.SubElement(node_recipient_blood_serum, "nhic_tra_142").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_serum, "nhic_tra_143").text = ""  # str
                etree.SubElement(node_recipient_blood_serum, "nhic_tra_144").text = ""  # datetime
                node_recipient_blood_glucose = etree.SubElement(node_recipient_blood, "blood-glucose")
                etree.SubElement(node_recipient_blood_glucose, "nhic_tra_145").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_glucose, "nhic_tra_146").text = ""  # str
                etree.SubElement(node_recipient_blood_glucose, "nhic_tra_147").text = ""  # datetime
                node_recipient_blood_ciclosporin = etree.SubElement(node_recipient_blood, "ciclosporin-level")
                etree.SubElement(node_recipient_blood_ciclosporin, "nhic_tra_154").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_ciclosporin, "nhic_tra_155").text = ""  # str
                etree.SubElement(node_recipient_blood_ciclosporin, "nhic_tra_156").text = ""  # datetime
                node_recipient_blood_tacrolimus = etree.SubElement(node_recipient_blood, "tacrolimus-level")
                etree.SubElement(node_recipient_blood_tacrolimus, "nhic_tra_151").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_tacrolimus, "nhic_tra_152").text = ""  # str
                etree.SubElement(node_recipient_blood_tacrolimus, "nhic_tra_153").text = ""  # datetime
                node_recipient_blood_hba1c = etree.SubElement(node_recipient_blood, "hba1c-level")
                etree.SubElement(node_recipient_blood_hba1c, "nhic_tra_157").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_hba1c, "nhic_tra_158").text = ""  # str
                etree.SubElement(node_recipient_blood_hba1c, "nhic_tra_159").text = ""  # datetime
                node_recipient_blood_cmv = etree.SubElement(node_recipient_blood, "cmv-viral-load")
                etree.SubElement(node_recipient_blood_cmv, "nhic_tra_160").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_cmv, "nhic_tra_161").text = ""  # str
                etree.SubElement(node_recipient_blood_cmv, "nhic_tra_162").text = ""  # datetime
                node_recipient_blood_ebv = etree.SubElement(node_recipient_blood, "ebv-viral-load")
                etree.SubElement(node_recipient_blood_ebv, "nhic_tra_163").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_ebv, "nhic_tra_164").text = ""  # str
                etree.SubElement(node_recipient_blood_ebv, "nhic_tra_165").text = ""  # datetime
                node_recipient_blood_bk = etree.SubElement(node_recipient_blood, "bk-viral-load-blood")
                etree.SubElement(node_recipient_blood_ebv, "nhic_tra_166").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_ebv, "nhic_tra_167").text = ""  # str
                etree.SubElement(node_recipient_blood_ebv, "nhic_tra_168").text = ""  # datetime
                node_recipient_blood_result = etree.SubElement(node_recipient_blood, "blood-result")
                etree.SubElement(node_recipient_blood_result, "nhic_tra_169").text = ""  # Datetime
                etree.SubElement(node_recipient_blood_result, "nhic_tra_170").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_result, "nhic_tra_171").text = ""  # str
                etree.SubElement(node_recipient_blood_result, "nhic_tra_172").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_result, "nhic_tra_173").text = ""  # str
                etree.SubElement(node_recipient_blood_result, "nhic_tra_174").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_result, "nhic_tra_175").text = ""  # str
                etree.SubElement(node_recipient_blood_result, "nhic_tra_176").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_result, "nhic_tra_177").text = ""  # str
                etree.SubElement(node_recipient_blood_result, "nhic_tra_178").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_result, "nhic_tra_179").text = ""  # str
                etree.SubElement(node_recipient_blood_result, "nhic_tra_180").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_result, "nhic_tra_181").text = ""  # str
                etree.SubElement(node_recipient_blood_result, "nhic_tra_182").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_result, "nhic_tra_183").text = ""  # str
                etree.SubElement(node_recipient_blood_result, "nhic_tra_184").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_result, "nhic_tra_185").text = ""  # str
                etree.SubElement(node_recipient_blood_result, "nhic_tra_186").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_result, "nhic_tra_187").text = ""  # str
                node_recipient_blood_gfr = etree.SubElement(node_recipient_blood, "estimated-GFR")
                etree.SubElement(node_recipient_blood_gfr, "nhic_tra_236").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_gfr, "nhic_tra_246").text = ""  # datetime
                node_recipient_blood_mycophenylate = etree.SubElement(node_recipient_blood, "mycophenylate")
                etree.SubElement(node_recipient_blood_mycophenylate, "nhic_tra_237").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_mycophenylate, "nhic_tra_247").text = ""  # str
                etree.SubElement(node_recipient_blood_mycophenylate, "nhic_tra_248").text = ""  # datetime
                node_recipient_blood_sirolimus = etree.SubElement(node_recipient_blood, "sirolimus")
                etree.SubElement(node_recipient_blood_sirolimus, "nhic_tra_238").text = ""  # char(30)
                etree.SubElement(node_recipient_blood_sirolimus, "nhic_tra_249").text = ""  # str
                etree.SubElement(node_recipient_blood_sirolimus, "nhic_tra_250").text = ""  # datetime

                # Recipient - HLA
                node_recipient_hla = etree.SubElement(node_recipient, "hla")
                node_recipient_hla_serological = etree.SubElement(node_recipient_hla, "seroligical")  # sic!
                etree.SubElement(node_recipient_hla_serological, "nhic_tra_86").text = ""  # datetime
                etree.SubElement(node_recipient_hla_serological, "nhic_tra_87").text = ""  # str
                etree.SubElement(node_recipient_hla_serological, "nhic_tra_88").text = ""  # str
                etree.SubElement(node_recipient_hla_serological, "nhic_tra_89").text = ""  # str
                node_recipient_hla_molecular = etree.SubElement(node_recipient_hla, "molecular")
                etree.SubElement(node_recipient_hla_molecular, "nhic_tra_268").text = ""  # datetime
                etree.SubElement(node_recipient_hla_molecular, "nhic_tra_269").text = ""  # str
                etree.SubElement(node_recipient_hla_molecular, "nhic_tra_270").text = ""  # str
                etree.SubElement(node_recipient_hla_molecular, "nhic_tra_271").text = ""  # str

                # Recipient - GENERIC-CONSENT
                node_recipient_consent = etree.SubElement(node_recipient, "generic-consent")
                etree.SubElement(node_recipient_consent, "nhic_tra_210").text = ""  # Enum
                etree.SubElement(node_recipient_consent, "nhic_tra_211").text = ""  # Enum
                etree.SubElement(node_recipient_consent, "nhic_tra_212").text = ""  # Enum
                etree.SubElement(node_recipient_consent, "nhic_tra_213").text = ""  # Enum
                etree.SubElement(node_recipient_consent, "nhic_tra_214").text = ""  # Enum
                etree.SubElement(node_recipient_consent, "nhic_tra_215").text = ""  # Enum
                etree.SubElement(node_recipient_consent, "nhic_tra_216").text = ""  # Datetime
                etree.SubElement(node_recipient_consent, "nhic_tra_217").text = ""  # Datetime

                # Recipient - STUDY
                node_recipient_study = etree.SubElement(node_recipient, "study")
                node_recipient_study_enrolment = etree.SubElement(node_recipient_study, "enrolment")
                etree.SubElement(node_recipient_study_enrolment, "nhic_tra_218").text = ""  # str
                etree.SubElement(node_recipient_study_enrolment, "nhic_tra_219").text = ""  # Datetime
                etree.SubElement(node_recipient_study_enrolment, "nhic_tra_220").text = ""  # str
                etree.SubElement(node_recipient_study_enrolment, "nhic_tra_221").text = ""  # Datetime
                etree.SubElement(node_recipient_study_enrolment, "nhic_tra_222").text = ""  # str
                etree.SubElement(node_recipient_study_enrolment, "nhic_tra_223").text = ""  # str
                node_recipient_study_sample = etree.SubElement(node_recipient_study, "sample-collection")
                etree.SubElement(node_recipient_study_sample, "nhic_tra_224").text = ""  # str
                etree.SubElement(node_recipient_study_sample, "nhic_tra_225").text = ""  # str
                etree.SubElement(node_recipient_study_sample, "nhic_tra_226").text = ""  # Datetime
                etree.SubElement(node_recipient_study_sample, "nhic_tra_227").text = ""  # str
                etree.SubElement(node_recipient_study_sample, "nhic_tra_228").text = ""  # str
                etree.SubElement(node_recipient_study_sample, "nhic_tra_229").text = ""  # str

                # Output the record
                xml_file.write(etree.tostring(node_record, pretty_print=True, encoding="UTF-8"))

            """
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


                # RECIPIENTS


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
            """
