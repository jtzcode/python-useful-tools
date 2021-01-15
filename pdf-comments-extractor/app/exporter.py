from abc import ABCMeta, abstractmethod
import os, io

class Exporter(metaclass=ABCMeta):
    def __init__(self, notes_data, name="Exporter"):
        self.name = name
        self.notes_data = notes_data

    @abstractmethod
    def run(self):
        pass

class FileExporter(Exporter):
    def __init__(self, notes_data, output_file, type="text"):
        super().__init__(notes_data, "FileExporter")
        self.type = type
        self.output_file = output_file

    def run(self):
        if self.type == 'text':
            if (self.validate_file('.txt')):
                with io.open(self.output_file, 'w', encoding="utf8") as result_file:
                    for note in self.notes_data:
                        result_file.write(note + '\n')
            else:
                raise Exception('Invalid ouput file.')
        elif self.type == 'csv':
            pass
    
    def validate_file(self, target_ext):
        return os.path.isfile(self.output_file) and self.output_file.endswith(target_ext)
    


class CloudExporter(Exporter):
    def __init__(self, notes_data, token, type="yinxiang"):
        super().__init__(notes_data, "CloudExporter")
        self.type = type
        self.token = token

    def run(self):
        pass
