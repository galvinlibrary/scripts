import sys
import os, os.path
import zipfile
import csv
import shutil


def move(src, dest):
    shutil.move(src, dest)

all_subs = []
dirs_w_zip = [] # list of directories containing zip files
dirs_wo_zip = [] # list of directories without zip files
zips = [] 
subs_file_list = [] # list of subdirectories and files

zip_done = 'C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\proccessed\\zipcomplete' # directory of processed etds that contained zip files
no_zip_done = 'C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\proccessed\\nozipcomplete' # directory of processed etds that contained NO zip files

export = 'C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\test'

dirlist = os.listdir(export)

for d in dirlist:
    all_subs.append(export + '\\' + d)
    subd = export + '\\' + d
    
for d in all_subs:
    files = os.listdir(d)
    for f in files:
        if f.endswith('zip'):
            short_sub = d
            dirs_w_zip.append(d)
            zips.append(f)
            zip = d + '\\' + f # get name of zip in each dir
            
            zf = zipfile.ZipFile(zip, 'r') 
            zcontents = zf.namelist()  # get contents of each zip 
            zcontents.insert(0, short_sub)
            #subs_file_list.append(zcontents) # get list of files
            zf.extractall(d) # extract zip contents to ../
            zf.close()
            os.remove(zip) # remove zip file
            files = os.listdir(d)  # new stuff next 4 lines
            contents = os.listdir(d)
            contents.insert(0, d)
            subs_file_list.append(contents)
            
for d in dirs_w_zip:
    move(d, zip_done)

for d in all_subs:
    if d not in dirs_w_zip:
        dirs_wo_zip.append(d)
        files = os.listdir(d)
        contents = os.listdir(d)
        contents.insert(0, d)
        subs_file_list.append(contents)
        
for d in dirs_wo_zip:
    move(d, no_zip_done)
        
with open('C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\proccessed\\filelist.csv' , 'w') as derp:
    writer = csv.writer(derp)
    writer.writerows(subs_file_list)
