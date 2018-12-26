# Webex Teams - Compliance Data - JSON to CSV Format

This is a Python3 script written to convert Webex Teams JSON-format Compliance data in to a CSV Flat file structure.

Modules Used:
```
flatten https://github.com/amirziai/flatten
pandas https://github.com/pandas-dev/pandas
(note: both modules have required modules such as numpy, etc)
```

Both Modules can be installed using 'pip3 install flatten pandas' and pip will take care of the other required modules. Please note, all modules may require different compilers in different circumstances and may throw errors if not available.

This file was tested under Cygwin on a Windows 10 environment using Python3. Cygwin specifically needed the following bits and pieces installed:
```
gcc-core, gcc-fortran, gcc-g++, wget, libgtk2, python3-devel, python3, python-gtk2.0, python3-pip, make, libpng16, libpng16-devel
```
Not all of these were required for the script, but rather for the installation of pandas and its required modules.
This may vary on a proper Linux installation, please refer to the guides for each specific module above for installation requirements.

# How to run the script

Currently this script is not very dynamic, it should take sysargs as input for the JSON file name, however for now I have hardcoded it in the function in the script.

```
# Call flattenjson function + JSON File Name
flattenjson('c44f5690-6db9-11e6-8c7e-016ddef37535.json')
```
Please update the .json file name to the file you want to convert.
