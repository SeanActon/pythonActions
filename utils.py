import xml.etree.ElementTree as ET
from pathlib import Path


def print_plays_data(writeNew=False, filename="plays.xml"):
    file_path = ET.parse(filename)
    root = file_path.getroot()

    if writeNew:
        for play in root.iter('play'):
            if(play.find("item").attrib['name'] == "Magic: The Gathering"):
                play.find("item").attrib['name']="Magic: I do not like this game"
        
        file_path.write("newPlays.xml")
    else:
        for play in root:
            print(play[0].attrib['name']) 



def numberAdder(a, b):
    return a + b
