#!/usr/bin/python
# coding = models.CharField(max_length=100, verbose_name="utf-8
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils import timezone

# NB: The entire set of NHSBT records would be ideal for MongoDB

class NHSBTFile(models.Model):
    filename = models.CharField(max_length=200)
    extract_date = models.DateField()
    ingest_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "NHSBT Ingest File"
        verbose_name_plural = "NHSBT Ingest Files"


class NHSBTRecord(models.Model):
    recip_forename = models.CharField(
        max_length=50,
        verbose_name="RECIP_FORENAME",
        help_text="Recipient Forename",
        blank=True
    )
    recip_surname = models.CharField(
        max_length=50,
        verbose_name="RECIP_SURNAME",
        help_text="Recipient Surname",
        blank=True
    )
    rdob = models.DateField(verbose_name="RDOB", help_text="Recipient date of birth", null=True, blank=True)
    rnhs_no = models.CharField(max_length=12, verbose_name="RNHS_NO", help_text="Recipient NHS Number", blank=True)
    rpostcode = models.CharField(max_length=10, verbose_name="RPOSTCODE", help_text="Recipient Postcode", blank=True)
    recip_residence = models.CharField(
        max_length=20,
        verbose_name="recip_residence",
        help_text="Recipient country of residence",
        blank=True
    )
    rsex = models.CharField(max_length=10, verbose_name="RSEX", help_text="Recipient gender", blank=True)
    rethnic = models.CharField(max_length=20, verbose_name="RETHNIC", help_text="Recipient ethnicity", blank=True)
    rbg = models.CharField(max_length=3, verbose_name="RBG", help_text="Recipient blood group", blank=True)
    rrhesus = models.CharField(max_length=20, verbose_name="RRHESUS", help_text="Recipient rhesus blood group", blank=True)
    recip_id = models.CharField(
        max_length=10,
        verbose_name="RECIP_ID",
        help_text="NHSBT recipient identification number",
        db_index=True
    )
    rdod = models.DateField(verbose_name="RDOD", help_text="recipient date of death", null=True, blank=True)
    donor_forename = models.CharField(
        max_length=50,
        verbose_name="DONOR_FORENAME",
        help_text="donor forename",
        blank=True
    )
    donor_surname = models.CharField(
        max_length=50,
        verbose_name="DONOR_SURNAME",
        help_text="donor surname",
        blank=True
    )
    ddob = models.DateField(verbose_name="DDOB", help_text="donor date of birth", null=True, blank=True)
    dnhs_no = models.CharField(max_length=12, verbose_name="DNHS_NO", help_text="donor NHS Number", blank=True)
    donor_postcode = models.CharField(
        max_length=10,
        verbose_name="DONOR_POSTCODE",
        help_text="Donor postcode",
        blank=True
    )
    dresidence = models.CharField(
        max_length=20,
        verbose_name="DRESIDENCE",
        help_text="Donor country of residence",
        blank=True
    )
    dsex = models.CharField(max_length=10, verbose_name="DSEX", help_text="Donor gender", blank=True)
    dethnic = models.CharField(max_length=20, verbose_name="DETHNIC", help_text="Donor ethnicity", blank=True)
    dbg = models.CharField(max_length=3, verbose_name="DBG", help_text="Donor blood group", blank=True)
    drhesus = models.CharField(max_length=20, verbose_name="DRHESUS", help_text="Donor rhesus blood group", blank=True)
    donor_id = models.CharField(
        max_length=10,
        verbose_name="DONOR_ID",
        help_text="NHSBT donor identification number",
        db_index=True
    )
    dage = models.CharField(max_length=5, verbose_name="DAGE", help_text="Donor age", blank=True)
    dcod = models.CharField(max_length=100, verbose_name="DCOD", help_text="Donor cause of death", blank=True)
    dhtlv = models.CharField(max_length=20, verbose_name="DHTLV", help_text="Does the donor have HTLV", blank=True)
    dsyphilis = models.CharField(
        max_length=20,
        verbose_name="DSYPHILIS",
        help_text="Does the donor have syphilis",
        blank=True
    )
    dpast_alcohol_abuse = models.CharField(
        max_length=20,
        verbose_name="DPAST_ALCOHOL_ABUSE",
        help_text="past history of alcohol abuse in the donor",
        blank=True
    )
    dpast_cardio_disease = models.CharField(
        max_length=20,
        verbose_name="DPAST_CARDIO_DISEASE",
        help_text="past history of cardio disease in the donor",
        blank=True
    )
    dpast_diabetes = models.CharField(
        max_length=20,
        verbose_name="DPAST_DIABETES",
        help_text="past history of diabetes in the donor",
        blank=True
    )
    dpast_drug_abuse = models.CharField(
        max_length=20,
        verbose_name="DPAST_DRUG_ABUSE",
        help_text="past history of drug abuse in the donor",
        blank=True
    )
    dpast_hypertension = models.CharField(
        max_length=20,
        verbose_name="DPAST_HYPERTENSION",
        help_text="past history of hypertension in the donor",
        blank=True
    )
    dpast_liver_disease = models.CharField(
        max_length=20,
        verbose_name="DPAST_LIVER_DISEASE",
        help_text="past history of liver disease in the donor",
        blank=True
    )
    dpast_other = models.CharField(
        max_length=20,
        verbose_name="DPAST_OTHER",
        help_text="any other past history in the donor",
        blank=True
    )
    dpast_other_details = models.TextField(
        verbose_name="DPAST_OTHER_DETAILS",
        help_text="details of other past histories",
        blank=True
    )
    dpast_smoker = models.CharField(
        max_length=20,
        verbose_name="DPAST_SMOKER",
        help_text="past history of smoking in the donor",
        blank=True
    )
    dpast_smoker_amount = models.CharField(
        max_length=10,
        verbose_name="dpast_smoker_amount",
        help_text="past smoking amount",
        blank=True
    )
    dpast_tumour = models.CharField(
        max_length=20,
        verbose_name="DPAST_TUMOUR",
        help_text="past history of tumour in the donor",
        blank=True
    )
    dpast_uti = models.CharField(
        max_length=20,
        verbose_name="DPAST_UTI",
        help_text="past history of UTI in the donor",
        blank=True
    )
    dpast_family_diabetes = models.CharField(
        max_length=20,
        verbose_name="DPAST_FAMILY_DIABETES",
        help_text="past history of diabetes in the donor family",
        blank=True
    )
    dpast_family_diabetes_type = models.CharField(
        max_length=20,
        verbose_name="DPAST_FAMILY_DIABETES_TYPE",
        help_text="what type of family diabetes",
        blank=True
    )
    dial_at_tx = models.CharField(
        max_length=20,
        verbose_name="DIAL_AT_TX",
        help_text="was the recipient on dialysis at transplant",
        blank=True
    )
    dial_at_tx_type = models.CharField(
        max_length=20,
        verbose_name="DIAL_AT_TX_TYPE",
        help_text="what type of dialysis was the recipient on",
        blank=True
    )
    dial_start_date = models.DateTimeField(
        verbose_name="DIAL_START_DATE",
        help_text="what date did the recipient start dialysis",
        null=True,
        blank=True
    )  # NB: Naive datetime info from xlsx
    dial_end_date = models.DateTimeField(
        verbose_name="DIAL_END_DATE",
        help_text="what date did the recipient stop dialysis",
        null=True,
        blank=True
    )  # NB: Naive datetime info from xlsx
    no_prev_tx = models.CharField(
        max_length=5,
        verbose_name="NO_PREV_TX",
        help_text="had the recipient had any previous transplants",
        blank=True
    )
    tx_date = models.DateField(
        verbose_name="TX_DATE",
        help_text="date of recipients transplant",
        null=True,
        blank=True
    )
    rec_unit = models.CharField(max_length=50, verbose_name="REC_UNIT", help_text="Transplant unit", blank=True)
    rhosp_no = models.CharField(
        max_length=30,
        verbose_name="RHOSP_NO",
        help_text="recipients hospital number",
        blank=True
    )
    dtype = models.CharField(max_length=50, verbose_name="DTYPE", help_text="donor type", blank=True)
    rltnship = models.CharField(
        max_length=50,
        verbose_name="RLTNSHIP",
        help_text="relationship status of living donor transplants",
        blank=True
    )
    relationship_details = models.CharField(
        max_length=50,
        verbose_name="RELATIONSHIP_DETAILS",
        help_text="details of the relationship between recipient and donor",
        blank=True
    )
    laterality = models.CharField(
        max_length=30,
        verbose_name="LATERALITY",
        help_text="No description",
        blank=True
    )
    tx_type = models.CharField(
        max_length=30,
        verbose_name="TX_TYPE",
        help_text="Type of transplant performed",
        blank=True
    )
    local = models.CharField(
        max_length=100,
        verbose_name="LOCAL",
        help_text="was the transplant performed in the same centre as the donor",
        blank=True
    )
    faildate = models.DateField(
        verbose_name="FAILDATE",
        help_text="what date did the transplant fail",   # TODO: Investigate, because some data here predates tx date!
        null=True,
        blank=True
    )
    aitx_type = models.CharField(
        max_length=20,
        verbose_name="AITX_TYPE",
        help_text="what type of antibody incompatible transplant was performed",
        blank=True
    )
    cit_hrs = models.CharField(
        max_length=20,
        verbose_name="CIT_HRS",
        help_text="cold ischaemia time in hours",
        blank=True
    )
    fwit = models.CharField(
        max_length=20,
        verbose_name="fWIT",
        help_text="functional warm ischaemia time in minutes",
        null=True,
        blank=True
    )
    swit = models.CharField(
        max_length=20,
        verbose_name="sWIT",
        help_text="standard warm ischaemia time in minutes",
        null=True,
        blank=True
    )
    amm = models.CharField(
        max_length=20,
        verbose_name="AMM",
        help_text="how many mismatches at the A locus",
        null=True,
        blank=True
    )
    bmm = models.CharField(
        max_length=20,
        verbose_name="BMM",
        help_text="how many mismatches at the B locus",
        null=True,
        blank=True
    )
    drmm = models.CharField(
        max_length=20,
        verbose_name="DRMM",
        help_text="how many mismatches at the DR locus",
        null=True,
        blank=True
    )
    recip_hla_sample_date = models.DateTimeField(  # NB: Input data is naive
        verbose_name="RECIP_HLA_SAMPLE_DATE",
        help_text="when was the last recipient HLA sample taken",
        null=True,
        blank=True
    )
    recip_first_a_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_First_A_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_a_split = models.CharField(
        max_length=10,
        verbose_name="Recip_First_A_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_a_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_A_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_a_split = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_A_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_b_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_First_B_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_b_split = models.CharField(
        max_length=10,
        verbose_name="Recip_First_B_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_b_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_B_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_b_split = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_B_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_c_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_First_C_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_c_split = models.CharField(
        max_length=10,
        verbose_name="Recip_First_C_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_c_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_C_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_c_split = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_C_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_dr_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_First_DR_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_dr_split = models.CharField(
        max_length=10,
        verbose_name="Recip_First_DR_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_dr_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_DR_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_dr_split = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_DR_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_dp_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_First_DP_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_dp_split = models.CharField(
        max_length=10,
        verbose_name="Recip_First_DP_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_dp_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_DP_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_dp_split = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_DP_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_dq_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_First_DQ_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_first_dq_split = models.CharField(
        max_length=10,
        verbose_name="Recip_First_DQ_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_dq_broad = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_DQ_Broad",
        help_text="Recipient HLA type",
        blank=True
    )
    recip_second_dq_split = models.CharField(
        max_length=10,
        verbose_name="Recip_Second_DQ_Split",
        help_text="Recipient HLA type",
        blank=True
    )
    donor_hla_sample_date = models.DateTimeField(
        verbose_name="DONOR_HLA_SAMPLE_DATE",
        help_text="When was the last donor HLA sample taken",
        null=True,
        blank=True
    )
    donor_first_a_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_First_A_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_a_split = models.CharField(
        max_length=10,
        verbose_name="Donor_First_A_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_a_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_A_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_a_split = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_A_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_b_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_First_B_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_b_split = models.CharField(
        max_length=10,
        verbose_name="Donor_First_B_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_b_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_B_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_b_split = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_B_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_c_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_First_C_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_c_split = models.CharField(
        max_length=10,
        verbose_name="Donor_First_C_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_c_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_C_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_c_split = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_C_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_dr_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_First_DR_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_dr_split = models.CharField(
        max_length=10,
        verbose_name="Donor_First_DR_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_dr_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_DR_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_dr_split = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_DR_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_dp_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_First_DP_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_dp_split = models.CharField(
        max_length=10,
        verbose_name="Donor_First_DP_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_dp_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_DP_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_dp_split = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_DP_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_dq_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_First_DQ_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_first_dq_split = models.CharField(
        max_length=10,
        verbose_name="Donor_First_DQ_Split",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_dq_broad = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_DQ_Broad",
        help_text="Donor HLA type",
        blank=True
    )
    donor_second_dq_split = models.CharField(
        max_length=10,
        verbose_name="Donor_Second_DQ_Split",
        help_text="Donor HLA type",
        blank=True
    )
    cyclosporin = models.CharField(
        max_length=10,
        verbose_name="CYCLOSPORIN",
        help_text="Immunosuppresion and induction therapy",
        blank=True
    )
    mycophenolate_mofetil = models.CharField(
        max_length=10,
        verbose_name="MYCOPHENOLATE_MOFETIL",
        help_text="Immunosuppresion and induction therapy",
        blank=True
    )
    other_immuno_drug = models.CharField(
        max_length=10,
        verbose_name="OTHER_IMMUNO_DRUG",
        help_text="Immunosuppresion and induction therapy",
        blank=True
    )
    immuno_text = models.CharField(
        max_length=100,
        verbose_name="IMMUNO_TEXT",
        help_text="Immunosuppresion and induction therapy",
        blank=True
    )
    prednisolone_prednisone = models.CharField(
        max_length=10,
        verbose_name="PREDNISOLONE_PREDNISONE",
        help_text="Immunosuppresion and induction therapy",
        blank=True
    )
    tacrolimus = models.CharField(
        max_length=10,
        verbose_name="TACROLIMUS",
        help_text="Immunosuppresion and induction therapy",
        blank=True
    )
    azathioprine = models.CharField(
        max_length=10,
        verbose_name="AZATHIOPRINE",
        help_text="Immunosuppresion and induction therapy",
        blank=True
    )
    alg_atg = models.CharField(
        max_length=10,
        verbose_name="ALG_ATG",
        help_text="Immunosuppresion and induction therapy",
        blank=True
    )
    okt3 = models.CharField(
        max_length=10,
        verbose_name="OKT3",
        help_text="Immunosuppresion and induction therapy",
        blank=True
    )
    rcmv = models.CharField(max_length=20, verbose_name="RCMV", help_text="Recipient CMV status", blank=True)
    rhiv = models.CharField(max_length=20, verbose_name="RHIV", help_text="Recipient HIV status", blank=True)
    debv = models.CharField(max_length=20, verbose_name="DEBV", help_text="Donor EBV status", blank=True)
    dtoxo = models.CharField(max_length=20, verbose_name="DTOXO", help_text="Donor TOXO status", blank=True)
    dhiv = models.CharField(max_length=20, verbose_name="DHIV", help_text="Donor HIV status", blank=True)
    dgf = models.CharField(
        max_length=30,
        verbose_name="DGF",
        help_text="Did the recipient have delayed graft function",
        blank=True
    )
    resume_dialysis_date = models.DateTimeField(
        verbose_name="RESUME_DIALYSIS_DATE",
        help_text="when did the recipient resume dialysis post transplant",
        null=True,
        blank=True
    )
    rheight = models.CharField(max_length=10, verbose_name="RHEIGHT", help_text="recipient height", blank=True)
    # NB: Excel displays numbers like 82.6, but stores it as 82.60000000000001
    rweight = models.CharField(max_length=20, verbose_name="RWEIGHT", help_text="recipient weight", blank=True)
    serum3 = models.CharField(
        max_length=10,
        verbose_name="serum3",
        help_text="serum creatinine at 3 months",
        blank=True
    )
    scdate3 = models.DateField(
        verbose_name="scdate3",
        help_text="date of serum creatinine at 3 months",
        null=True,
        blank=True
    )
    serum12 = models.CharField(
        max_length=10,
        verbose_name="serum12",
        help_text="serum creatinine at 12 months",
        blank=True
    )
    scdate12 = models.DateField(
        verbose_name="scdate12",
        help_text="date of serum creatinine at 12 months",
        null=True,
        blank=True
    )
    serum24 = models.CharField(
        max_length=10,
        verbose_name="serum24",
        help_text="serum creatinine at 24 months",
        blank=True
    )
    scdate24 = models.DateField(
        verbose_name="scdate24",
        help_text="date of serum creatinine at 24 months",
        null=True,
        blank=True
    )
    serum36 = models.CharField(
        max_length=10,
        verbose_name="serum36",
        help_text="serum creatinine at 36 months",
        blank=True
    )
    scdate36 = models.DateField(
        verbose_name="scdate36",
        help_text="date of serum creatinine at 36 months",
        null=True,
        blank=True
    )
    serum48 = models.CharField(
        max_length=10,
        verbose_name="serum48",
        help_text="serum creatinine at 48 months",
        blank=True
    )
    scdate48 = models.DateField(
        verbose_name="scdate48",
        help_text="date of serum creatinine at 48 months",
        null=True,
        blank=True
    )
    serum60 = models.CharField(
        max_length=10,
        verbose_name="serum60",
        help_text="serum creatinine at 60 months",
        blank=True
    )
    scdate60 = models.DateField(
        verbose_name="scdate60",
        help_text="date of serum creatinine at 60 months",
        null=True,
        blank=True
    )
    rbhv = models.CharField(max_length=10, verbose_name="RBHV", help_text="recipient BHV status", blank=True)
    rhcv = models.CharField(max_length=10, verbose_name="RHCV", help_text="Recipient HCV status", blank=True)
    dhbcab = models.CharField(
        max_length=20,
        verbose_name="DHBCAB",
        help_text="donor Hep B core antigen status",
        blank=True
    )
    dhbsag = models.CharField(
        max_length=20,
        verbose_name="DHBSAG",
        help_text="donor hep B surface antigen status",
        blank=True
    )
    dhcv = models.CharField(max_length=20, verbose_name="DHCV", help_text="Donor HCV status", blank=True)
    egfr3 = models.CharField(max_length=10, verbose_name="eGFR3", help_text="recipient eGFR at 3 months", blank=True)
    egfr12 = models.CharField(max_length=10, verbose_name="eGFR12", help_text="recipient eGFR at 12 months", blank=True)
    egfr24 = models.CharField(max_length=10, verbose_name="eGFR24", help_text="recipient eGFR at 24 months", blank=True)
    egfr36 = models.CharField(max_length=10, verbose_name="eGFR36", help_text="recipient eGFR at 36 months", blank=True)
    egfr48 = models.CharField(max_length=10, verbose_name="eGFR48", help_text="recipient eGFR at 48 months", blank=True)
    egfr60 = models.CharField(max_length=10, verbose_name="eGFR60", help_text="recipient eGFR at 60 months", blank=True)

    # Temporary fields for linking to the NHIC export, until we have this stored as part of the FHIRbase
    _psuedo_id_r = models.CharField(max_length=10, default="", blank=True, db_index=True)
    _psuedo_id_d = models.CharField(max_length=10, default="", blank=True, db_index=True)

    class Meta:
        verbose_name = "NHSBT Record Row"
        verbose_name_plural = "NHSBT Record Rows"


class NHSBTLog(models.Model):
    file = models.ForeignKey(NHSBTFile)
    record = models.ForeignKey(NHSBTRecord)
    changed_fields = models.TextField(blank=True)

    class Meta:
        verbose_name = "NHSBT Ingest Log"
        verbose_name_plural = "NHSBT Ingest Logs"


class PSSPerson(models.Model):
    nhsnumber = models.CharField(
        max_length=10,
        verbose_name="nhs number",
        help_text="NHS Number",
        db_index=True
    )
    mrn = models.CharField(max_length=8, verbose_name="mrn", blank=True)
    sex = models.CharField(max_length=10, verbose_name="sex", help_text="Gender", blank=True)
    forename = models.CharField(
        max_length=50,
        verbose_name="forename",
        help_text="Forename",
        blank=True
    )
    surname = models.CharField(
        max_length=50,
        verbose_name="Surname",
        help_text="Surname",
        blank=True
    )
    birthdate = models.DateField(verbose_name="dob", help_text="date of birth", null=True, blank=True)
    deathdate = models.DateField(verbose_name="dod", help_text="date of death", null=True, blank=True)
    ethnic_group = models.CharField(
        max_length=50,
        verbose_name="ethnic group",
        help_text="Ethnic Group",
        blank=True
    )


class PSSmicroResult(models.Model):
    person = models.ForeignKey(PSSPerson)
    collection_datetime = models.DateTimeField(verbose_name="collection datetime")
    accession_number = models.CharField(max_length=10, verbose_name="accession number", blank=True)
    testcode = models.CharField(max_length=5, verbose_name="test code")
    batch_test_code = models.CharField(max_length=5, verbose_name="test code")
    result_trans = models.TextField(verbose_name="result translated", blank=True)
    result_modifiers = models.TextField(verbose_name="result modifiers", blank=True)
    res_composed_text = models.TextField(verbose_name="result text", blank=True)
    result_method = models.CharField(max_length=4, verbose_name="Result Method", blank=True)


class PSSlimsResult(models.Model):
    person = models.ForeignKey(PSSPerson)
    collection_datetime = models.DateTimeField(verbose_name="collection datetime")
    test_name = models.CharField(max_length=20, verbose_name="test name")
    min_range = models.FloatField(verbose_name="min range", blank=True, null=True)
    max_range = models.FloatField(verbose_name="max range", blank=True, null=True)
    units = models.CharField(max_length=10, verbose_name="units", blank=True)
    value_string = models.CharField(max_length=10, verbose_name="value (string)", blank=True)
    value_number = models.FloatField(verbose_name="value (float)", blank=True, null=True)
