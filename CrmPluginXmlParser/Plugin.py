from Step import Step

class Plugin:

    step_tag = '{http://schemas.microsoft.com/crm/2011/tools/pluginregistration}Step'

    def __init__(self: object, element: object) -> None:
        self.element = element
        self.friendly_name = element.attrib.get('FriendlyName')
        self.description = element.attrib.get('Description')
        self.steps = self.__load_steps()
        

    def __load_steps(self) -> list:
        steps = []
        for step in self.element.getiterator(Plugin.step_tag):
            steps.append(Step(step))
        return steps


    def __str__(self) -> str:
        string = f"{str(self.friendly_name).center(100, '/')}\n\n"
        string += f'Friendly name: {self.friendly_name}\nDescription: {self.description}\n\n'
        for i, step in enumerate(self.steps):
            string += 1 * '\t' + f'STEP-{i + 1}'.center(75, '*') + '\n'
            string += step.__str__() + 2 * '\n'
        return string
        



