import os
import sys
import lxml.etree
import numpy

#location of dspace export root and transfrom xsl
root = 'C:\\transform'
#location to place processed files.  Directory must be created beforehand. Not used for this...
#processed = 'C:\processed\\'


def get_dirs(directory):
    
    #create array of subdirectories
    basedirs  = []
    
    for wd, dirs, files in os.walk(directory):
        
        for folder in dirs:
            #join root directory and subdirectory 
            dir_path = os.path.join(root, folder)
            basedirs.append(dir_path)
            #print(file_path)
    
    return basedirs
    #print(basedirs)

dir_array = get_dirs(root)
counter = 0
mods_array = []
xsl = "C:\\transform\\dc_to_mods_2018_new.xsl" #Location of xsl


for dir in (dir_array):
    unformatted = dir + "\dublin_core.xml" # DC file to use in transform
    mods = dir + "\mods.xml" # New mods.xml file location
    counter += 1
    
    #check to see if metadata_iit.xml exists
    
    target = dir + "\metadata_iit.xml" #
    mods_array.append(target)

    if os.path.isfile(target):
        print("file found. Using existing metadata")
    else:
        # Copies metadata_iit.xml template to be used in transform
        print("metadata not found...Copying from template.")
        os.popen("copy C:\\transform\\metadata_iit.xml C:\\transform\\3")
        
    
    xml_input = lxml.etree.parse(unformatted)
    xslt_root = lxml.etree.parse(xsl)

    transform = lxml.etree.XSLT(xslt_root)
    derp = (str(transform(xml_input)))

    fd = open(mods, 'w', encoding="utf-8")
    fd.write(derp)

    #print(derp)
