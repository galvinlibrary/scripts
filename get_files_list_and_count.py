import os
import csv

contents = []

home = 'C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\patents'

dirlist = os.listdir(home)

for d in dirlist:
    files = os.listdir(home + '\\' +d)
    #contents.append(files)
    num = len(files)
    #my_list = [d, num]
    #contents.append(my_list)
    files.insert(0, num)
    files.insert(0, d)
    contents.append(files)
    
print(contents)
    
with open('C:\\Users\\tfluhr\\Documents\\islandora_cleanup\\patents\\filelist.csv' , 'w') as derp:
    writer = csv.writer(derp)
    writer.writerows(contents)
