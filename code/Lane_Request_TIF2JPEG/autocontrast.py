"""Autocontrast script, place folder in DIRECTORY_LOC"""
import os  # used in date, directory naming
from datetime import date
import imagej  # imports necessary imagej module

day = date.today()
ij = imagej.init('sc.fiji:fiji')  # activates imagej

## Two Options:
## 1. create convert to JPEG to PNG-> Autocontrast
## 2. autocontrast JPEG -> convert to PNG       
## if no difference, autocontrast the PNG and overwrite them
## if there is a differet

# MACRO USED IN PyImageJ
MACRO = """
#@ String input
#@ String output
open(input);
run("Enhance Contrast", "saturated=0.35");
saveAs("PNG", output);
close();
"""
day = date.today()

def search_copy(sub_loc):
    """Searches and Copies a Directory while running each file through PyImageJ"""
    new_directory = os.path.join(os.path.dirname(sub_loc), ('AutoContrast_ImageJ_' + str(day)))
    for dirpath, dirnames, filenames in os.walk(sub_loc):
        new_loc = new_directory + '/' + os.path.basename(dirpath)
        os.makedirs(new_loc)
        for files in filenames:
            args = {'input': os.path.join(dirpath, files), 'output': os.path.join(new_loc, files)}
            ij.py.run_macro(MACRO, args)


DIRECTORY_LOC = '/workspaces/ImageJ_Automated_Macro/code/test_dir/omega'
search_copy(DIRECTORY_LOC)
