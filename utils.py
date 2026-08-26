import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime


def print_plays_data(writeNew=False, filename="plays.xml"):
    file_path = ET.parse(filename)
    root = file_path.getroot()

    if writeNew:
        for play in root.iter('play'):
            if(play.find("item").attrib['name'] == "Magic: The Gathering"):
                play.find("item").attrib['name']="Magic: I do not like this game"
        
        filename = datetime.now().strftime("plays_%Y-%m-%d_%H.xml")
        file_path.write(filename)
    else:
        for play in root:
            print(play[0].attrib['name']) 
            print(play[1].text)



def numberAdder(a, b):
    return a + b
