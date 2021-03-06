# Transplant Pathways (DRAFT)

* Original version by *Mark Slaymaker*, 10/07/2014, Draft 1.0.0
* Updates via *Ally Bradley* and *Carl Marshall*, 11/11/2016
* Currently v1.0.3, July 2017

## Overview

This report is intended to be a starting point to facilitate a discussion about the requirements of the transplant patient pathway. It aims to capture the various stages that a patient traverses. It is intended that a patient focussed methodology be followed. It is further hoped that, by the introduction of an efficient pathway support system, we can improve the patient experience by ensuring all the necessary information is available to the relevant team member at the appropriate time.

Once we have a full understanding of the pathway we can then conduct a gap analysis between what is required and the current features of the EPR system. Once the gap analysis is completed we will be in a position to develop a detailed requirements document stating what system needs to be developed.

It is the goal of this endeavour to provide a system to support the patient pathway within transplantation.

An orthogonal ambition is to provide high quality research data. In the initial stages the research data will be made available in the form of a number of standardised queries, which can be parameterised. It is anticipated that initially these queries will only produce aggregated results to maintain patient confidentiality.

The aim is to allow clinicians, managers and researchers access to information pertaining to the performance of the transplant programme and allow identification of any trends that could warrant further action. We will also give consideration to how additional data collection could be integrated for additional research purposes. This may need additional protocols that relate to the additional processes involved in obtaining relevant consent to permit the collection of supplementary information.

Throughout this document the term '*referring clinician*' will be used to cover any clinician that could refer a patient including but not limited to Nephrologists, Diabetologists, and GPs.

### 1.1 Data Needs

The data collected as a patient traverses the pathway will be used to support several functions by fulfilling the needs of various customers. The primary uses can be classified as: Clinical, Managerial, Mandatory reporting, Evaluation and Research. The following give a brief summary of the key data consumers and the types of data that they require.

#### 1.1.1 Clinical

There is a minimum set of data that needs to be collected for clinical reasons. This data is necessary to permit clinical staff to perform their function effectively and maintain patient safety. The exact makeup of the required data will depend on the clinical specialty concerned. Although, there will be a core set of data that will usually be needed alongside a more extensive discipline specific data set.

#### 1.1.2 Managerial

The managerial data collection is necessary to maintain the smooth running of the department. It is important to collect data that allows the rapid identification of potential problem areas.

#### 1.1.3 Mandatory Reporting

There is a requirement to provide data to certain external bodies such as the Renal Registry and NHSBT. This reporting is mandatory and the information required is specified by these bodies. It is therefore essential that any information necessary to comply with these requirements is collected in an appropriate way.

#### 1.1.4 Evaluation/Research

This section relates to the data collected, over and above that needed for other purposes, that will permit the critical evaluation of the performance of the department. In addition this data can also form a core of research data that could be used to support studies if the appropriate ethical permissions and consent are obtained.

### 1.2 Scope

The kidney transplant pathway is complex and there are several potential routes that a patient could take. The pathway involves members of a multidisciplinary team who provide patient care and support at different stages. It is therefore important to clearly articulate the scope of this document and to highlight the elements that we consider to be within the pathway.

It is important to remember that the patient is always central to each of the stages that comprise the pathway.

It is understood that the scope is purely a boundary to the areas we provide detailed consideration to. However, as information has to flow across the scope boundary it is therefore vital that appropriate protocols and information flows are well defined to ensure efficient communication across the boundary.

It has been decided that for the purpose of documenting the renal transplant pathway we will include all interactions from an initial referral to a transplant surgeon through to the discharge of a patient into the care of their local referrer. There may be a need for patients to re-enter the pathway for a number of reasons. Additionally is is also important to record as part of the pathway information relating to the donated organ. It is also possible that some patients are unsuitable for transplant and this information also requires recording.

### 1.3 Groups involved

The following is an initial list of groups and personnel who are involved in the pathway associated with transplant.

- Patient
- Nephrologist
- Surgeon
- Anaesthetist
- Theatre staff
- Pharmacist
- Transplant Coordinator
- Clinical Nurses
- H&I lab
- Administrative Support

Other groups that are involved or provide support include:

- Infectious Diseases
- Radiologist
- Cardiologist
- Dietician
- Pathologist
- Laboratory
- Management
- Social Services
- Transport

### 1.4 Information acquisition

It is also important to ascertain how information is presented. It will require different handling depending on the format used. If the information is presented as paper records it will need to be rekeyed to add it to an electronic record. This could lead to random errors being introduced. It may therefore be advantageous to use a double entry method to help reduce the error rate. 

If the information is presented in an electronic format it is important to ascertain that all the concepts that are used are correctly mapped to a local representation. This again could lead to systemic errors being introduced if the mappings are incorrect. This requires agreeing the semantic means of each of the fields, as well as mappings between various acceptable values that could be recorded in each of the fields.

### 1.5 Information assets

It will be necessary to identify all the current information assets that are being utilised to provide the current service. In addition to these assets it will be necessary to identify which assets already exist to meet the needs of the pathway and where there are deficiencies that need to be plugged.

Currently the various data items are stored utilising multiple techniques and applications. These include EPR, Proton, Excel spreadsheets, Word documents, and paper records.

It is necessary to clearly identify how the solution that will support this pathway fits within the strategic aims of the organisation as a whole. This is clearly of importance as we should not follow a path that is inconsistent with the long term goals of the organisation without due consideration and consultation.

### 1.6 Outline of the following sections

The rest of this document is set out in a number of sections. The next section considers what quality and audit mechanisms are necessary to allow accurate reporting of the effectiveness of the pathway. A section providing a brief overview of the whole pathway follows this. The following chapters concentrate on an individual portion of the pathway. This is followed by sections on administration and notes relating to the EPR. The final section summarises the key findings and suggestions.

## 2 Quality and Audit

It is very important to capture sufficient information to fulfil the secondary requirements created both internally and externally. These include providing information to external bodies. These bodies may perform one of several functions: some require information to release payments, and others collect data for the production of statistics. The local secondary uses can include monitoring of performance and identifying any deviations from stated goals.

The quality of the data collected is paramount. However, it is important to define the meaning of quality in the context of the data captured. A potential measure that could be considered is completeness. Equally critical is the provenance, accuracy, and contemporary nature of the data.

It is also vital that the organisation monitors its own performance. This monitoring will allow the organisation to react to any negative changes to its own statistics. Additionally the use of monitoring allows a rigorous assessment of the effect of any changes to procedures that occur.

External bodies that currently receive information includes the Renal Registry and NHSBT. The renal registry returns are currently generated by the Proton system. The NHSBT returns are generally generated by hand from information gathered from multiple sources. The data required by these organisations is reasonably well defined, although there is occasionally a need for some additional translation between the data collected and that required for submission.

The information that would probably be useful for local analysis includes:

- The total number of transplants
- The type of each transplant
- The outcome of each transplant
  - Graft failure
  - Death and functioning graft
  - Rejection
  - DGF
  - Successful
- Re-admissions
- Other complications not directly related to the treatment

### 2.1 Data registry and metadata

To facilitate the reuse of data for research purposes it is necessary to clearly define the data being captured. This includes providing a definition of each item, how the data is collected, when data is entered, the acceptable units for the measurement, and any restrictions to the acceptable range. For reasons of data provenance it is essential that information is stored that details the time that the data was captured along with the person entering the data. Any changes also need to be accurately recorded to ensure that any modifications are easily identified to enable verification. In addition, there may be a need to record temporal information for procedures and processes that have a clearly identifiable starting and finishing time.

The most important thing is to ensure that we capture a complete set of data items that together provide a coherent piece of information related to an event. Each of these information items should be signed, in some way, to help provide a degree of provenance. In support of this all data should be recorded contemporaneously with respect to the events to which it relates.

## 3 Pathway Summary

The contents of this section represent our current understanding of the pathway. Figure 1 provides an abstract summary of the pathway. The subsequent sections will provide a more detailed description of each process. As far as possible the data required to support each process will be identified along with the source of the data. 

Our current understanding is that a patient follows one of several possible pathways from referral to the eventual outcome.

The simplified pathways can be summarised as:

1. Referral
2. Outpatient appointment (which on the initial appointment normally includes work up)
   1. Refusal is a potential outcome of the outpatient appointment
   2. Recommendation to consider for listing
3. Listing discussion
   1. Refusal
   2. Further investigation
   3. Accepted onto the waiting list
4. Activation
   1. Tissue typing
5. Waiting List
6. Transplant
   1. Tissue typing - confirm compatibility
   2. Donor information
   3. Organ (Biopsy)
   4. Anaesthetic assessment
   5. Operation (Post admission tests)
7. Post operation
8. Discharge
9. Follow-up at outpatients
   1. Initial follow-up is local
   2. Finally patient is discharged to their referring unit for further follow-up
10. Events
   1. Outpatient
   2. Telephone contact
   3. Admission

There are a number of outcomes possible at various stages of the pathway. The patient can proceed to the next step, require further investigations, or be turned down for transplant.

There is a potential for a number of individuals to be involved at each stage in the pathway, who each have a responsibility for ensuring different portions of the required information is collected. 

The overall target is to ensure that sufficient information is available to allow it to be accessed in an appropriate manner to reach a decision.

![Figure 1: Pathways with scope](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_figure_1.svg)

### 3.1 18 Week referral to treatment pathway

There is a maximum time of 18 weeks between the referral being recorded and a final decision about treatment, either refusal or entry onto the waiting list. The general rule is that there should not be more than 18 weeks between referral and first treatment. In the case of transplant, first treatment is considered to be acceptance onto the waiting list or being deemed unsuitable for transplant. An illustration of the timeline for the case of being accepted onto the waiting list is outlined in Figure 2. The 18 weeks may not be contiguous, as there are various reasons that can cause the clock to be temporarily stopped. If the clock has been stopped it may subsequently be restarted if appropriate events occur at a future time. This is discussed more fully in Section 5 below.

*NOTE: The 18 week pathway is currently managed via an Excel spreadsheet. It should also be noted that there is a suggested maximum of 6 weeks between referral and the first outpatient appointment.*

![Figure 2: 18 Week Timeline](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_figure_2.svg)

## 4 Satellite organisations

There are a number of satellite organisations that will interact with the patient pathway, who may have different Information Technology (IT) solutions. To prevent this being a problem it will be necessary to have clearly defined protocols with respect to the information being passed between the organisations. These protocols will have to define minimum acceptable data sets for each possible interaction. The definitions will have to include field names along with acceptable pseudonyms, the type of data being recorded, and (if applicable) a range for acceptable values including any relevant units. If electronic information interchange can be agreed then it will minimise the amount of human intervention (and error) necessary to incorporate data from satellite sites.

## 5 Other general comments

At various points in the patient pathway numerous forms are currently filled in. Further details about the content of these forms is to be provided at the relevant places within this document. A copy of each form needs to be obtained and annotated to indicate the minimum amount of information that has to be collected. This will help to identify the source of the data required at each stage of the pathway as well as the data that is supplied by each of the stages.

There are a number of coordinators who are responsible for dealing with referrals for all the transplant programmes:

- Kidney
- Kidney and pancreas
- Pancreas
- Islet cells
- Kidney and islet cells
- Small bowel

Although there is a separate living donor team, they interface closely with the deceased donor kidney team.

The RTC (Renal Transplant Coordinators), in addition to other roles and responsibilities, perform the following tasks:

- Waiting list management
- Call in patients

There is currently a separate team that performs the function of post transplant follow up.

There is a potential for patients to switch between lists for various reasons, including:

- Failed transplants - which can potentially result in the patient being relisted 
- Second transplant - this may be a different organ (e.g. pancreas transplant after a kidney transplant)
- Patient no longer fit - for their originally planned transplantation such as a SPK but are still suitable for lesser option of renal transplant only.

**NHSBT** - currently submissions to the NHSBT from the transplant team are via manually completed paper forms which are completed after gathering data from multiple sources. 

Some forms can be automatically generated by Proton. As the Proton functionality is migrated to the EPR system it is hoped that these features can be maintained and additional forms added. This is however dependent on the priorities set during the migration from Proton to EPR.

**SUG:** It is the intention of the project team to concentrate on kidney only transplantation in the first instance. The lessons learned from this work will help inform the development of appropriate solutions for other transplant treatments.

## 6 Referral

**NOTE:** Referral letters MUST be processed in accordance with any OUH NHS Trust SOP. The receipt of the referral letter is the start of the 18 week referral to treatment clock. On receipt of the referral letter, it should be stamped with a date. This date indicates the start of the 18 week referral to treatment (RTT) pathway which is illustrated in Figure 2.

The referral is the initial contact with the unit and is usually in the form of a physical letter. The quality of the information supplied is variable. It is however possible for referrals to be received in alternate ways including but not limited to:

- Electronic transfer
- Email
- Phone conversations
- Self referral

The remainder of this section identifies the mechanisms involved in referral and the information flows that are expected to occur.

![Figure 3: Referral Stage](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_figure_3.svg)

### 6.1 Standard Operating Procedures (SOP)

The trust's standard procedure for logging referrals should be followed. The patient should be entered into the EPR system along with all of the information available at this point in time.

### 6.2 Inputs

The referral, usually a letter, is the only input available at this time. The referral should include at least the patient's name, contact details, and reason for referral. It would be useful if additional information pertaining to medical history and medications could be included.

#### 6.2.1 Where do referrals come from?

Typically a referral to a transplant surgeon is generated by a referring clinician. The referring clinician may be based locally in Oxford, in one of the satellite centres closely associated with Oxford, or potentially from further afield. In some circumstances it is possible to get self referrals. It is also possible to get referrals from other centres asking for a second opinion.

#### 6.2.2 What information is essential for a valid referral?

The more details provided in the referral the better. It is essential to have contact details and some details about the referral. In general, the following would be a good starting point:

- Demographic information
  - Patient name
  - Patient contact details
- GP information
- Referrer details
- BMI
- Patient clinical history
- Medications
- Allergies
- Dialysis status
- LRD option is appropriate
- Cardiac investigations and results
- Reason for referral
- Type of transplant required

It has been suggested that there could be an improvement in the quality of information provided at the time of referral if a pro-forma template was provided to referring clinicians. This could be tailored to the type of referral. The initial sections should contain suitable space to allow the capture of essential information. Additional sections could ask for the information that would be 'nice to have'.

### 6.3 Queries required

There may be a need to specify a report that provides information about the number of referrals that have been received. It would also be of benefit for the management of the department to know the average time from referral to treatment, along with any outliers that exceed the 18 week time limit. Further reports detailing the number of DNA or withdrawals may also be useful for the management of the department.

### 6.4 Actors involved

The following are generally involved in the referral process:

- Patient
- Referring clinician
- Surgeon
- Receiver and processor of the referral, e.g.:
  - Secretaries. Consultant and ANP receive and agree assessment to proceed. Then calls admin to make and send an appointment.
  - Admin (managed by office manager)
  
### 6.5 Processes involved

An outpatients appointment is generated after the basic information contained within the referral letter is entered onto the EPR system. It is required that patients are seen within 6 weeks of the receipt of the referral letter.

It is possible that the patient is referred onto a different speciality.

### 6.6 Information generated and stored

A summary of the information gathered at referral is presented in Table 1. The majority of the information generated by this phase of the pathway is stored in the EPR.

![Table 1: Data captured at referral](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_table_1.svg)

### 6.7 Outputs

There are a number of potential outcomes from a referral:

- Outpatient appointment
- Request for additional information from the referring clinician
- A refusal to proceed

The primary goal of this phase of the pathway is a letter inviting the patient to attend an outpatient appointment. In addition, the basic demographic information should have been entered into the EPR. This information will need to be validated at the time the patient attends the outpatient appointment. 

A refusal can occur at any stage of the pathway if the consultant feels that it is indicated. Also, the patient can change their mind and decline a transplant at any point.

### 6.8 Other comments

**SUG:** It would improve the process if all referrals contained the essential information pertaining to the reason for referral. Additional benefit may also be obtained if certain standard clinical investigations could be either scheduled or completed around the time of referral. e.g. cardiac mps?

**NOTE:** The referral letter should be digitised and attached to the patient record. This could make up the initial entry on the timeline. 

**NOTE:** If a local system is developed the information from the EPR needs to be visible to local users without rekeying. It is important that there is no additional work created by the requirement to rekey data.

Ideally, all the required information associated with the referral would be supplied in an electronic format by the referring clinician. This would permit the incorporation of the information in the patient record without the need to rekey. In addition to the potential time saving, the removal of the manual rekeying reduces the chance of typographic errors being introduced. The minimum information that should be included in a referral is the demographic information. A reasonable minimum referral should include: name, address, contact details, DoB, GP, and details of the reason for the referral. It is also imperative that the date of receipt of the referral is recorded to ensure that the first offer of an appointment is within the target time scales.

## 7 Outpatient appointment

The outpatient appointment is the initial contact with the patient. During this appointment a transplant assessment form is completed alongside other tests to gather the necessary information to permit a decision to be made about suitability for transplant. The patient arrives for assessment and the demographic information already in the system is validated. If tests have been performed previously then some of the information required might already be available.

![Figure 4: Outpatient Stage](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_figure_4.svg)

### 7.1 Assessment process

The first appointment should occur within 6 weeks of receiving the referral. At the outpatient appointment a Consultant and Nurse perform a Transplant Assessment using a standard form. This form is designed to capture the information necessary to enable a listing meeting to make an appropriate decision. This form does include diagrams that are annotated when the clinical examination is conducted.

It would be beneficial to have an electronic version of the form that recorded the information directly into a suitable information system. 

In addition an anaesthetic assessment section should be completed as part of the outpatient appointment. This should be forwarded to the anaesthetist in advance to enable them to request additional tests if that is appropriate.

The assessment usually include:

- Blood tests, with the results being available from the EPR
- X-rays
- Tissue typing (H&I lab)
- ECG

Additional tests can include:

- Chest - CXR, PFTs, CPEX
- Cardiology - heart MPS, coronary angio stent cardiac surgery
- Myocardial perfusion scans
- Other - canoud? dopplers, duplex, CT

In addition input may be required from:

- Pharmacist
- Dietician
- Psychologist

All of the data collected is used to make an assessment of the suitability of the patient for transplant. Additional tests can be ordered at different times. The results of tests take variable amounts of time to become available. It is therefore essential that any system notifies an appropriate person when all of the data becomes available, or if a particular timeout has been exceeded.

During the assessment phase, and subsequent phases, it is necessary to get positive confirmation from the patient of the current medication, as any information recorded in the system may be out of date.

It is also desirable to obtain positive confirmation of allergies at the same time. 

Blood tests may be done on the day of the assessment or at subsequent appointments possibly at the patient's local centre. It is unlikely that these results will be available immediately. Currently tests for out patients are ordered on paper but this should become electronic ordering as the EPR rollout continues.

In addition to the completion of the assessment form the patient is asked to sign several consent forms:

- DPA related to permit the sending of information to NHSBT
- Consent for virology test - in particular HIV
- Consent for a photograph to be taken and added to work-up documents
- Consent to go on the waiting list (is this currently done?)

The consent forms are currently filled in by hand, with some of the information duplicated on each of the forms. One of the forms goes to NHSBT the others are stored locally. It is possible for forms to be mislaid. A method of reducing the duplication of information would be beneficial. 

It would also be beneficial to have an electronic version of the consent forms associated with the patient record.

It is also necessary to take account of potential exceptions to the usual progress through the transplant pathway. For instance special measures may need to be taken to prevent discrimination against patients from particular groups or suffering from particular ailments, such as:

- Jehovah's Witnesses
- Allergies
- Other issues

### 7.2 Inputs

For an outpatient appointment to occur several things need to be in place:

- A record of the patient on the system that needs to be verified
- The patient needs to attend
- The patient needs to bring any additional information requested at the time the appointment was sent out.

However, the primary input to the outpatient appointment is the referral letter and any associated patient history it includes. It is therefore imperative that the referral letter is available either physically or electronically.

### 7.3 Actors involved

The following are normally involved in the outpatient appointment stage:

- Patient
- Surgeon
- Coordinator
- Tissue typing (H&I lab)

These are potentially involved:

- Radiologist
- Phlebotomist
- Nursing staff
- Laboratory staff
- Secretarial support
- Pharmacist
- Cardiology
- Dietician
- Psychologist

### 7.4 Processes involved

Each of the individual tests ordered could be considered a sub-process. They will each have their own SoPs that govern how the patient is evaluated and the results returned.

### 7.5 Information generated and stored

The data is potentially captured in a number of ways:

* EPR will capture demographic data as well as that pertaining to lab results
* PACS will contain radiographic information
* The H&I lab system will contain additional information not available in EPR
* ECG information is captured, though potentially this is only in paper format
* Proton currently captures any information related to the pharmacist although this is likely to change in the near future as the ePrescribing module of the EPR is rolled out

In addition there is a form to be filled in during the assessment process. This is currently a paper form. This could be translated into a form on EPR to allow the electronic capture of data.

### 7.6 General data

- Demographics
  - NHS number
  - Hospital number (MRN)
  - Name
  - DoB
  - Address
  - Contact numbers
  - Age
  - Gender
  - Ethnicity
  - Employment
  - NOK
  - GP details

- Referral details
  - Date
  - Clinic
  - Tx Surgeon
  - Tx Coordinator
  - Local coordinator
  - Organ(s) required
  - Clock start
  - Clock stop
  - Reason
  - Referring consultant
  - Contact details
  - Dialysis unit

- Transport plan
  - Own transport
  - Hospital transport
  - Plan
  - Pre-authorisation code
  - Backup?
 
- Is there a LD Kidney option?

- Clinical basics
  - Height
  - Weight
    - BMI
  - Hip/waist ratio
  - BP
  - Pulse
  - SF-36 Questionnaire
  - Hypoglycaemia questionnaire

- Renal History (diabetic)
- Past medical history
- Past surgical history
- Drug history
- Anaesthetic assessment
- Social history
- Check list
  - PAP smear date
  - Mammogram date
  - Pregnancies
  - Blood transfusions 
    - Date
  - VZV immunity
  - Female less than 55 years and Rh neg?
- Clinical Examination
  - Diagrams to complete
- Plan and investigations required
- Date
- Assessing surgeon
- Assessing coordinator
- Cardiac investigation outcomes
  - Type of scan
  - Date
  - Centre
  - Report Details
- Cardiology MDT Summary
  - Date 
  - Present
  - Summary
- Blood test results
- Urine test results
- H&I lab results

### 7.7 Consent Forms

#### 7.7.1 Sample Consent Form

- Hepatitis B surface antigen
- Hepatitis B core
- Hepatitis C IgG
- HIV 1 and 2 antibody
- Herpes zoster IgG antibody
- Treponema pallidum ELISA
- Epstein Barr virus
- Cytomegalotvirus IgG antibody
- Syphillis
- Toxoplasmosis
- Herpes Simplex
- Name
  - Signature
  - Date
- Coordinator name
  - Signature
  - Date

#### 7.7.2 Clinical Photography
 
- Hospital number
- Name
- Address
- DoB
- Department/Ward
- Consultant
- Clinician's name
  - Signature
- Photographs details
  - Taken by
  - Badge number
  - Job title
  - Location of photography
  - Date
  - Location of stored image files

Consent level 1

- signature of patient
- date
- name of signatory (if different from patient)
- relationship

Consent level 2 (restricted education use)

- signature of patient
- date
- name of signatory if different from patient
- relationship
 
Consent level 3

- Individual consent for each image
 
#### 7.7.3 Recipient consent form
 
Consent
 
- Understand voluntary consent for data use by NHSBT
  - Initial
- All data shared as necessary
  - Initial
- Signature of patient
- Date  
- Witness signature
- Date
- Representative signature (if necessary)
- Date
- Name of representative
 
Refusal of consent
 
- Understand refusal may jeopardise chances
  - Initial
- Refuse consent for certain items
  - Initial
  - Specify items
- Refuse consent for all information
  - Initial
- Signature of patient
  - Date
- Witness signature
  - Date
- Representative signature
  - Date
  - Name of representative
 
#### 7.7.4 Outpatient outcome form
 
- Consultant
- Clinic prep
- Reception
  - Patient type (NHS/Private/Overseas)
- Clinical staff
  - Patient on 18 week pathway
- Outcome of attendance
  
### 7.8 Outputs

The potential results of the OPA are:

- The patient is put forward to a listing meeting (considered an appropriate candidate)
- The patient is not considered to be a suitable candidate and a refusal is granted
 
The ultimate output from this section is a letter, wither indicating that the patient is being forwarded to the listing meeting or that they are an unsuitable candidate for transplantation.
 
Letters are usually generated using the ALDEN system.

- The letter is dictated or typed
- Dictated letters are sent for transcription
- The content is checked by the author
- A secretary performs final formatting tasks
- The letter is stored in the renal directory (R:) as well as being added to Proton
 
### 7.9 Notes
 
Some procedures exit in various states.
 
- Transplant immunology -> SOPs
- Protocols on intranet for all transplant programmes reviewed
- Renal 
  - Transplant intranet 
  - link to other OUH documents
- Renal transplant RTC SOP (Renal directorate server)
 
It is not clear if the EPR system captures all of the information required for the assessment. If the EPR system does not collect all of the necessary information it is probable that an additional system will need to be developed that will operate in conjunction with the EPR system.

**SUG:** A system should allow the storage of the letter as part of the overall patient record. In addition it should also form part of the patient's timeline. Note: Apparently this is being incorporated into the EPR system.

**SUG:** A template for a letter could be provided that is automatically populated with the relevant test result and other assessment findings. The surgeon could then add any customisations that were appropriate for the individual patient.

**Note:** Islet and bowel cases do not always fit into the 18 week time frame as the assessments can be complex.


## 8 Listing Meeting

The final decision about the suitability of a candidate patient for transplant is made at the listing meeting. The outcome of the meeting dictates the next stage for the patient in the pathway.

The meeting is a multi-profession meeting.

**SUG:** It is important to identify any items of information that should be circulated to all attendees prior to the meeting being convened. For each item of information that is required the format and acceptable content should be defined. It is easier to circulate information if it is in an electronic form.

![Figure 5: Listing Meeting](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_figure_5.svg)

### 8.1 Inputs

The inputs to this process are the outputs of the outpatient appointment phase and the initial referral letter. This includes the letter detailing the recommendation as the result of a cardiology MDT meeting, test results, and any other information available at the time of the meeting.

The general information to complete the NHSBT form is currently obtained from several sources including:

- Word documents containing patient demographics
- Lab reports from EPR
- Dialysis data from
- Assessment
- Proton
- Referral letter
 
Also recorded:

- Height
- Weight -> BMI
- QoL and hypoglycaemia awareness from a paper questionnaire and clinical assessment - only in word document
 
### 8.2 Actors involved

The following are usually involved in the listing meeting

- Nephrologist
- Surgeon
- Anaesthetist
- Coordinator
- Tissue typing (H&I lab)

### 8.3 Procedure

There should be a record of who attended the meeting. There should be a brief record of discussions that occurred, and this should be attached to the patient's timeline. A record of the consensus view should be kept along with any reservations raised. There should be a record of the reasons for declining a patient.

If the patient is deemed suitable for listing then the NHSBT pre-registration data needs to be collected and the following done:

- Complete the form so the patient is registered with NHSBT
- Send the form to the H&I lab for tissue type information to be added prior to being sent off

Paper form is faxed to NHSBT at the time of registration

We are currently focusing on the requirements for renal transplant but it is worth noting that there are some differences between each programme as to the criteria to go on the waiting list.

### 8.4 Information generated and stored

The following data artefacts should be generated by the listing meeting:

- Listing MDT Summary and Transplant Plan
  - Date
  - Present
  - Issues Discussed/concerns raised
  - Outcomes/Actions
  - Consultant Sign off
- Letter to patient
- Letter to GP/referring clinician
- NHSBT form

Data to register the patient on the waiting list including:

- Blood group
- Tissue type details

### 8.5 Outputs

The ultimate output of the meeting is a letter to the patient and GP (?) indicating whether or not the patient has been accepted onto the waiting list. In addition, if the patient is recommended for listing then the appropriate NHSBT forms should be completed and sent off.

### 8.6 Notes

**SUG:** Automated letter production

A standard letter template *should* be created appropriate to each specialty. The letter should be automatically populated with any information available from the system (EPR) along with entered information. Information entered should be via a template captured via an input form appropriate to the specialty. A combination of dropdowns and text areas should be used to permit the entry of information that completes standardised prose. Entered information should also be stored to facilitate searching for items of interest at a later point in time.

The letter will either be requesting the addition of the patient to a waiting list or the refusal of the patient.

If the outcome is positive, the letter requests the activation of the patient on the waiting list. This letter is sent to the H&I lab. It is necessary for this letter to be signed before the H&I lab forward the form to NHSBT.

**QUE:** Could this letter be in an electronic format and be signed with a digital signature?

## 9 Waiting List

At present there is an Excel spreadsheet that is used for managing the patients transition through the pathway. The spreadsheet records pertinent information that is required for ensuring that the 18 week time frame is complied with. The information includes items such as:

- Date of appointment
- Date that the clock started on the 18 weeks (as well as clock stop/restart)
- A paper admin form has the code for the next stage and start/stop clock

![Figure 6: Waiting List](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_figure_6.svg)

### 9.1 Inputs

The inputs to this stage of the pathway are the decision of the listing meeting along with the information collected to this point. Additional inputs can take the form of communications relating to the patient. These communications can take many forms such as telephone calls, emails, and letters. 

### 9.2 Queries required

**Reports:** Currently information has to gathered from multiple sources to be able to generate results and reports. Some of these reports form the basis of submissions to relevant external bodies. It could be useful to generate periodic reports that give up-to-date figures relating to the activity of the department as well as the status of patients. This would allow closer monitoring of the number of patients on the waiting list and the proportion of patients in each potential waiting list state.

### 9.3 Actors involved

The following are the primary participants at this stage:

- Patients
- Coordinators

In addition there will be periodic input from clinical specialists as required.

### 9.4 Processes involved

While on the waiting list each patient can be in one of several states:

- An active work up patient
- Be suspended for any one of a number of reasons, such as:
  - Overweight/high BMI
  - Cardiac issues
  - Anything else that could cause additional complications with the transplant
 
If a patient is removed from the active list they can be reactivated when they are considered fit. A multi disciplinary team (MDT) is responsible for assessing the patient's fitness for listing in the case of kidney or kidney and pancreas.

The bowel transplant team have separate listing meetings.

Cardiology meet fortnightly for fitness discussions. This is a physical meeting and actions are taken at the meeting.

If the patient is from another centre and radiology images need to be reviewed there is an image exchange portal for images from other centres. This can introduce delays into the process if investigations are carried out by local centres. This is because the process is currently very labour intensive.

For some patients on the waiting list there is a need for a periodic review, usually annually, see section below. There is also some biannual cardiac testing (annual for Type 1 DM).

**SUG:** System should automatically flag tests needed and review dates. Notify of annual annual review.

If the tests are to be carried out at another centre the system should flag when a test being carried out remotely has not been reported within a predefined period of time. 

### 9.5 Information generated and stored

Data locations:

* MedCon - Cardiologist information
* PACs - images

We need to be able to record when a patient has their waiting list status either activated or suspended. It is important for this information to be accurate. 

**NOTE:** It has been suggested that it would be useful to generate a letter automatically for the patient and clinician. This letter would provide details about the status update as well as indicate the next follow up.

Other information that may be generated while the patient is on the waiting list includes:

- Letters:
  - from other centres are not currently scanned
  - Cardiology letters on a different system to Proton letters
  - nternal and external letters not centrally accessible
- Telephone conversations
- Emails
 
Keeping up with externally sourced information such as letters, emails etc can be problematic (it might be helpful to have some form of notifications alongside scanning).
 
Monthly reports are sent to other centres to keep them informed about the status of their patients. Mainly:

- Where in the work-up process they are
- What, if anything, is causing delays
- Who is active/suspended/transplanted

This is currently managed in an Excel spreadsheet.

This is a very time consuming process which typically involves a lot of cutting and pasting. The manual nature of this process increases the possibility of minor errors being introduced.

**SUG:** Would it be possible to allow external read only access to reduce work?

**QUE:** What would the granularity of access be for external users? They should only have access to their own patients.

The information is currently stored on the 'Renal (R:) drive'. There is no linking between the different portions of the information.

**SUG:** This would be better organised using a central information store which mandated consistent (standardised) coding of information.

Word documents contain the threads of communication.

- Emails are cut and pasted into the word document
- This forms a timeline with a sequence of events recorded by virtue of their order in the document
- This allows conversations and requests to be tracked
- On call coordinator has access to the information especially that associated with health

Patient notes are occasionally unavailable or missing.
 
The patient notes at listing consists of 2 sets:
 
 - Buff - General hospital notes that could be anywhere depending on which department was the last to have contact with the patient
 - Blue - activated at transplant but need to reflect changes that are made to the buff notes.
 
**NOTE:** This issue is closely related to data reliability and accuracy. Ultimately it could impact upon patient safety.
 
While on the waiting list the patient may be seen by the nephrologist. 

Letters may be generated and sent to external referring clinicians - these need to be part of the medical record. 

All correspondence by coordinators, such as email, need to be captured. 

**NOTE:** Currently all correspondence by coordinators by email or telephone is recorded in a word document. If this information is included within the EPR or other system, appropriate access control needs to be considered.
 
**SUG:** There is possibly a need for access control to be included on any system or subsystem that records correspondence between coordinators and others in relation to patients.
 
Patients can be suspended at any time. This may be because of holiday, illness, change in circumstances, etc.
 
**SUG:** There *should* be a mechanism that allows a patient to be suspended and a cause given. There *should* be a mechanism for reactivating patients. A reactivation plan *should* be recorded. Periodic reminders *should* be sent to appropriate team members to check if suspension is still appropriate. The reminder mechanisms *must* be configureable with respect to the frequency of reminders being sent.

### 9.6 Outputs

Outputs at this stage could include the mandatory periodic reporting to various bodies.

In addition there could be:

* Letters for annual reviews
* Email and other correspondence

## 10 Periodic checks

While the patient is on the waiting list, depending on the transplant that they are waiting for, it may be prudent to carry out periodic health checks to ascertain if there have been any significant changes. These changes may alter the suitability of the patient for transplant. This regular monitoring and contact with the patient will also allow the capturing of any changes to relevant information, including demographic and underlying health issues.

**QUE:** If the patient is referred from a satellite unit, will that unit be responsible for performing any tests and checks?

- Patient is reassessed annually by the Oxford team.

If so, how will the relevant data be returned for inclusion in the patient history?

- Annual checks for pancreas transplant are carried out by surgeons. For renal only transplants the patients are only checked when they are called for transplant.

## 11 Transplant

![Figure 7: Transplant](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_figure_7.svg)

### 11.1 Process

The living donor team have demographic information. 

**DATA:** paper based and word documents. Some is stored locally and some at remote centres.

If donor is remote the local living donor team should have all the information.

**TO CONFIRM:** Check with Sandra Dix

#### DONOR
For deceased donors the Electronic Organ Offering System (EOS) contains all pertinent data relating to the donors and organs.

It is not currently possible to obtain the information held in EOS automatically.

Induction plan.

#### ORGAN
Data needs to be recorded relating to the organ retrieval. This should include as a minimum:

- The surgeon and team involved
- The solution perfused with
- *HTA Form A* Document comes with the organ. This should be scanned and the image attached to the relevant patient record. In addition the information contained on the form should be incorporated in the patient record by manual data entry.

It is also important to ensure that the *HTA Form A* document number is recorded.

#### OPERATION

Back table information:

- Who performed the tasks. i.e. record the surgeon responsible
- Time
- Perfusion fluid and batch number

**SUG:** Template for back table data entry

Data from operation:

 - Time of operation
 - Surgeon
 - Other details?
 
 This is recorded in the transplant surgery form - recipient timings.
 
 **QUE:** Can a template be created in Surginet
 **SUG:** Template for operation data entry.
 
There should be a standardised form to fill out for the surgery. From this, data can be recorded in an electronic format. In addition, an OpNote can be generated. The data entry should follow a standardised template with a small number of free text areas to note any deviations from the standard procedure.

### 11.2 Inputs

Information related to the organ being transplanted along with information pertaining to the recipient.

### 11.3 Actors Involved

The following perform the transplant and support this stage:

- Surgeons and juniors
- Nurses
- Theatre staff
- Pharmacist

### 11.4 Information generated and stored

What information is gathered and stored as a result of this process?

#### NHSBT
At the time of transplant there are multiple forms to fill in.

- HTA Form B (one for each organ). NB: A lot of duplicated information.
- Pancreas record form (deceased pancreas form)
- Islets record form
- Small bowel/multi viscera
- Organ CIT and Perfusion Record and Kidney Record Form

Organ specific forms

- Repeated details from various sources:
  - Labs
  - Wards

Kidney record form - approximately 2 pages

- Repeated information such as 
  - Height
  - Weight
  - Virology status
  - Dialysis status
  
Deceased patient form

Outcome and anatomical issues
  
HTA Form B

- Organ perfusion
- TIMMS system recorded but not available link (theatre uses TIMMS to record organ perfusion fluid)
  
Information copied manually: A copy of forms is kept locally for inspection - originals sent off. Copies kept.
  
Recipient Coordinator has to fill forms and send to NHSBT (Transplant surgeon should complete).
  
Induction procedure used and medications
  
### 11.5 Outputs
  
The outputs that are generated by the transplant surgery include:

- An Operation Note
- HTA B Form (1 per organ transplanted)
  - Kidney Transplant record
  - Pancreas Transplant record   
- Transplant surgery form
- Crossmatch report
- Medication details
  

### 11.6 Notes

The operation note may be able to be automatically generated if the data necessary is entered using an appropriate system.

The *HTA Form B* needs to be submitted. A record needs to be kept tying the *HTA Form A* numbers to the *HTA Form B* numbers for reasons of traceability. The forms are submitted to NHSBT.

Electronic versions of the data along with a scanned copy of each form would aid traceability.

## 12 Post operative care

The patient is monitored post operatively to assess their progress.

![Figure 8: Post Operative Care](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_figure_8.svg)

### 12.1 Inputs

All of the information gathered by previous stages. Along with any medication information.

### 12.2 Actors involved

- Patients
- Nephrologist
- Surgeon
- Nursing staff

### 12.3 Information generated and stored

The results of regular measurements of blood pressure and temperature. Along with blood and urine results.

### 12.4 Outputs

Recommendation that a patient can be discharged.

## 13 Discharge

The patient is initially discharged with local follow-up. The local follow-up continues until the patient is discharged to the care of their referring unit. The referring unit then continues with planned follow-ups at regular intervals.

![Figure 9: Discharge](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_figure_9.svg)

### 13.1 Actors involved

- Patient
- Nephrologist
- Surgeon
- Nursing staff

### 13.2 Information generated and stored

Update patient record to indicate the patient has been discharged. In addition record the medication, if any, they are sent home with.

### 13.3 Outputs

A discharge summary letter that is sent to the patient's GP. (Does this also go to the referring clinician?)

## 14 Follow up

Initial follow-ups are carried out locally. The responsibility for follow-ups is then returned to the referring centre, which may of course be Oxford.

![Figure 10: Follow-up](../../_static/transplant_epr/transplant_pathway/transplant_pathways_diagrams_figure_10.svg)

### 14.1 Actors involved

- Patient
- Nephrologist

### 14.2 Information generated and stored

A standard set of information is required to enable the completion of NHSBT reporting forms. This is likely to include:

- Patient demographic details
- Blood pressure
- Height/Weight/BMI
- Blood tests
- Urine tests

### 14.3 Outputs

A regular report document for NHSBT is created at this stage.

## 15 Refusal

**QUE:** If a patient is considered unsuitable for whatever reason, do they have an opportunity to be re-evaluated at a later time? Or is the decision non-negotiable? Does a refusal generate a letter for the GP and referring clinician?

## 16 Other notes

Transplant hospital admission: Most of the data is in the EPR.

Discharge: There is a word template for the discharge letter stored on the shared renal drive.

Follow-up clinics: Letters from clinics should be stored.

Information relation to additional hospital admissions should be recorded where this information is available.

Should also record how successful the surgery was along with any other relevant clinical data.

## 17 Administration

Any administration system needs to be small and efficient. It cannot require the duplication of work such as manually re-typing information that has already been entered into the EPR system. 

The reasons for not duplicating effort are two fold: Firstly, the re-entry of information is inefficient and is usually non-productive work; Secondly, the probability of typographical errors being introduced increases each time information has to be re-keyed. 

It is envisaged that the vast majority of information required for administrative tasks associated with the patients interactions with the transplantation centre will be available through the EPR system. 

The EPR system currently contains information pertaining to outpatient activity including peripheral clinics. In addition, most ward-based activity is also recorded in the EPR. The ADT (Admission Discharge Transfer) is rolled out and will in due course provide realtime information for all wards. This is currently not the case as there can be delays in updating information. 

The EPR system will soon have ePrescribing rolled out. 

Numerous tests are currently ordered via the EPR. There are however a number of tests associated with the transplantation function that are ordered in a more traditional way.

**QUE:** How will the introduction of ePrescribing affect Proton? It is my understanding that Proton currently has the patient's medication as well as the induction medication used at the time of transplant. 

One current shortfall in the EPR system is the lack of digitised copies of correspondence from referral centres as well as electronic copies of reports sent out from the unit. It would be useful to have all relevant correspondence scanned and associated with the relevant patient record. This would allow timely access by clinicians or others responsible for various aspects of the care pathway.

There should be wider range of templates available to assist the generation of appropriate letters to be sent to patient and other parties with a legitimate care relationship with the patient.

Currently the department uses the ALDEN service which is a typing service which transcribes digital diction into letters. The service woks by sharing information, the dictations and resulting letters, via a secure site. Once finalised the letters associated with transplant are stored in Proton.

The Surginet module in the EPR should ideally record transplant information as well as any other procedures carried out.

**QUE:** What can be recorded in Surginet?

Proton currently stores data sent to commissioners pertaining to procedures carried out. There are different payment models for each of the transplants performed. Currently the kidney only transplant is only paid at the time of transplant. This payment is to cover all work up to and including the transplant. This model of payment is likely to change to one where payment is provided for each stage of the process separately.

This is where will be separate payments for:

- Assessment
- Work-up of donor
- Transplant episode
- Ongoing care

It therefore becomes necessary to accurately record each individual element.

The proton system is also responsible for other data feeds:

- The data needed by the renal registry
- The data used by the patient facing web application (some further investigation is needed on exactly how this currently works)

**QUE:** Is it possible for EPR to capture the relevant information for these two external uses as well as push the necessary data?

## 18 EPR Notes

It is possible to add adhoc attachments to a patient record in EPR. This is done by creating a digital version of the item to be added and placing it in an appropriate place. The item is 'scanned' in some way and is usually placed in a directory on the K drive. From there it is possible to attach the item to a 'Note'. This will allow the viewing of each item added to the patient record.

Dashboards can be added to the EPR, with complex pathway rules to allow a quick visual check as to the state of the required tasks related to the tests and other items necessary for completion before the patient moves to the next phase of the pathway.

It is also possible to capture paper forms, including those with the diagrams, in the EPR. This would allow the capturing of information in a consistent way and permit the instant sharing with multiple interested parties.

## 19 Findings and suggestions

The current transplant pathway utilises various mechanisms to store and manage patient information. These include EPR (Cerner Millennium), Proton, Excel spreadsheets, and Word documents.

A potential improvement would be to enable the scanning of documents into the patient record. An additional enhancement would be the ability to add notes relating to all communications relevant to the patients treatment. This would permit easy access to historical communications relating to the patient in a single place. It would also be more robust than the current procedure of adding notes to a word document. 

Another enhancement could be to make various forms that need filling in electronic. This could potentially include several consent forms that need to be signed. Currently there is a lot duplicated information on each of these forms. If the information was collected electronically it could permit the sharing of information between the various forms thus reducing the amount of duplicated effort. The forms could still be printed for signing and then scanned in using the mechanism that supports the first improvement. Alternatively, the forms could be signed electronically on a a tablet and only printed to give the patient a copy for their own records. 

In the area of assessment, it could be beneficial to other professionals involved in the care pathway to have access to the information collected in an electronic form. This would allow some automated processes to be used as an initial prescreening. One potential example is anaesthetic assessment. In this case, based on information collected, additional tests could be suggested before the patient even saw the consultant anaesthetist. To help facilitate this form of data sharing, it would be beneficial to make the assessment form electronic.

The Proton system is being retired and the functionality is being migrated to the EPR. The exact nature of the new system is still being assessed.

There are a number of spreadsheets that support a wide range of functionality. Some of this functionality is very specific to transplant. This may therefore necessitate the development of a standalone application that can communicate with the EPR for demographic and other standard information. This however will need careful consideration and detailed discussion with the EPR team. There is a already a facility to access demographic information. This is via the EPDS system which is already used by several systems across the multiple departments.

The production of letters is currently via the ALDEN system. These letters are then incorporated in the patient record with Proton. This functionality needs to be maintained after the migration of Proton to EPR.

The next stage of this process is to produce a definitive gap analysis between the features required for the transplant pathway and those available within EPR. It is also worth considering what is planned for EPR in the next 12 to 18 months as developing a standalone system that would be subsumed shortly after completion would not necessarily be the best use of time.

It would also be desirable to have the facility to automatically generate the relevant forms that need to be submitted to NHSBT and other bodies at various points in the patients journey. Additionally the data should be accessible within the boundaries of information governance and data protection legislation for use in research. 

Note: After several discussions with various people it is unlikely in the short to medium term that the EPR system will be able to support all of the requirements necessary to provide the functionality required by the transplant pathway. Although some feature are likely to be supported, inparticular those associated with the core functions of Proton, others are unlikely to be considered or do not fit with the EPR architectural model. It is worth noting that the current understanding is subject to revision as more information becomes available.