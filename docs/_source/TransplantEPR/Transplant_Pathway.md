# Transplant Pathway

Original version by Mark Slaymaker, 10/07/2014

# Overview

This report is intended to be a starting point to facilitate a discussion about the requirements of the transplant patient pathway.  It aims to capture the various stages that a patient traverses.  It is intended that a patient focussed methodology be followed.  It is further hoped that, by the introduction of an efficient pathway support system, we can improve the patient experience by ensuring all the necessary information is available to the relevant team member at the appropriate time.

Once we have a full understanding of the pathway we can then conduct a gap analysis between what is required and the current features of the EPR system.  Once the gap analysis is completed we will be in a position ot develop a detailed requirements documetn stating what system needs to be developed.

It is the goal of this endeavour to provide a system to support the patient pathway within transplantation.

An orthogonal ambition is to provide high quality research data.  In the initial stages the research data will be made available in the form of a number of standardised queries, which can be parameterised.  It is anticipated that initially these queries will only produce aggregated results to maintain patient confidentiality.

The aim is to allow clinicians, managers and reserchers access to information pertaining to the performance of the transplant programme and allow identification of any trends that could warrant futher action.  We will also give consideration to how additional data collection could be integrated for additional reserch purposes.  This may need additional protocols that relate to the additional processes involved in obtaining relevant consent to tpermit the collection of supplementary information.

Throughout this document the term 'referring clinician' will be used to cover any clinician that could refer a patient including but not limited to Nephrologists, Diabetologists and GPs.

1.1  Data Needs

The data collected as a patient traverses the pathway will be used to support several functions by fulfilling the needs of various customers.  The primary uses can be classified as:  Clinical, Managerial, Madatory reporting, Evaluation and Research.  The following give a brief summary of the key data consumers and the types of data that they require.

1.1.1 Clinical

There is a minimum set of data that needs to be collected for clinical reasons.  This data is necessary to permit clinical staff to perform their function effectively and maintain patient safety.  The exact makeup of the required data will depend on the clinical specialty concerned.  Although, there will be a core set of data that will usually be needed alonside a more extensive discipline specific data set.

1.1.2. Managerial

The managerial data collection is necessary to maintain the smooth running of the department.  It is important to collect data that allows the rapid identification of potential problem areas.

1.1.3 Mandatory Reporting

There is a requirement to provide data to certain external bodies such as the Renal Registry and NHSBT.  This reporting is mandatory and the informaiton required is specified by these bodies.  It is therefore essential that any information necessary to comply with these requirements is collected in an appropriate way.

1.1.4 Evaluation/Research

This section relates to the data collected over and above that needed for other purposes that will permit the critical evaluation of the performance of the department.  In addition this data can also form a core of research data that could be used to support studies if the appropriate ethical permission and consents are obtained.

1.2 Scope

The kidney transplant pathway is complex and there are several potential routes that a patient could take.  the pathway involves members of a multidiscicplinary team who provide patient care and support at different stages.  It is therefore important to clearly articulate the scope of this document and to highlight the elements that we consider to be within the pathway.

It is important to remember that the patient is always central to each of the stages that comprise the pathway.

It is understood that the scope is purely a boundary to the areas we provide detailed consideration to. However, as information has to flow across the scope boundary it is therefore vital that appropriate protocols and information flows are well defined to ensure efficient communication across the boundary.

It has been decided that for the purpose of documenting the renal tranplant pathway we will include all interactions from an initial referral to a transplant surgeon throuhg to the discharge of a patient into the care of their local referrer.  There may be a need for patienets to re-enter the pathway for a number of reasons.  Additionally is is also important to record as part of the pathway information relating to the donated organ.  It is also possible that some patients are unsuitable for transplant and this information also requires recording.

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

It is also vital that the organisation monitors its own performance.  This monitoring will allow the organistion to react to any negative changes to its own statistics.  Additionally the use of monitoring allows a rigourous assessment of the effect of any changes to procedures that occur.

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

2.1 Data registry and metadata

To facilitate the reuse of data for research purposes it is necessary to clearly define the data being captured.  This includes providing a definition of each item, how the data is collected, when data is enterd, the acceptable units for the measurement and any restrictions to the acceptable range.  For reasons of data provenance it is essential that informatio is stored that details the time that the data was captured along with the person entering the data.  Any changes also need to be accurately recorded to ensure that any modifications are easily identified to enable verification.  In addition ther may be a need to record temporal informatio for procedures and processses that have a clearly identifiable staring and finishing time.
The most important this is to ensure that we capture a complete set of dat items that togerher provide a coherent piece of information related to an event.  Each of these infomration items should be signed, in some way, to help provide a degree of provenance.  In suppor of this all data should be recorded contemporaneously with respect to the events to which it relates.

# 3 Pathway Summary

The contents of this section represent our current understanding of the pathway.  Figure 1 provides an abstract summary of the pathway.  The subsequent sections will provide a more detailed description of each process.  As far as possible the data required to support each process will be indentified along with the source of the data.  our current understanding is that a patient follows one of several possible pathways from referral to the eventual outcome.

The simplified pathways can be summarised as:

1. Referral
2. Outpatient appointment which on the initial appointment normally includes work up.
(a) Refusal is a potential outcome of the outpatient appointment
(b) Recommendation to consider for listing
3. Listing discussion
(a) Refusal
(b) Further investigation
(c) Accepted onto the waiting list
4. Activation
(a) Tissue typing
5. Waiting List
6. Transplant
(a) Tissue typing - confirm compatibility
(b) Donor information
(c) Organ
    (i) Biopsy
(d) anaesthetic assessment
(e) Operation (Post admission tests)
7. Post operation
8. Discharge
9. Follow-up at outpatients
(a) Initiallyfollow up is local
(b) Finally patient is discharged to their referring unit for further followup
10 Events
(a) Outpatient
(b) Telephone contact
(c) Admission

There are a number of outcomes possible at various stages of the pathway.  The patient can proceed to the next step, require further investigations or be turned down for transplant.  There is a potential for a number of individuals to be involved at each stage in the pathway, who each have a responsibility for ensureing different portions of the information required is collected.  The overall target is to ensure that sufficient information is available to allow it to be accessed in an appropriate manner to reach a decision.

Insert Figure 1 

3.1 18 Week referral to treatment pathway

There is a maximum time of 18 weeks between the referral being recorded and a final decision about treatment, either refusal or entry onto the waiting list. The general rule is that ther should not be more thatn 18 weeks betwen referral and first treatment.  In the cae of transplant, first treatment is consered to be acceptance onto the waiting list or being deemed unsuitable for transplant.  An illustration of the timeline for the case of being accepted onto the waiting list is outlined in Figure 2.  The 18 weeks may nto be contigiuous as there are various reasons that can cause the clock to be temporarily stopped.  If the clock has been stopped it may subsequently be restarted if approprate events occur at a future time.  This is discussed more fully in Section 5 below.

NOTE:  The 18 week pathway is currently managed via an Excel spreadsheet.  It should also be noted that there is a suggested maximum of 6 weeks between referral and the first outpatient appointment.

Insert Figure 2

# 4 Satellite organisations

There are a number of satellite organisations that will interact with the patient pathway, who may have different Information Technology (IT) solutions.  To prevent this being a problem it will be necessary to have clearly defined protocols with respect to the information being passed between the organisations.  These protocols will have to define minimum acceptable data sets for each possible interaction.  The definitions will have to include field names along with acceptable pseudonyms, the type of data being recorded and if applicable a range for acceptable values including any relevant units.  If electronic information interchange can be agreed then it will minimise the amount of human intervention necessary to incorporate data from satellite sites.

# 5 Other general comments

At various points in the patient pathway numerous forms are currently filled in. Further details about the content of thse forms is to be provided at teh relevant places within this document.  A copy of each forms needs to be obtained and annotated to indicate the minimum amount of information that has to be collected.  This will help to identify the source of the data required at each stage of the pathway as well as the data that is supplied by each of the stages.

There are a number of coordinators who are responsible for dealing with referrals for all the transplant programmes;p
- Kidney
- Kidney and pancreas
- Pancreas
- Islet cells
- Kidney and islet cells
- Small bowel

Although there is a separate living donor team, they interface closely with the deceased donor kidney team.

The RTC (Renal Transplant Coordinators) in addtion to other roles and responsibilities perform the following tasks:
- Waiting list management
- Call in patients

Ther is currently a separate team that performs the function of post transplant follow up.

There ia a potential for patients to seitch between lists for various reasons, including 
- Failed transplants which can potentially result in teh patient being relisted 
- Second trasplant - this may be a different organ (e.g. pancreas transplant after a kidney transplant)
- Patient no longer fit for their originally planned transplantation such as a SPK but are still suitable for lesser option of renal transplant only.

NHSBT - currently submissions to hte NHSBT from the transplant team are via manually completed paper forms which are completed after gathering data from multiple sources.  

Some forms can be automatically generated by Proton.  As teh Proton fuctionality is migrated to the EPR system it is hoped that these features can be maintained and additional forms added.  This is however dependent on the priorities set during the migration from Proton to EPR.

NOTE:  It is the intention of the project team to concentrate on kidney onl trasnplantation in teh first instance.  The lessons learned from this work will help inform the development of approprate solutions for other transplant treatments.

# 6 Referral

STM:  Referral letters MUST be processed in accordance with any OUH NHS Trust SOP.  The receipt of the referral letter is the start of the 18 week referral to treatment cloack.  On receipt of the referral letter it should be stamped with a date.  This date indicates the start of the 18 week referral to treatment pathway which is illustrated in Figure 2.

The referral is the initial contact with the unit and is usually in the form of a physical letter.  The quality of the information supplied is variable.  It is however possible for referrals to be received in alternate ways including but not limited to:
- Electronic transfer
- Email
- Phone conversations
- Self referral

The remainder of this section identifies the mechanisms involved in referral and the information flows that are expected to occur.

Insert Figure 3

6.1 Standard operating procedures

The trusts standard procedure for logging referrals should be followed.  The patient should be entered into the EPR system along with all of the information available at this point in time.

6.2 Inputs

The referral, usually a letter is the only input available at this time.  The referral should include at least the patients name, contact details and reason for referral.  It would be useful if additional information pertaining to medical history and medications could be included.

6.2.1 Where do referrals come from?

Typically a referral to a transplant surgeon is generated by a reffering clinician.  The referring clinician may be based locally in Oxford, in one of the satellite centres closely associated with Oxford or potentially from further afield.  In some circumstances it is possible to get self referrals.  It is also possible to get referrals from other centres asking for a second opinion.

6.2.2 What information is essential for a valid referral?

The more details provided in teh referral the better.  It is essential to have contact details and some details about the referral.  In general the following would be a good starting point
- Demographic information.
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

It has been suggested that there could be an improvement in the quality of information provided at the time of referral if a proforma template was provided to referring clinicians.  This could be tailored to the type of referral.  The initial sections should contain suitable space to allow the capture of essential information.  Additional sections could ask for the information that would be 'nice to have'.

6.3 Queries required

There may be a need to specify a report that provides information about the number of referrals that have been received.  It would also be of benefit for the management of the department to know the average time from referral to treatment along with any outliers that exceed the 18 week time limit.  Further reports detailing the number of DNA or withdrawals may also be useful for the management of the department.

6.4 Actors involved

The following are generall involved in the referral process:
- patient
- Referring clinician
- Surgeon
- Receiver and processor of the referral?
    Secretaries.  Consultant and ANP receive and agree assessment to proceed.  Then calls admin to make and send an appointment.
    Admin (managed by office manager)
    
6.5 Processes involved

An outpatients appointment is gererated after the basic information contained within the referral letter is entered onto the EPR system.  It is required that patients are seen within 6 weeks of the receipt of the referral letter.

It is possible that the patient is referred onto a different speciality.

6.6 Information generated and stored

A summary of the information gathered at referral is presented in Table 1.  The majority of the information generated by this phase of the pathway is stored in the EPR.

Insert Table 1.

6.7 Outputs

There are a number of potential outcomes from a referral:
- Outpatient appointment
- Request for additional information from the referring clinician
- A refusal to proceed

The primary goal of this phase of the pathway is a letter inviting the patient to attend an outpatient appointment.  In addition the basic demographic information should have been entered into the EPR.  This information will need to be validated at teh time the patient attends the outpatient appointment.  A refusal can occur at any stage of the pathway if the consultant feels that it is indicated.  Also, the patient can change their mind and decline a transplant at any point.

6.8 Other comments

SUG: It would improve the process if all referrals contained the essential information pertaining to the reason for referral.  Additional benefit may also be obtained if certain standard clinical investigations could be either scheduled or completed around the time of referral.  e.g. cardiac mps?

STM: The referral letter should be digitised and attached to the patient record.  This could make up the initial entry on the timeline.  If a local system is developed the information from the EPR needs to be visible to local users without rekeying.  It is important that there is no additional work created by the requirement to rekey data.

Ideally all the required information associated with the referral would be supplied in an electronic format by the referring clinician.  This would permit the incorporation of the information in the patient record without the need to rekey.  In addition to the potential time saving, the removal of the manual rekeying reduces the chance of typographic errors being introduced.  The minimum information that should be included in a referral is the demographic information.  A reasonable minimum referral should include: name, address, contact details, DoB, GP and details of the reason for the referral.  It is also imperative that the date of receipt of the referral is recorded to ensure that the first offer of an appointment is within the target time scales.

# 7 Outpatient appointment

The outpatient appointment is the initial contact with the patient.  During this appointment a transplant assessment form is completed alongside other tests to gather the necessary information to permit a decision to be made about suitability for transplant.  The patient arrives for assessment and the demographic information already in the system is validated.  If tests have been performed previously then some of the informatio required might already be available.

Insert Figure 4

7.1 Assessment process

The first appointment should occur within 6 weeks of receiving the referral.  At the outpatient appointment a consultant and nurse perform a transplant assessment using a standard form.  This form is designed to capture the information necessary to enable a listing meeting to make an appropriate decision.  This form does include diagrams that are annotated when the clinical examination is conducted.

It would be beneficial to have an electronic version of the form that recorded the information directly into a suitable information system.  In addition an anaesthetic assessment section shoudl be completed as part of the outpatient appointment.  This should be forwarded to the anaesthetist in advance to enable them to request additional tests if that is appropriate.

The assessment usually include:
- Blood tests, with the results being available from the EPR
- X-rays
- Tissue typing (H&I lab)
- ECG

Additional tests can include:
- Chest - CXR, PFTs, CPEX
- Cardiology - heart MPS, coronary angio stent cardiac surgery
- Myocardial perfusion scans
- Other - dopplers, duplex, CT

In addition input may be required from 
- Pharmacist
- Dietician
- Psychologist

All of the data collected is used to make an assessment of the suitability of the patient for transplant.  Additional tests can be ordered at different times.  The results of tests take variable amounts of time to become available.  It is therefore essential that any system notifies an appropriate person when all of the data becomes available, or if a particular timeout has been exceeded.

During the assessment phase, and subsequent phases, it is necessary to get positive confirmation from the patient of the current medication as any information recorded in the system may be out of date.

It is also desireable to obtain positivie confirmatio of allergies at the same time.  Blood tests may be done on the day of the assessment or at subsequent appointments possibly at the patient's local centre.  It is unlikely that these results will be available immediately.  Currently tests for out patients are ordered on paper but this should become electronic ordering as the EPR rollout continues.

In addition to the completion of the assessment form the patient is asked to sign several consent forms:
- DPA related to permit the sending of information to NHSBT
- Consent for virology test - in particular HIV
- Consent for a photograph to be taken and added to work up documents
- Consent to go on the waiting list (is this currently done?)

The consent forms are currently filled in by hand, with some of the information duplicated on each of the forms.  One of the forms goes to NHSBT the others are stored locally.  It is possible for forms to be mislayed.  A method of reducing the duplication of information would be beneficial.  It would also be beneficial to have an electronic version of the consent forms associated with the patient record.

It is also necessary to take account of potential exceptions to the usual progress through the transplant pathway.  For instance special measures may need to be taken to prevent discrimination against patients from particular groups or suffering from particular ailments, such as:

- Jehovah's Witnesses
- Allergies
- Other issues

7.2 Inputs

For an outpatient appointment to occur several things need to be in place;
- A record of the patient on the system that needs to be verified
- The patients needs to attend
- The patient needs to bring any additional informatio requested at the time the appointment was sent out.

However, the primary input to the outpatient appointment is the referral letter and any associated patient history it includes.  It is therefore imperative that the referral letter is available either physically or electronically.

7.3 Actor involved

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


7.4 Processes involved

Each of the individual tests orgered could be considered a sub-process.  They wil leach have their own SOPs that govern how the patient is evaluated and the results returned.

7.5 Information generated and stored

The data is potentially captured in a number of ways:
EPR will capture demographic data as well as that pertaining to lab results.
PACS will contain radiographic information
The H&I lab system will contain additional information not available in EPR.

ECG information is captured potentially this is only in paper format at the moment.

proton currently captures any information related to the pharmacist although this is likely to change in the near future as teh ePrescribing module of the EPR is rolled out.

In addition there is a form to be filled in during the assessment process.  This is currently a paper form.  This could be transplated into a form on EPR to allow the electronic capture of data.

7.6  General data

- Demographics
 - NHS number
 - Hospital number 
 - Name
 - DoB
 - Address
 - Contact numbers
 - Age
 - Gender
 - Ethinicity
 - Employment
 - NOK
 - GP details

-Referral details
 - Date
 - Clinic
 - Tx Surgeon
 - Tx Coordinator
 - Local coordinator
 - Organs required
 - Clock start
 - Clock stop
 - Reason
 - Ref consultant
 - Contact details
 - Dialysis unit

- Transport plan
 - Own transport
 - Hospital transport
 - Plan
 - Pre-authorisation code
 - Back up
 
- Is there a LD Kidney option
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

7.7 Consent Forms

7.7.1  Sample Consent Form

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
 
 
 7.7.2 Clinical Photography
 
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
 
 7.7.3 Recipient consent form
 
 Consent
  - Understand voluntary consent for data use by NHSBT
    - Initial
  - All data shared as necessary
   - Initial
  - Signature of paient
  - Date
  - Witness signature
  - Date
  - Representative signature (if necessary)
  - Date
  - Name of representative
  
 Refusal of consent
  - Understan refusal may jeopardise chances
    - Initial
  - Refuse consent for certain items
    - Initial
    - Specify items
  - Refuse consent for all information
    - Initia
  - Signature of patient
  - Date
  - Witness signature
  - Date
  - Representative signature
  - Date
  - Name of representative
  
  7.7.4 Outpatient outcome form
  
   - Consultant
   - Clinic prep
   - Reception
      - Patient type (NHS/Private/Overseas)
   - Clinical staff
      - Patient on 18 week pathway
   - Outcome of attendance
   
  7.8 Outputs
The potential results of the OPA are:
 - The patient is put forward to a listing meeting (considered an appropriate candidate).
 - The patient is not considered to be a suitable candidate and a refusal is granted.
 
 The ultimate output from this section is a letter, wither indicating that the patietn is being forwrded to the listing meeting or that they are un unsuitable candidate for transplantation.
 
 Letters are usually generated using the ALDEN system.
  - The letter is dictated or typed
  - Dictated letters are sent for transcription
  - The content is checked by the author
  - A secretary performs final formatting tasks
  - The letter is stored in the renal directory (R:) as well as being added to Proton
  
  7.9 Notes
  
  Some procedures exit in various states.
  
  - Transplant immunology - SOPs
  - Protocols on intranet for all transplant programmes reviewed
  - Renal - Transplant intranet - link to other OUH documetns
  - Renal transplant RTC SOP (Renal directorate server)
  
It is not clear if the EPR system captures all of the information required for the assessmetn.  If the EPR system does not collect all of the necessary information it is probable that an additional system will need to be developed that will operate in conjunction with the EPR system.

SUG: A system should allow the storage of the letter as part of teh overall patietn record.  In addition it should also form part of the patietns timeline.  Note:  Apparently this is being incorporated into the EPR system.

SUG:  A template for a letter could be provided that is automatically populated with the relevant test result and other asessment findings.  The surgeon could then add any customisations that were appropriate for the individual patient.

Note:  Islet and bowel cases do not always fit into the 18 week time frame as the assessments can be complex.


# 8 Listing Meeting

The final decision about the suitability of a candidate patietn for transplant is made at the listing meeting.  The outcome of the meeting dictates the next stage for the patient in the pathway.

The meeting is a multi-professional meeting.

SUG:  It is importanat to identify any items of information that should be circulated to all attendees prior to the meeting being convened.  For each item of information that is required the format and acceptable content should be defined.  It is easier to circulate information if it is in an electronic form.

8.1  Inputs
The inputs to this process are the outputs of the outpatient appointment phase and teh initial referral letter.  This includes the letter detailing the recommendation as the result of a cardiology MDT meeting, test results and any other information available at the time of the meeting.

The gereral information to complete the NHSBT form is currently obtained from several sources including:

 - Word documents containing patient demographics
 - Lab reports from EPR
 - Dialysis data from
  - Assessment
  - Proton
  - Referral letter
  
Also recorded:

  - Height
  - Weight - BMI
  - QoL and hypoglycaemia awareness from a paper questionnaire and clinical assessment - only in word document
  
8.2 Actors involved

The following are usually involved in the listing meeting

- Nephrologist
- Surgeon
- Anaesthetist
- Coordinator
- Tissue typing (H&I lab)

8.3 Procedure

There should be a record of who attended the meeting.  There should be a brief record of discussions that occurred.  This should be attached to the patients timeline.  A record of the consensus view should be kept along with any reservations raised.  Ther should be a record of the reasons for declining a patient.

If the patient is deemed suitable for listing then the NHSBT pre registration data needs to be collected and the following done:

- Complete the form so the patient is registerd with NHSBT
- Send the form to the H&I lab for tissue type information to be added prior to being sent off
- Paper form is faxed to NHSBT at the time of registration

We are currently focusing on the requirements for renal transplant but it is worth noting that ther are some differences between each programme as to the criteria to go on the waiting list.

8.4 Information generated and stored

The following data artefacts should be generated by the listing meeting:

- Listing MDT Summary and Transplant Plan
  - Date
  - Present
  - Issues Discussed/concerns raised
  - Consultant Sign off
- Letter to patient
- Letter to GP/referring clinician
- NHSBT form

Data to register the patient on the waiting list including:

- Blood group
- Tissue type details

8.5 Outputs

The utimate output of the meeting is a letter to the patient and GP (?) indicating whether or not the patient has been accepted onto the waiting list.  In addition if the patient is recommended for listing then the appropriate NHSBT forms should be completed and sent off.

8.6 Notes

SUG:  Automated letter production

A standard letter template should be created appropriate to each specialty.  The letter should be automatically populated with any information available from the system (EPR) along with entered information.  Information entered should be via a template captured via an input form appropriate to the specialty.  A combination of dropdowns and text areas should be used to permit the entry of information that completes standardised prose.  Enterd information should also be stored to facilitate searching for items of interst at a later point in time.

The letter will either be requesting the addition of the patient to a waiting list or the refusal of the patient.

  
 

