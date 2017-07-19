# TRA Processing
The overall aim here is to merge as many data sources as required together, into a complete submission for the NIHR-HIC theme.

This primarily means mapping the NHSBT dataset to the NHIC xsd specification, but the gaps in that dataset need to be filled with H&I data, and Biopsy report data.

## Design
Basic principle is to generate a schema that maps to the NHIC xsd closely, and to extend that schema with any additional data that may be useful from the local sources. 

Process will involve loading an NHSBT data sample into an empty datastore, and then mapping the H&I and Biopsy data to those records. Finally it should be possible to generate the XML export file.

v1 can treat this as a manual CLI process with import commands, and an export command.

v2 can put some analytics and display information into a UI and allow files to be uploaded and downloaded from that portal.

## Work plan

#### Plan as of 2/6/16
Working on the `export_xml` command, using the `xml.minidom` to generate an xsd compatible file. Basic outlining work in progress, with mapping work to begin soon. Then we look to get the `load_nhsbt` command to import the xlsx data via the relevant forms into the data model.

#### Plan as of 19/5/16
Background:

* Generate DS didn't give any useful structure from the XSD because the XSD lacks any useful structure (for starters, there is no definition of what the root "record" element represents!)
* XSD parsing with Oxygen XML Editor and some consultation with other Oxford BRC members concluded that this isn't a helpful schema. Reference was then made to a set of UML models created 2 years ago at the start of this project. Reviewing those gave me a better starting point.
* No information or data structure examples have been received from GSTT
* Now have derived an initial model structure to handle Transplant data, with the emphasis on being Organ-centric. Organs are moved between people (the Donor and Recipient) via Operations, and the Recipient Person is given the most medical attention with Followups and Pre-operation investigations. The Donor Person may or may not be alive when the organ(s) are extracted. One Operation can handle multiple Organs (both extraction from Donor, and transplanting/grafting onto Recipient) so a web of data should emerge over time, though mostly in fairly small clusters.
* It should be noted that this schema implicitly presumes Kidneys are the organs of choice.
* We have a basic mapping of NHSBT xlxs data to the XSD data based on previous submission work and a document from the project archive.

Next steps:

1. We have a basic Excel Util to load the NHSBT data. Need to map that onto the new data models
 * Generate model forms - DONE
 * Mapping exercise...
 * Write a CLI function to take the xlsx file and ingest it
2. JF has created views onto the PSS system to get more information for this, so we need to get a list of what, and then map that accordingly
 * How we'll receive and can query this data is still unknown, so the implementation of this stage is vague.
3. All the translated and unit/type fields need examination to ensure we have the correct data types defined for capturing the information sensibly
 * Find a friendly clinician as a starting point and/or wikipedia/google
4. Mapping of the data model into the XSD, and outputing an XML file from a template design
 * Generate an XML template and corresponding view
 * Start basic and see what validateds


#### Plan as of 14/4/16 

...is to use the existing (poor) XSD to test the process, and then to work on a more sensible XSD and data model.

- Example data structure to come from GSTT/Syed
- Looking at the data structure again, can develop a much simpler DB model, and ultimately, xsd. So, build new model, then do the import, and export processes

#### Plan as of 3/3/16

1. Setup dev environment - DONE
2. Generate a model structure based on the NHIC xsd, and explore
 *  generateDS code is semi-functional
 *  Can use the pypi code to generate utility classes
 *  Getting Django classes from it isn't working
 *  Requires that you download the package source code and run as scripts - DONE
 *  But the scripts don't run under python2, nor under python3, though they get closer on the latter
 *  Debugging those scripts via 2to3 and some edits has now got them working.
 *  The importlib process has a problem with xsd files containing periods, thus have renamed the xsd to `NHIC_TRA_1-6-0.xsd`
 *  Running instructions from [generateDS Django docs](http://www.davekuhlman.org/generateDS.html#examples-and-demonstrations) results in a command of `./gends_run_gen_django.py -f NHIC_TRA_1-6-0.xsd` 
 *  This creates admin, models, and forms .py files.
 *  Moved the raw code across, but finding various helpful bits missing - like the description text being used for verbose_name, FK's not having their null attribute set, etc. The GenerateDS functions are very rudimentary in their approach, but non-trivial to amend, so doing a manual update from XSD to `ingest/models.py`
 *  ... This process is paused pending rewrite/review of the XSD
3. Write utils to load the excel sheet
 * Initial load utils created
 * Column dictionary generated with NHSBT headers, and comments linking to their NHIC mapping id 
4. Build input forms to validate and map the data into the model
5. Add in lots of logging to record data transformation/substitution changes