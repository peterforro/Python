import xml.etree.ElementTree as ET
from Plugin import Plugin

class XmlParser:

    plugin_tag = '{http://schemas.microsoft.com/crm/2011/tools/pluginregistration}Plugin'

    def __init__(self: object, file_path: str) -> None:
        self.tree = ET.parse(file_path)
        self.root = self.tree.getroot()
        self.plugins = self.__load_plugins()
        
    def __load_plugins(self) -> list:
        plugins = []
        for plugin in self.root.getiterator(XmlParser.plugin_tag):
            plugins.append(Plugin(plugin))
        return plugins

    def write_to_file(self, dir_path: str) -> None:
        for plugin in self.plugins:
            with open(dir_path + plugin.friendly_name + '.txt', 'w') as file:
                file.write(plugin.__str__())