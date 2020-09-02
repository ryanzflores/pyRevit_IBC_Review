# pyRevit_IBC_Review
This [pyRevit](https://github.com/eirannejad/pyRevit) plugin helps users calculate a (single-occupancy*) building's
maximum height, stories, and area, as specified in Chapter 5 of the 2018 International Building Code
(https://codes.iccsafe.org/content/IBC2018P4/chapter-5-general-building-heights-and-areas).
The plugin was made to be able to easily accommodate updates to the code and local revisions to the code;
see the info below for details on how to add different versions to use.

**This plugin is intended to provide a quick estimate, and is not a replacement for a professional code review. 
This plugin will warn you about some possible complications that can affect the accuracy of the calculations made,
but these warnings may not be comprehensive.**

\* This plugin *can* be used to calculate individual occupancies in a mixed-occupancy building, however,
sections of Chapter 5 (namely, section 508, 506.2.2, and 506.2.4) complicates things. Please only do so
if you know what you're doing.

## Installation

This plugin requires [pyRevit](https://github.com/eirannejad/pyRevit). 
If you have not installed pyRevit, please do so using the
instructions found here: https://www.notion.so/Install-pyRevit-98ca4359920a42c3af5c12a7c99a196d

Download the zip containing the plugin's files using the green download button above.
Unzip the files and remember where you placed them, as you'll need the directory containing the
.extension folder.

#### If you do not have a custom extension directory set up:

In Revit, go to the pyRevit tab, click on the pyRevit dropdown on the far left, and
click "Settings". In the tab labelled "Custom Extension Directories", click add folder and
select the folder directly containing the folder labelled "pyRevitIBC.extension". If you
didn't edit the name of the zip file, the folder you want to select is probably called
"pyRevit_IBC_Review-master".

After adding the folder to the list of directories, you'll need to reload the plugin.
This won't close your Revit window and should only take a short moment.

The plugin will be available under the new "pyRevitIBC" tab at the top of the Revit window.

#### If you do have a custom extension directory set up:

Simply cut or copy the .extension folder contained in the .zip and paste it into
your custom extension directory. 

Alternatively, if you want to include the button for the helper in a different panel in a different tab 
(and/or are annoyed by the fact that the plugin is hogging an entire tab all to itself), 
either cut/copy the "App.panel" folder and paste it into a pre-existing "\*.tab" folder, or
cut/copy the "Building Height Stories and Area.pushbutton" folder and paste it into a pre-existing "\*.panel" folder.

## Adding code versions

This plugin is designed so that IBC.py (and whatever other codes are added) are as decoupled as possible from script.py.
The initial window allows you to select a building code, group, use, type, and sprinkler. The values for the
building code are gathered from a tuple called "available_codes", and the values for the other fields are populated
based on the "table_info", "table_sprinklers", and "table_types" variables from the selected code module.
Pressing the "Continue" button on the initial window submits the selected group, use, sprinkler, and type to
the selected building code module's show_results method. From there, the selected code module figures out the values
to display and shows them in a new window.

To make a new code version to be used by this plugin, it is recommended to copy IBC.py and use it as a template. The
code throughout the module is commented with templates for variables and brief explanations.

To ensure compatibility with script.py, it is important to follow the formats described for "table_info",
"table_sprinklers", and "table_types", as the data contained in these variables is used to populate the options for
the initial window. Specifically, the keys in table_info are used to populate the groups, and for the values assigned
to these keys, the first tuple is a group's available uses (potentially empty), and the second tuple is a group's
available sprinklers (either a tuple if each use has the same sprinklers, or a dict if different uses have different
sprinklers). Next, the table_sprinklers dictionary assigns each sprinkler some descriptive text. Finally,
table_types lists the available types.

allowable_height, allowable_stories, and allowable_area are all based off of tables described in 
[Chapter 5 of the IBC](https://codes.iccsafe.org/content/IBC2018P4/chapter-5-general-building-heights-and-areas). 
Comparing the code in each
method with the corresponding table (listed above the method header) should make the format for these methods clear.
One exception is that the keyword "ANY" is used when any possible value is allowed. For example, for groups B, E, M,
and U, "ANY" was used as the only possible use, as there are no uses specified for these groups in the tables. 