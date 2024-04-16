import json
from PIL import Image as ImageLoader
from PIL.Image import Image
from io import BytesIO


version = '14.7.1'
language = 'en_US'

class DdragonRequest():

    def __init__(self, **kwargs):
        self.ddragon_path = kwargs.get('ddragon_path', None)
  

    def _get_data(self, **kwargs):
        get_type = kwargs.get('get_type', None)

        match get_type:
            case 'champion':
                champ = kwargs.get('champion', None)
                path = f'{self.ddragon_path}/{version}/data/{language}/champion/{champ}.json'
                file=open(path,'r')
                champion_data = json.load(file)
                return champion_data
            
            case 'item':
                path = f'{self.ddragon_path}/{version}/data/{language}/item.json'
                file=open(path,'r')
                item_data = json.load(file)
                return item_data
            
            case _:
                raise Exception ('Invalid data type')
            

    def _get_champion_image(self, **kwargs):
        get_type = kwargs.get('get_type', 'splash')
        num = kwargs.get('num', 0)
        champ = kwargs.get('champion', 'Aatrox')
        path = f'{self.ddragon_path}/img/champion/{get_type}/{champ}_{num}.jpg'
        with open(path, 'rb') as image:
            f = image.read()
            b = bytearray(f)
        return ImageLoader.open(BytesIO(b))
        # return data


class RiotJson():

    def __init__(self, Dto):
        self.type = Dto.get('type', None)
        self.format = Dto.get('format', None)
        self.version = Dto.get('version', None)
        self.data = Dto.get('data', None)


    



        
