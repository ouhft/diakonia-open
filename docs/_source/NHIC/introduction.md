# Introduction

Overview: ???


## Common Terms
* **NIHR** - NHS National Institute for Health Research [http://www.nihr.ac.uk/]() 
* **HIC** - Health Informatics Collaborative [http://www.nihr.ac.uk/about/hic.htm]()
* **TRA** - Renal Transplantation Theme (one of five themes within the HIC project)
* **ACS** - Acute Coronary Syndromes (another theme)
* **CAN** - Ovarian Cancer theme
* **HEP** - Hepititis theme
* **ICU** - Critical Care theme
* **GSTT** - Guy's and St Thomas Trust, one of the TRA theme partners, and theme lead

## Resources
* NIHR Website - single page overview: [http://www.nihr.ac.uk/about/hic.htm]()
* NIHR Google Hub - a shared Google instance related to a `@nihr.ac.uk` address. Not very much on there at all.
* Old BRC/HIC shared documents - via the Google Hub, in `Shared with me -> OxBRC`. Has a fair amount of dated content. Barely updated since 2014.
* New BRC/HIC shared documents - also via the [Google Hub](https://drive.google.com/open?id=0BxVx4JelQXE_aE9OU0VnMGVQMFk), but this time in `My Drive -> HIC Shared Documents`. More current documentation, but still a dearth of Transplantation information (mostly due to there being little work done on it to date)
* Ryan's [GitLab project](https://gitlab.com/spikeheap/nhic-tra-extract) - From his work to use Talend Open Studio to map NHS BT data to the HIC xsd specification.
 * The Talend files can be simplified down to just looking at the `talend_workspace/NHIC_TRA_OXFORD/process/NHSBT_to_XML_0.1.item` file, and using the `OutputTrees` element (ln1351 onwards) as the main guide.
 * There are some data cleanup steps which can be seen as simple if functions within the code, for example replacing "." with null in some cases. 
* BRC [Bitbucket repositories](https://bitbucket.org/account/user/oxfordbrcinformatics/projects/NHIC) - some more code locations for things done in the BRC
* More files from Ryan with a Mapping XLSX file in from an unknown source from early on in the project that translates NHSBT file into XSD headings.

## To sort:

* Local files in `~/Documents/NHIC`. Need a repository workspace setting up for storing of content off of laptop.
 * Awaiting some feedback on whether to set up a BRC Gitlab instance
 * Will do a local workspace and project for the time being
* PC Laptop that works on the NHS network. Still needs setting up and credentials set.