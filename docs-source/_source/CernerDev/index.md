# Cerner Development
There are a lot of areas of concern, and large gaps in knowledge (both available and received), when it comes to developing in the Cerner Millennium Environment. We want to improve this situation by sharing and curating our findings and experiences here.

## Guides
Concise (and mostly short) documents on a range of common topics

### How-to
1. [Create an mPage project](./guides/build_mpage_project.md)
2. [Build an mPage project](./guides/create_mpage_project.md)
3. [Deploy an mPage project](./guides/deploy_mpage_project.md)
4. [Register for Cerner Development access](./guides/register_for_cerner_development.md)
5. [Register for Cerner Lights On Network access](./guides/register_for_cerner_lon_access.md)

And the presently uncategorised [Miscellaneous Notes](notes.md).

## Mini-projects

### [Test/Probe Environment](test.md)

A set of scripts/tools that can probe the workings of PowerChart and similar from the inside, and provide both understanding of what is enabled, and longitudinally a view on what changes. Hopefully this will also turn into a useful diagnostic tool for the support teams to use to help identify any obvious causes of things not working as expected.

### [Database Schema Documentation](database.md)

An embryonic approach to sharing our knowledge of how our patient data (and related metadata) is actually stored at the base level within the Cerner+Oracle DB. 

### [JS/Browser Debug Utilities](debug.md)

Given the limitations of testing scripts on a virtual desktop, within a third party application, we lack the use of common browser based diagnostics. This project aims to gather and build a suite of tools that we can embed to provide better insights as to what is and isn't working with our code once inside PowerChart.