# Cerner Test/Probe Environment

There are a lot of unknowns, assumptions, and false assertions that need to be confirmed when working in the Cerner Millennium environment. The basic aim of the pages and scripts here is to poke from the inside as much of the tech as possible to provide clues as to what is possible, what is working, and what has changed.

## MPages
Looking specifically at the MPages technology and environment, my working understanding (currently ranked as very minimal and entirely anecdotal) is that the PowerChart desktop application uses an Internet Explorer instance (e.g. an iFrame within the app) to provide the rendering engine for HTML content. There is JS and CSS support (to an undefined degree, and with quirks) and we want to know as much about this from a pragmatic and definitive standpoint as possible (relying on what we're told or can read from training materials is insufficient at best and sophistry at worst).
    

### Background

Prior to this design pattern being enabled, the basic problem was one of a hideously complicated desktop application with almost no interlinking and everything tied into preset forms often optimised for the developer, not the clinician or user.

Users wanted to reduce the number of clicks needed to get at (and modify) data, and a concise and flexible way to to view content. In marketing terms, MPages were introduced to:

* Promote efficiency and productivity  *(wait, this wasn't a concern before? - ed)*
* Support specialty workflows  *(one size does not fit all - ed)*
* Improve clinician's satisfaction and increase adoption/compliance *(they noticed that poor user experience leads humans to find the path of least resistance, often against desired behaviour - ed)*
* Provide clinical decision support to improve quality of care *(i.e. if we present relevant information to the clinician they can make more informed decisions - ed)*

Thus MPages are declared as a technology platform consisting of: Web tools for the UI (HTML, CSS, Javascript) + Cerner technologies to acquire data (CCL and Services)

The aim was to introduce some positive attributes to the platform, namely:

* **Consistency** - One Cerner UI standard across all solutions *(unfortunately this has clearly not occurred as the suite of Cerner apps still have varying iconography and usage patterns, and even within the MPages themselves, there's variations in layout that look to be lacking a style guide - something that has yet to be located!)*
* **Configurability** - Component library to meet the needs of all role / venue / speciality workflow needs *(this has yet to be fully assessed, but there is a hint at a range of UI widgets that Cerner call components)*
* **Contextualisation** - Which components appear and contents of the components flex based on user and patient attributes
* **Personalisable** - User able to rearrange and add/remove to meet their personal preferences
* **Extensible** - Clients may develop and plug-in custom components to meet unique needs *(this is indeed the key need here)*
* **Shareable** - When developed under standards based approach - SMART on FHIR - shareable across platforms *(noble, but which standards, defined where, and examples of which... are still to be ascertained)* 

Metaphors used in the framework for MPages:

* **Worklists** - e.g. Ambulatory Organiser, Surgery Organiser, Provider Handoff, Clinical Leader Worklist
* **Workflow Views** - e.g. Multiple workflows based on Role/Venue/Condition, Body Systems View
* **Summary Views** - e.g. Multiple summaries based on Role/Venue/Condition
* **Dashboards** - e.g. ED Dashboard, Perioperative Dashboard

### Mechanics

DRAFT from slides...

Bedrock `bedrock.exe`

* mPages -> View Builder:
  * Name the framework (see layout types)
  * Add the components needed
  * Save
* mPages -> Setup:
  * Topic is the name of your Framework
  * Setup each Column

Preferences `prefmaint.exe`

* Select *Applicable Application*
* Select *Applicable Position*
* Powerchart -> Organizer -> Add Discern Report
* `VIEW_CAPTION` -> Front end Framework Name
* `REPORT_NAME` -> `mp_unified_org_driver`
* `REPORT_PARAM` -> `"MINE",$USR_PERSONID$,$USR_PositionCd$,"$APP_AppName$","",“VB_<VIEWPOINT NAME>"`

Servers

* 535 - MPages
* 548 - ClinicalLeaderDashboard
* `SCPView.exe`
  * Server -entry [xxx] -> View Server State
  * Start [xxx] -> Start Server
  * Cycle -entry [xxx] -> Cycle Server
* **NB: Cycle Servers every time a view is changed in Bedrock**

Columns

* Configuration Pages: https://wiki.ucern.com/pages/viewpage.action?spaceKey=reference&title=Configure+MPages+Worklist+Columns
* Configuration Types:  * CKI Mapped `ConceptMap.exe`
  * Code Sets
  * Generic Clinical Event
  * Generic OrdersDocuments to reference:
* [MPage Component Standard 1.1](https://connect.ucern.com/docs/DOC-238855) (pdf) - 19/12/12
* [MPages Technical Development](https://connect.ucern.com/groups/mpages-technical-development/content?filterID=contentstatus%5Bpublished%5D~objecttype~objecttype%5Bdocument%5D) (uCern Wiki Group)