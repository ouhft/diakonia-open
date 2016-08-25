# Notes

Assorted findings that need further processing to make sense of them

## Documentation
There needs to be a lot more, and better structured. So one thing to get right from the start is Requirements Engineering (Gathering, Tracking, & Specification)

### ReqEng
* [http://stackoverflow.com/questions/171653/examples-of-requirement-documents]()
* [http://techwhirl.com/writing-software-requirements-specifications/]()
* [https://en.wikipedia.org/wiki/Software_requirements_specification]()

## UI

Consider shift of methodolgy as shown by the OPAL project, using Angluar JS as the Client side technology, with a Django application service backing it (and possibly a direct link to FhirBase?)

* [https://angular.io/docs/ts/latest/guide/architecture.html]()
* [http://www.bluebuttonjs.com]() -- BlueButton.js helps developers parse and generate complex health data formats like C-CDA with ease, so you can empower patients with access to their health records.
* [https://github.com/openhealthcare/opal]() -- Django+Angular OSS health system
	* With Plugins (though none for Transplant): [http://opal.openhealthcare.org.uk/docs/guides/plugins_list/]()
	* Documentation: [http://opal.openhealthcare.org.uk/docs/]()


## Data Structures

There are many :-/

### NHS

* NHS HSCIC has a data dictionary, with contents online at: [http://www.datadictionary.nhs.uk/data_dictionary/diagrams/diagrams/person_diagram_fr.asp?shownav=1]()
* [https://data.england.nhs.uk]() -- Find and explore the data used by NHS England to conduct its core business
* [http://systems.digital.nhs.uk/ddc]() -- Are behind the NHS Spine
* [https://code4health.org]() -- An incubator group from NHS England
* There are many references to strategy and ongoing work via the NHS Digital Technology pages - [https://www.england.nhs.uk/digitaltechnology/]()
* Various data resources can be found on the TRUD (the Technology Reference data Update Distribution site) - [https://isd.hscic.gov.uk/trud3/user/guest/group/0/home]()
	* The Interoperability Toolkit - [https://isd.hscic.gov.uk/trud3/user/guest/group/41/pack/30]()
* [http://data.developer.nhs.uk/fhir/eRS/Chapter.1.About/index.html]() -- FHIR Implementation Guide for the NHS e-Referral Service
* [http://www.oxonhealthcaretransformation.nhs.uk/who-is-involved/transformation-board-meeting-papers/transformation-board-2016-04-26/73-for-info-oxfordshire-digital-platform/file]() -- Oxfordshire plans from March
	* [http://www.oxonhealthcaretransformation.nhs.uk/who-is-involved/transformation-board-meeting-papers/]() -- For a full index of the Transformation Board's meetings
* [http://www.ouh.nhs.uk/about/trust-board/2016/january/documents/TB2016.15-epr-plans-and-governance.pdf]() -- Trust strategy talks of a new Health Informatics Committee to be created. Need to investigate.
	* Full index at [http://www.ouh.nhs.uk/about/trust-board/meetings-and-papers.aspx]()
* South, Central, and West, Commisioning Support Unit (Andrew Fenton, previously of this trust), writing about how they are supporting Digital Health changes -- [https://www.scwcsu.nhs.uk/news/insights-issue-6-june-2016-commissioning-show-special/how-digital-health-transformation-is-taking-shape]()
	* [Digital Transformation Services](https://www.scwcsu.nhs.uk/solutions/digital-transformation) @ SCW:CSU 


### FHIR(base)

A likely favourite as their data model seems more flexible and saner (see person -> names as an example compared to NHS)

* [http://fhirbase.github.io]() -- Docs
* [https://github.com/fhirbase]() -- Code repositories
* [https://github.com/fhirbase/fhirbase-plv8]() -- Repository for the Postgres Implementation
* [http://fhirbase.github.io/demo/index.html]() -- Demo site with query window


* [http://hl7.org/implement/standards/fhir/documentation.html]() -- Fhir documentation
* [http://hl7.org/implement/standards/fhir/datatypes.html]() -- Fhir datatypes
* [http://hl7.org/implement/standards/fhir/resourcelist.html]() -- Fhir resource types
* [http://hl7.org/implement/standards/fhir/resourceguide.html]() -- HL7 standards
* [http://hl7.org/implement/standards/fhir/implementation.html]() -- Fhir implementation checklist


* Slideshows:
	* [http://www.slideshare.net/ewoutkramer/fhir-tutorial-morning]()
	* [http://www.slideshare.net/GrahameGrieve/introduction-to-fhir]()
	* [http://www.slideshare.net/DevDays2014/fhir-architecture-overview-for-nonprogrammers-ren-spronk]()
	* [http://www.slideshare.net/ewoutkramer/fhir-profiling-tutorial]()
	* [http://www.slideshare.net/ewoutkramer/hl7-fhir-for-developers]()
	
* Extensions are a key concept to understand, and some work will likely be needed to be done to create relevant ones for Transplantation
	* [https://fhirblog.com/2014/03/06/extensions-are-not-second-class-fhir-citizens/]()
	* See also the link to the NHS eRS which uses extensions 

* [http://www.hl7.org.uk/doc_store/NHS/HL7%20Integration%20Options%20for%20Trusts.pdf]() -- HL7 talks about integration strategies, including the need for roadmaps (and steps to create)

* [http://www.ehealthnews.eu/emis/4679-emis-health-implements-open-standards-for-interoperability]() -- EMIS are using Fhirbase with Snomed and NHS DD

* [https://www.renalreg.org/wp-content/uploads/2014/10/The-UK-Renal-Data-Collaboration-UKRDC-and-the-Data-Model-by-Dr-Keith-Simpson-and-Peter-Nicklin.pdf]() - Project to create a UK Renal Registry that communicates with partners via FHIR
	* [https://www.renalreg.org/wp-content/uploads/2014/09/UK_Renal_Data_Collaboration_White_Paper_1.1.pdf]()
	* [https://www.renalreg.org/data/]() - Has a UK Renal Registry Dataset definition

* [http://stackoverflow.com/questions/tagged/hl7-fhir]() -- Stackoverflow has 260 Q&As so far

* [https://twitter.com/FHIRnews]()

* From GNU Health, there's a python reference library for Fhir: [https://pypi.python.org/pypi/fhir]()

* Someone is having a go at merging Django with other techs to get a Fhir stack: [https://github.com/videntity/django-fhir]()

* Lots of FHIR related postings at [https://fhirblog.com]()
* As well as at: [https://thefhirplace.com]()
	* [https://thefhirplace.com/2016/08/08/create-my-first-fhir-implementation-guide-using-simplifier/]() 

* Or from SMARTonFHIR: [https://github.com/smart-on-fhir/client-py]()
	* [https://fhirblog.com/2016/07/08/what-is-smart-and-why-should-you-care/#more-158596]()
	* SMART on FHIR Python Client Docs - [http://docs.smarthealthit.org/client-py/index.html]()

### OpenEHR

Scotland went a different way earlier on and supported the Open EHR initiative, something started at UCL, but now international. 

* [http://www.openehr.org/home]()

### SNOMED CT
The NHS National Information Board (NIB) has specified that SNOMED CT is to be used as the single terminology in all care settings in England, with work to be started by all before Dec 2016, and all systems be implemented before 2020.

* [https://www.networks.nhs.uk/nhs-networks/snomed-ct/snomed-ct-webinars/why-snomed-ct]()
* [http://systems.digital.nhs.uk/data/uktc/snomed]()
* Look for the UK SNOMED CT! - [https://isd.hscic.gov.uk/trud3/user/guest/group/0/pack/26]()
* Python has a module for SNOMED - [https://pypi.python.org/pypi/PyMedTermino]()
	* Docs at [http://pythonhosted.org/PyMedTermino/]()
* Mapping is not without its issues: [http://www.safescript.com/tmt_error_analysis.html]()


## Infrastructure

At somepoint, the reality is that developed services will need to operate somewhere. Given the low value and high cost of IM&T solutions, external alternatives to consider include:

* Searching for "g cloud nhs accredited n3 hosting":
* [http://www.redcentricplc.com/services/infrastructure/hosting-colocation/n3-hosting/]()
* [https://www.4d-dc.com/cloud]()
* [http://ukcloud.com]() -- The new name for Skyscape
	* Supposedly behind Genomics England hosting: [http://ukcloud.com/wp-content/uploads/2016/07/UKCloud_CaseStudy_RGB_Digital_Genomics.pdf]()
	* [https://www.digitalmarketplace.service.gov.uk/g-cloud/services/7456481668431278]()
	* [http://ukcloud.com/what-we-do/platform-as-a-service/digital-application-platform]()

**Security** is an important topic, and covers all aspects of all projects...

* [http://docs.smarthealthit.org/authorization/best-practices/]()