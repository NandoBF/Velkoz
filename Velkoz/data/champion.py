from .common import (
    RiotJson,
    DdragonRequest

        )


class Champion(RiotJson):

    def __init__(self, **kwargs):
        self.request = kwargs.get('ddragon', None)
        dto = kwargs.get('dto', None)
        RiotJson.__init__(self, dto)
        self.champ = kwargs.get('champion', None)
        self.championDto = self.data.get(self.champ, None)
        self._general(self.championDto)
   
    def _general(self, Dto:dict):
        self.id = Dto.get('id', self.champ)
        self.key = Dto.get('key', None)
        self.name = Dto.get('name', None)
        self.title = Dto.get('title', None)

        self.image = Dto.get('image', None)

        #func to skins
        self._set_skins(Dto.get('skins', None))
        #func to tips
        self.tags = Dto.get('tags', None)
        self.partype = Dto.get('partype', None) #Resource?
        self.info = Dto.get('info', None)
        self.stats = Dto.get('stats', None)
        self.spells = Dto.get('spells', None)
        self.passive = Dto.get('passive', None)
        self.recommended = Dto.get('recommended', None) #what even is this

    def _set_skins(self, skinsArray):
        self.skins = Skins(champion=self.champ, request=self.request, skinsArray=skinsArray) 

    

class Skins(Champion):
   
    def __init__(self, **kwargs):
        self.request = kwargs.get('request',None)
        self.champion= kwargs.get('champion',None)
        self.all = kwargs.get('skinsArray', [])
        self.skinNum = len(self.all)
       
    def _handleIndexError(self):
        raise Exception ('This champion does not have that many skins :(')


    def _get_img(self, get_type, number):
        try:
            skinNumber = self.all[number].get('num', 0)
            return self.request._get_champion_image(get_type=get_type, champion=self.champion, num=skinNumber)
        except IndexError:
            self._handleIndexError()

    def get_splash(self,number):
        return self._get_img('splash',number)

    def get_loading(self,number):
        return self._get_img('loading',number) 

    def get_centered(self,number):
        return self._get_img('centered',number)

    def get_tile(self,number):
        return self._get_img('tiles',number)
    
    def skin(self, number):
        try:
            return self.all[number]
        except IndexError:
            self._handleIndexError()


    def __str__(self):
        return (f'{self.champion} has {self.skinNum - 1} skins')
        


