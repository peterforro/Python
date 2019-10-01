from Image import Image

class Step:

    image_tag = '{http://schemas.microsoft.com/crm/2011/tools/pluginregistration}Image'

    def __init__(self: object, element: object):
        self.element = element
        self.message_name = element.attrib.get('MessageName')
        self.description = element.attrib.get('Description')
        self.rank = element.attrib.get('Rank')
        self.primary_entity = element.attrib.get('PrimaryEntityName')
        self.stage = element.attrib.get('Stage')
        self.images = self.__load_images()

    def __load_images(self: object) -> list:
        images = []
        for image in self.element.getiterator(Step.image_tag):
            images.append(Image(image))
        return images

    def __str__(self):
        string = 2 * '\t' + f'Message name: {self.message_name}\n'
        string += 2 * '\t' + f'Descirption: {self.description}\n'
        string += 2 * '\t' + f'Rank: {self.rank}\n'
        string += 2 * '\t' + f'Primary entity: {self.primary_entity}\n'
        string += 2 * '\t' + f'Stage: {self.stage}\n'
        for i, image in enumerate(self.images):
            string += 3 * '\t' + f'IMAGE-{i + 1}'.center(50, '-') + '\n'
            string += image.__str__() + '\n'
        return string
