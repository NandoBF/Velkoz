
from Velkoz.tentacles import (ChampionMasteryApi)

from Velkoz.eye import (ChampionMastery)


def _get_all_masteries_by_puuid(service, puuid:str, region:str = 'euw1'):
    parameters = {'puuid':puuid, 'region':region}
    championMasteryDto = ChampionMasteryApi.get_all_masteries(service, parameters)
    return championMasteryDto


def _get_champion_mastery(service, puuid:str, championId:int, region:str = 'euw1'):
    parameters = {'puuid':puuid, 'championId':championId, 'region':region}
    championMasteryDto = ChampionMasteryApi.get_mastery(service, parameters)
    championMastery = ChampionMastery(championMasteryDto)
    return championMastery


def _get_top_masteries(service, puuid:str, query:dict = {}, region:str = 'euw1'):
    parameters = {'puuid':puuid, 'region':region, 'query': query}
    championMasteryDto = ChampionMasteryApi.get_top_masteries(service, parameters)
    return championMasteryDto

def _get_masteryscore(service, puuid:str, region:str = 'euw1'):
    parameters = {'puuid':puuid, 'region':region}
    masteryscore = ChampionMasteryApi.get_masteryscore(service, parameters)
    return masteryscore


