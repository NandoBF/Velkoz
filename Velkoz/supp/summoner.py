
# DO NOT FORGET THE DOTS!!!!!!
from tentacles import (SummonerApi, RiotApiService, api_key) 

from eye import Summoner

service = RiotApiService(api_key)


def _get_summonerDto_by_account(service, account:dict, region:str = 'euw1'):
    parameters = {'puuid' : account['puuid'], 'region': region}
    summonerDto = SummonerApi.get_summoner(service, parameters)
    return summonerDto


def _get_summoner_by_account(service, account:dict, region:str = 'euw1'):
    parameters = {'puuid': account['puuid'], 'region' : region}
    summonerDto = SummonerApi.get_summoner(service, parameters)
    return Summoner(summonerDto)

def _get_summoner_by_summonerName(service, summonerName:str, region:str = 'euw1'):
    parameters = {'summonerName': summonerName, 'region': region}
    summonerDto = SummonerApi.get_summoner(service,parameters)
    return Summoner(summonerDto)

def _get_summoner_by_summonerId(service, summonerId:str, region:str = 'euw1'):
    parameters = {'summonerId': summonerId, 'region': region}
    summonerDto = SummonerApi.get_summoner(service, parameters)
    return Summoner(summonerDto)


def _get_summoner_by_parameters(service, parameters):
    summonerDto = SummonerApi.get_summoner(service, parameters)
    return Summoner(summonerDto)



def _request_on_summoner_by_riotId(riotId:str, routing:str = 'europe',region:str = 'euw1', request={'summonerLevel'}):
    account = _get_account_by_riotId(riotId, routing) 
    summonerDto = _get_summonerDto_by_account(account, region)
    summoner = Summoner(summonerDto)
    summoner_data = summoner.request({'data':request})
    return summoner_data



