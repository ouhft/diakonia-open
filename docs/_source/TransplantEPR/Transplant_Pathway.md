# Transplant Pathway

Original version by Mark Slaymaker, 10/07/2014

# Overview

This report is intended to be a starting point to facilitate a discussion about the requirements of the transplant patient pathway.  It aims to capture the various stages that a patient traverses.  It is intended that a patient focussed methodology be followed.  It is further hoped that, by the introduction of an efficient pathway support system, we can improve the patient experience by ensuring all the necessary information is available to the relevant team member at the appropriate time.

Once we have a full understanding of the pathway we can then conduct a gap analysis between what is required and the current features of the EPR system.  Once the gap analysis is completed we will be in a position ot develop a detailed requirements documetn stating what system needs to be developed.

It is the goal of this endeavour to provide a system to support the patient pathway within transplantation.

An orthoganoal ambition is to provide high quality research data.  In the initial stages the research data will be made available in the form of a number of standardised queries, whic ccan be parameterised.  It is anticipated that initially these queries will only produce aggregated results to maintain patient confidentiality.

The aim is to allow clinicians, managers and reserchers access to information pertaining to the performance of the transplant programme and allow identification of any trends that could warrant futher action.  We will also give consideration to how additional data collection could be integrated for additional reserch purposes.  This may need additional protocols that relate to the additional processes involved in obtaining relevant consent to tpermit the collection of supplementary information.

Throughout this document the term 'referring clinician' will be used to cover any clinician that could refer a patient including but not limited to Nephrologists, Diabetologies and GPs.

1.1  Data Needs
The data collected as a patiten traverses the pathway will be used to support several functions by fulfilling the needs of various customers.  The primary uses can be classified as:  Clinical, Managerial, Madatory reporting, Evaluation and Research.  The following givea a brief summary of the key data consumers and the types of data that they require.

1.1.1 Clinical
There is a minimum set o fdata that needs to be collected for clinical reasons.  This data is necessary to permit clinical staff to perform their function effectively and maintain patient safety.  The exact makeup of the required data will depend on the clinical specialty concerned.  Although, there will be a core set of data that will usually be needed alonside a more extensive discipline specific data set.

1.1.2. Managerial
The managerial dta collection is necessary to maintain the smooth running of the department.  It is imprortant to collect data that allows the rapid identification of potential problem areas.

1.1.3 Mandatory Reporting
There is a requirement to provide data to certain external bodies such as the Renal Registry and NHSBT.  This reporting is mandatory and the informaiton required is specified by these bodies.  It is therfore essential that any information necesary to comply with these requirements is collected in an appropriate way.

1.1.4 Evaluation/Research
This section relates to the data collecte4d over and above that needed for other purposes that will permit the critical evaluation of the performance of the department.  In addition this data can also form a core of reserach data that could be used to support studies if the appropriate ethical permission and consents are obtained.

1.2 Scope
The kidney transplant pathway is complex and there are several potential rouutes that a patient could take.  the pathway involves members of a multidiscicplinary team who provide patient care and support at different stages.  It is therefore improtant to clearly articulate the scope of this document and to highlight the elements that we consider to be within the pathway.

It is important to remember that the patient is always central to each of the stages that comprise the pathway.

It is understood that the scope is purely a boundary to the areas we provide detailed consideration to. However, as information has to flow across teh cope boundary it is therefore vital that appropriate protocols and information flows are well defined to ensure efficient communication across the boundary.

It ahs been decided that for the purpose of documenting the renal tranplant pathway we will include all interactitons from an initial referral to a transplant surgeon throug to the discharge of a patient into the care of their local referrer.  There may a need for patienets to re-enter the pathway for a number of reasons.  Additionally is is also important to record as part of the pathway information relating to the donated organ.  It is also possible that some patients are unsuitable for transplant and this information also requires recording.

1.3 Groups involved
The following is an initial list of groups and personnel who are involved in the pathway associated with transplant.

- Patient
- Nephrologist
- Surgeon
- Anaesthetist
- Theatre staff
- Pharmacist
- Transplant Coordinator
- H&I lab
- Administrative Support


Other groups that are involved or porvide support include:
- Infectious Diseases
- Radiologist
- Cardiologist
- Dietician
- Pathologist
- Laboratory
- Management
- Social Services
- Transport

1.4 Information acquisition
It is also important to ascertain how information is presented.  It will require different handling depending on the format used.  If the information is presented as paper records it will need to be rekeyed to add it to an electronic record.  This could lead to random errors being introduces.  It may therefore be advantageous to use a double entry method to help reducde the error rate.  If the information is presented in an alectronic format it is important to ascertain that all the concepts that are used are correctly mapped to a local representation.  this again could lead to systemic errors being introduced if the mappings are incorrect.  This required the agreeing semantic means of each of fileds as well as mappings between various acceptable that could be recorded in each of the fields.

1.5 Information assets
It will be necessary to identify all th ecurrent information assets that are being utilised to provide the current service.  In addition to these assets it will be necessarry to identify which assets already exist to meet the needs of the pathway and wher there are deficiencies that need to be plugged.

Currently the various data items are stored utilising multiple techniques and applications.  These inclufe EPR, Proton Excel Spreadsheets, Word documentes and paper records.

It is necessary to clearly identify how the solution that will suport this pathway fits within the strategic aims of the organisaiton as a whole.  This is clearly of imprtance as we should not follow a path that is inconsistent with the long term goals of the organisation without due consideration and consultation.

1.6 Outline of the following sections
The rest of this document is set out in a number of sections.  The next section considers what quality and audit mechanisms are necessary to allow accurate reporting of the effectiveness of the pathway.  A section providing a brief overview of the whole pathway follows this.  The following chapters concentrate on an individual portion of the pathway.  This is followed by sections on administration and notes relating to the EPR.  The final section summarises the key findings and suggestions.

# 2 Quality and Audit

It is very important to capture sufficient information to fulfil the secondary requirements created both internally and externally.  These include providing information to external bodies.  These bodies may perform one of several functions:  some require information to release payments and others collect data for the production of statistics.  The local secondary uses can include monitoring of performance and identifying any deviations from stated goals.

The quality of the data collected is paramount.  However, it is important to define the meaning of quality in the context of the data captured. A poetneial measure that could be considered is completeness.  Equally critical is the provenance, accuracy and contemporary nature of the data.

it is also vital that the organisation monitors its own performance.  This monitoring will allow the organistion to react to any negative changes to its own statistics.  Additionally the use of monitoring allows a rigourous assessment of the effect of any changes to procedures that occur.

External bodies that currently receive information includes the Renal Registry and NHSBT.  The renal registry returns are currently generated by the Proton system.  The NHSBT returns are generally generated by hand from information gathered from multiple sources.  The dat required by these organisations if reasonably weel defined, although ther is occasionaly a need for some additional translation betwee the data collected and that required for submission.

The information that would probably be useful for local analysis included:
- The total number of transplants
- The type of each transplant
- The outcome of each transplant
    - Graft failure
    - Death and functioning graft
    - Rejection
    - DGF
    - Successful
- Readmissions
- Other complications not directly related to the treatment.

2.1 Dat registry and metadata
To facilitate the reuse of data for research purposes it is necessary to clearly define the data being captured.  This includes providing a definition of each item, how the data is collected, when data is enterd, the acceptable units for the measurement and any restrictions to the acceptable range.  For reasons of data provenance it is essential that informatio is stored that details the time that the data was captured along with the person entering the data.  Any changes also need to be accurately recorded to ensure that any modifications are easily identified to enable verification.  In addition ther may be a need to record temporal informatio for procedures and processses that have a clearly identifiable staring and finishing time.
The most important this is to ensure that we capture a complete set of dat items that togerher provide a coherent piece of information related to an event.  Each of these infomration items should be signed, in some way, to help provide a degree of provenance.  In suppor of this all data should be recorded contemporaneously with respect to the events to which it relates.
