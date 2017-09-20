The Citrix presented virtual desktops we use are for Windows 2008 Server (Service Pack 2?). This platform is currently in Extended Microsoft Support until Jan 14th 2020 (https://support.microsoft.com/en-us/lifecycle/search/1163). There are currently two newer major releases of the Windows Server platform since this (2012 & 2016)

Cerner has a [GitHub account](https://github.com/cerner) with a range of projects on it! Including details on for [FHIR-on-Cerner](https://github.com/cerner/fhir.cerner.com). [Terra related code](https://github.com/cerner/terra-core) is here, which leads to...

**[Terra UI](http://terra-ui.herokuapp.com/home)**
> Terra UI offers a set of configurable React components designed to help build scalable and modular healthcare focused applications. These components follow Cerner’s Design Standard Guidelines and are well-maintained and tested. The UI framework easily integrates with webpack-based workflows and was created to solve real-world issues in projects we work on day to day.

Cerner appears to be favouring [React.JS](https://facebook.github.io/react/) for some web development, and recommends being familiar with this before looking into Terra

Cerner's [SMART on FHIR tutorial](http://engineering.cerner.com/smart-on-fhir-tutorial/) is a basic example of how a FHIR app can be built and run with [example code](https://github.com/cerner/smart-on-fhir-tutorial).

Looking into the [Cerner Millennium API](https://www.google.co.uk/search?q=cerner+millennium+api) search results should be interesting...

## Cerner Open Developer Environment (CODE - code.cerner.com)

*TLDR: Waste of a website with no content*

First up in the Google results is [https://code.cerner.com](https://code.cerner.com) which looks promising as:

> Cerner Ignite APIs for Millennium allow outside apps to be integrated with the Cerner Millennium EHR platform. These APIs are Cerner’s implementation of SMART Health IT and the HL7® Fast Healthcare Interoperability Resources (FHIR®) standard.

... however this appears to be **a shell website consisting of minimal marketing and zero content**. Its purpose is to sign you up to a newsletter. At time of writing most of the content is on a Blog within the site, and hasn't been updated in 4 months, with the first update from Oct 2015, but they're short link articles to press releases on the main Cerner site.

Yet, from Google (and not easily findable from the site), you can see https://code.cerner.com/ehr-api, which essentially links you to http://fhir.cerner.com and the SMART On FHIR example marketing material.


## Cerner Accounts
There are multiple places to register for access to Cerner areas/tools/systems, and they have a multitude of account management systems

* [uCern Account](https://connect.ucern.com/get-started) (Cerner uCern **Connect**)
* [uLearn Account](https://ulearn.cerner.com/showAccountPrefs)
* [Cerner Account](https://cernercare.com/accounts) (CernerCare account login). Management is at [https://accounts.cerner.com]() *which is nigh on impossible to find a link to from anywhere!*

The Cerner Account link can also be found on the wiki page [Cerner Web Applications](https://wiki.ucern.com/display/CAP/Cerner+Web+Applications), which asks you to *"Bookmark this uCern Space and make it your go-to location for access to Cerner Applications"*

### Cerner Websites

#### Support
* [Cerner Support](https://support.ucern.com/Destination.aspx). Links to:
  * [eService](https://associates.cerner.com/accounts) for Cerner Associates only
  * [Help Desk](https://helpdesk.ucern.com) which errors on load suggesting its either dead or not usable
* [Cerner Classic Support](https://wiki.ucern.com/pages/viewpage.action?pageId=969441308) - *"The uCern Wiki HNA Classic Reference Pages are your source for HNA Classic solution documentation. Reference Pages allow you to contribute updates, provide feedback, receive update notifications, and much more."*
* `[DEAD]` Cerner Knowledge Manager Downtime (CKM) http://www.cerner.com/CKM-Downtime/ - *"Cerner Knowledge Manager is currently unavailable. We are working to get service restored." <-- Irony*
* [Cerner Support Dashboard](http://www.cerner.com/supportdashboard) -- redirects to [MyBI portal](https://mybi.cerner.com/analytics/saw.dll?dashboard). *Not compatible with Safari, works with Firefox.*

#### Systems Management
* [Distributions](https://distributions.cerner.com/) - Appears to be software downloads. *Investigate the [Linux Cerner Millennium](https://distributions.cerner.com/Downloads/dMillennium_Set.asp) 2015.01 Release Update Client Feb 2015 New Install* 
* [Flashes](https://flashes.cerner.com) - 3000+ news item style update notifications
* [Physician Practice Flashes](https://connect.ucern.com/community/healthcare-organizations/cerner-ambulatory-asp?view=overview) - uCern Connect Organisation linking to groups and pages
* [Lights On Network](https://lightson.cerner.com) - General info on the network
  * [OUH LoN Dashboard](https://lightson.cerner.com/clients/OUH_UK/domains/P0481/overview/kpi/)
* [Bedrock](https://wiki.ucern.com/display/public/reference/Bedrock+Overview) - uCern wiki, page missing
* [MethodM](https://methodm.cerner.com/), redirects via CernerCare account login (occasionally problematic) to a Sharepoint site, mostly listing .jar files 

#### Business
* [Cerner eBill](https://ebillsso.cerner.com/) - Apart from having a link to manage your CernerCare account (rare find!), this is otherwise a non-applicable website with a holding page on
* [Solution Descriptions](https://solutiondescriptions.cerner.com) - 
  * *"Below is a comprehensive listing of the current Cerner Solution Descriptions by Industry Classification. To view more details expand the category."* As an example, the [MPages Development Kit](https://solutiondescriptions.cerner.com/Home/ViewFile?filerefno=PS-22700_03) contains an empty template with no usable content in it! Just "Click here to type" written in for each of the five fields (Document #PS-22700, Version 3)
  * Thankfully other PDFs do contain short bits of content acting as a bullet point summary of features or licensing
  * Links to: [Contracts](https://contracts.cerner.com/admin/default.aspx) - *"You do not have access to view contracts online. Note: Client contracts are strictly confidential and are not to be accessed, downloaded, copied or forwarded without express permission from Cerner's Finance team. Access to these files is monitored and recorded."*
  * Links to: [Passthrough Provisions](https://passthroughprovisions.cerner.com)

#### Training
* [Illuminations](https://connect.ucern.com/community/illuminations) uCern Connect Organisation which supposedly provides "Unique web-based presentations that focus on the vision, direction, functionality, highlights, optimisation, and release of Cerner Solutions". The Client Illuminations list is predominately a list of documents providing links to register for upcoming WebEx conference calls, and video files and pdfs for past calls.
* [uLearn](https://ulearn.cerner.com) - a collection of free and charged-for eLearning courses. Be prepared to experience a lot of marketing dressed up as learning materials.

#### uCern
* [Connect](https://connect.ucern.com/news) is Cerner's social media platform that wraps around several of their websites. You can "follow" groups and discussions, and then get notifications on your profile. It's a poor man's attempt at LinkedIn, where it isn't easy to find people to follow, even in your own organisation.
* [Events](https://events.ucern.com/) is exactly what it sounds like, a list of Cerner events
* `[DEAD]` [Organisations](https://organizations.ucern.com/) is "uCern Organizations is a place to learn about your organization and connect with others" but results in a 403 Forbidden code after login, so no connecting or learning going on there.
* `[DEAD]` [Meaningful Use](https://meaningfuluse.ucern.com/about.do) https://meaningfuluse.ucern.com/
* [Search](https://search.ucern.com)... a search box on a page, which after logging in with a CC account, you can do a search over uCern content
* [Wiki](https://wiki.ucern.com/dashboard.action) is a Cerner hosted wiki, with a nightmarish lack of content management and linkage. But also contains l

### Other Dead Cerner Websites

* Cerner Store: https://store.cerner.com/ -> Redirects to cerner.com