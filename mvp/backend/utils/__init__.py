from stringcase import spinalcase, snakecase

class Utils:
            
    def convert_spinalcase(self, object):
        new_object = {}
        for key in object:
            new_object[spinalcase(key)] = object[key]

        return new_object
    

    def convert_snakecase(self, object):
        new_object = {}
        for key in object:
            new_object[snakecase(key)] = object[key]

        return new_object

    def convert_data_to_array(self, data):
        new_data = {}

        for key in data:
            new_data[snakecase(key)] = [data[key]]

        return new_data