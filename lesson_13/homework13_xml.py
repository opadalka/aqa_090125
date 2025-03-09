import xml.etree.ElementTree as ET
from pathlib import Path
import logging

xml_path = Path(__file__).parent / "groups.xml"
tree = ET.parse(xml_path)
root = tree.getroot()

#Find property in xml file
def get_property_from_xml():
    for group in root.findall('group'): 
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                value_log_pos = f"Number: {group.find('number').text}, incoming: {incoming.text}"
                log_event_console(value_log_pos)
        else:
            value_log_neg = f"Number: {group.find('number').text}, incoming: Не знайдено"
            log_event_console(value_log_neg)

#Create log function
def log_event_console(log_message):
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),  # Виведення в консоль
                    ])
    logger = logging.getLogger(__name__)
    logger.info(log_message)

    
get_property_from_xml()