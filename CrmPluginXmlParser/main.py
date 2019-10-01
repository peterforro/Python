import os
from XmlParser import XmlParser

src_filename = 'plugins.xml'
working_dir = os.getcwd()
file_path = working_dir + '\\src\\' + src_filename
result_path = working_dir + '\\out\\'

if __name__ == "__main__":
    xml_parser = XmlParser(file_path)
    xml_parser.write_to_file(result_path)
    
    