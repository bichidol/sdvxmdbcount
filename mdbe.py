import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description='Count the number of music IDs in musicdb.')
parser.add_argument('xml_file_path', help='Path to musicdb.xml')

args = parser.parse_args()

with open(args.xml_file_path, 'r', encoding='shift_jis', errors='replace') as f:
    xml_content = f.read()

root = ET.fromstring(xml_content)

music_id_count = 0

for entry_num, music_element in enumerate(root.iter('music'), start=1):
    music_id = music_element.attrib.get('id')
    if music_id:
        music_id_count += 1
        print(f"Entry Number: {entry_num}, ID Number: {music_id}")

print(f"Total number of music IDs: {music_id_count}")
