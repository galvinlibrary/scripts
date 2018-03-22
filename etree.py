import xml.etree.ElementTree as ET

tree = ET.parse("C:\\test_data\\mods.xml")
#tree = ET.parse("C:\\test_data\\test.xml")

root = tree.getroot()


for child in root:
    print(child)

for child in root.find("{http://www.loc.gov/mods/v3}subject").getchildren():
    print(child)
 

#for idt in root.iter('{http://www.loc.gov/mods/v3}physicalDescription'):
#    print(idt.tag)
