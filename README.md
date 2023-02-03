
# Recursive Convert and/or Contrast Script

search_convert.py
Script to convert TIF to JPEGs with ImageJ
1. Copies Parent Folder to renamed Parent Folder
2. Recursively Searches and runs Image Conversion Macro on TIF
3. Saves images to folder 
Final is UNIX/MACOS compatible

autocontrast.py
Script to convert TIF to PNG with ImageJ
1. Copies Parent Folder to renamed Parent Folder
2. Recursively Searches and runs Image Conversion/Autocontrast Macro on TIF
3. Saves images to folder 
Final is UNIX/MACOS compatible

# Guide
Following https://github.com/imagej/pyimagej

1. conda install mamba -n base -c conda-forge
2. mamba create -n pyimagej -c conda-forge pyimagej openjdk=8
3. conda activate pyimagej

4. Edit DIRECTORY_LOC to directory above folders containing the pictures
5. $ python search_convert.py 
5. $ python autocontrast.py
