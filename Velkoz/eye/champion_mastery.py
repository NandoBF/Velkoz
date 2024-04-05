
#useless?
class ChampionMastery():
    

    def __init__(self, kwargs):
        self.ChampionMasteryDto = kwargs
        self.chestGranted = kwargs.get('chestGranted' ,None)
        self.championId = kwargs.get('championId' ,None)
        self.lastPlayTime = kwargs.get('lastPlayTime', None)
        self.championLevel = kwargs.get('championLevel', None)
        self.championPoints = kwargs.get('championPoints', None)
        self.tokensEarned = kwargs.get('tokensEarned', None)

    def get(self, parameter):
        got = self.ChampionMasteryDto.get(parameter, None)

