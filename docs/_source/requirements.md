# Requirements

This page is going to evolve a lot over the course of this project, mostly because the scope of the overall project is huge, and that there will need to be many mini-projects, with their own link to requirements, that will come from this process.

**Process notes:**

* There will need to be a way to link to and from requirements. This will mean implementing a naming/tagging scheme for linking work tasks back to requirements; and a reference scheme for linking requirements to sources
* Some of the sources are likely to be people, but they should be abstracted to be role related requirements (i.e. the role of the person, rather than the actual person). To help with auditing and feedback though, an offline reference list of specific requirements from specific individuals may be needed (To be discussed further)
* The expectation is that we'll use the repository Issues system to track work items, which means having a stable set of URIs for referring to the requirements
* Documentation for this project (and sub-projects) will be a priority (and therefore a high priority Non-functional Requirement in itself), and the planned toolchain will have us using Sphinx to compile and index the documents and files, with developer contributed content coming in the form of plain text files (either .md Markdown, or .rst ReStructured Text)
* We still need to choose and adopt a suitable template for requirements gathering and reporting. Some examples can be seen at:
 * [http://stackoverflow.com/questions/171653/examples-of-requirement-documents]()
 * [http://techwhirl.com/writing-software-requirements-specifications/]()
 * [https://en.wikipedia.org/wiki/Software_requirements_specification]()


## Draft Content

### Technical Requirements

1. FHIR used as the standard for data persistence and communication
 * Interoperability is essential, FHIR embodies this, be it Human Readability for data, through to use of common technologies like REST APIs and good Documentation.

2. SNOMED CT used as the standard for clinical data coding. The NHS National Information Board (NIB) [has specified that](http://systems.digital.nhs.uk/data/uktc/snomed) SNOMED CT is to be used as the single terminology in all care settings in England. The move to using a single common terminology in electronic integrated care records means:
 * information can be shared consistently within and across all health and care settings
 * data can be organised for the benefit of the individual's care, for example highlighting current health problems
 * data can be organised for the benefit of groups of individuals, for example identifying trends resulting from change in clinical practice
 * the risk of different interpretations of the record between different care settings can be reduced.