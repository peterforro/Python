class Image:

    def __init__(self: object, element: object) -> None:
        self.element = element
        self.image_type = element.attrib.get('ImageType')
        self.entity_alias = element.attrib.get('EntityAlias')
        self.attribs = str(element.attrib.get('Attributes')).split(',')
        
    def __str__(self: object) -> str:
        string = 4 * '\t' + f'Image type: {self.image_type}\n'
        string += 4 * '\t' + f'Entity alias: {self.entity_alias}\n'
        string += 4 * '\t' + f'Attributes: {", ".join(self.attribs)}\n'
        return string