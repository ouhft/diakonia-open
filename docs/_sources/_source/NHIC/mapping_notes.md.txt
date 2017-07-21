# Mapping notes
This document (from Ryan Brooks) contains implementation notes to aid maintenance of the transform.

### Requirements

This transformation is built with the [Talend Open Studio Data Integration](https://www.talend.com/products/talend-open-studio) suite. 

* Talend Open Studio Data Integration, >~5.6.2.
* Git

### Transformation steps

The transform is broken down into 5 steps:

1. Extract the Excel spreadsheet.
2. Map the spreadsheet columns to NHIC data elements.
3. Replace spurious values with `null`s.
4. Replace input strings with their enumerated counterparts.
5. Load the output XML file.

### Replacements

The primary role of the replacements is to swap input values for valid enumeratied values in the XML, for example swapping `Positive` for `Pos`.

There are also many values which are non-values, for example `Not tested`, `Awaiting result`, and `Unknown`, when valid values in the XML are `Positive` and `Negative`. 

#### NHIC_TRA_43-1
* `Unknown` -> `0` (Not known)

#### NHIC_TRA_44-1
* `Burns` -> `17` (Other)
* `Cardiovascular - type unclassified` -> `17` (Other)
* `Chronic pulmonary disease` -> `17` (Other)
* `Liver failure (not self poisoning)` -> `17` (Other)
* `Pneumonia` -> `17` (Other)
* `Respiratory - type unclassified (inc smoke inhalation)` -> 
* `Respiratory failure` ->
* `Septicaemia` -> `17` (Other)
* `Other drug overdose` -> `6` (Drug overdose)
* `Not reported` -> `18` (Unknown)
* `Infections - type unclassified` -> `8` (Infection)
* `Trauma - RTA - car` -> `16` (Trauma)
* `Trauma - RTA - motorbike` -> `16` (Trauma)
* `Trauma - RTA - pedestrian` -> `16` (Trauma)
* `Trauma - RTA - pushbike` -> `16` (Trauma)
* `Trauma - RTA - unknown type` -> `16` (Trauma)
* `Other trauma - accident` -> `16` (Trauma)
* `Other trauma - unknown cause` -> `16` (Trauma)
* `Other trauma - suicide` -> `16` (Trauma)

#### NHIC_TRA_45-1
* `Mixed` -> `G` (Any other mixed background)
* `Other` -> `S` (Any other ethnic group)

#### NHIC_TRA_56
* `Peritoneal dialysis` -> `PERITONEAL DIALYSIS (CAPD/APD)`
* `Haemodialysis` -> `UNIT HAEMODIALYSIS` ** THIS IS A MASSIVE ASSUMPTION **

#### NHIC_TRA_70-1

* `Living unrelated - Altruistic` -> `LIVING UNRELATED`
* `Living unrelated - Pooled` -> `LIVING UNRELATED`
* `Unknown` -> removed

#### NHIC_TRA_71-1
* `ALTRUISTIC NON-DIRECTED DONOR` -> `OTHER LIVING NON-RELATED DONOR - PLEASE SPECIFY`
* `POOLED DONOR` -> `OTHER LIVING NON-RELATED DONOR - PLEASE SPECIFY`
* `LIVING NON-RELATED DONOR - PARTNER` -> `LIVING NON-RELATED DONOR - SPOUSE`

### `m` attributes

The modification time (`m`) attributes have been omitted from the transformation, because each transformation will include the entire NHSBT extract and will therefore supercede any prior values. The NHSBT extract doesn't contain timestamps for modifications, so it would only be possible to add the `m` value of the extract or transformation date and apply that to all elements.


