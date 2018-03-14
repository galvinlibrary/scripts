import os
import numpy

#location of dspace export root
root = 'C:\\item_2598\\1'
#location to place processed files.  Directory must be created beforehand
processed = 'C:\processed\\'


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
    
dir_array = get_dirs(root)

# build file list for each sub dir 
def get_file_list(x):
    #Create array of subdirectory file contents
    file_list = []
    counter = 0
    for dir in (x):
        #Create array of file size in each dir
        size_array = []
        counter += 1
        obj_path = dir
        for wd, subs, files in os.walk(dir):
            #Create list of files in subdirectories
            sub_dir_list = []
            for f in files:
                full_path = os.path.join(wd, f)
                sub_dir_list.append(full_path)
                file_size = os.path.getsize(full_path)
                size_array.append(file_size)
            #defines index of largest file
                biggest = numpy.argmax(size_array)
            print(biggest)
            
            file_list.append(sub_dir_list)
        #need to use index(biggest) to grab largest file strip name before extension and move to new dir
        item_path = (sub_dir_list[biggest])
        #get item filename
        item = (os.path.basename(item_path))
        item_base = item.split('.', 1)[0]
                
        #strip item of file ext to create string to use in mods.xml rename
        move_path = (processed + str(counter) + '\\' + item)
        xml_move_path = (processed + str(counter) + '\\' + item_base + '.xml')
        #create processed subdir
        if not os.path.exists(processed + str(counter)):
            os.makedirs(processed + str(counter))
        #move item to processed dir
        os.rename(item_path, move_path)
        #move mods.xml to processed dir
        #get mods.xml
        if os.path.isfile(obj_path + '\\mods.xml'):
            os.rename(obj_path + '\\mods.xml', xml_move_path )
            #print("file exists")
        else:
            pass
        # test stuff to make sure things are working
        #print(counter)
        #print(move_path)
        #print("Actual Item Path: " + item_path)
        #print(item)
        #print(size_array)
    return file_list
    #print(file_list)
    
            
blah = get_file_list(dir_array)


print(dir_array)

#print(file_array)   

print(blah)
