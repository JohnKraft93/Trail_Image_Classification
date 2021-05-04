import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


trailheads = ['kebler', 'brush', 'cement', 'gothic', 'washington', 'snodgrass', 'slate']

def xml_to_csv(paths):
    xml_list = []
    for p in range(len(paths)):
        for xml_file in glob.glob(paths[p] + '/*.xml'):
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for member in root.findall('object'):
                value = (trailheads[p] + root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list.append(value)
        
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    image_paths = []
    for i in range(len(trailheads)):
        image_paths.append(os.path.join(os.getcwd(), 'Annotations/' + trailheads[i] + 'Annotations')) #Gets annotation directory
        
    xml_df = xml_to_csv(image_paths) # puts all the .xml files into a dataframe
    xml_df.to_csv('data2/all_labels.csv', mode='a', index=None) #converts dataframe to a .csv file and saves it
    print('Successfully converted xml to csv.')


main()
