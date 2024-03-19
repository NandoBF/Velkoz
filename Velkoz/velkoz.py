from tentacles import (
    AccountApi,
    SummonerApi,
    api_key,
    RiotApiService
    )

from eye import (
    Summoner
        )

service = RiotApiService(api_key)

def _initialize_service(api_key=api_key):
    return RiotApiService(api_key) # Service should be initiated in the needed file


def _get_account_by_riotId(riotId:str, routing:str = 'europe'):
    parameters = {'riotId': riotId, 'routing' : routing}
    account = AccountApi.get_account(service, parameters)
    return account


def _get_summonerDto_by_account(account:dict, region:str = 'euw1'):
    parameters = {'puuid' : account['puuid'], 'region': region}
    summonerDto = SummonerApi.get_summoner(service, parameters)
    return summonerDto

################
# Get Summoner #
################


def _get_summoner_by_account(account:dict, region:str = 'euw1'):
    parameters = {'puuid': account['puuid'], 'region' : region}
    summonerDto = SummonerApi.get_summoner(service, parameters)
    return Summoner(summonerDto)

def _get_summoner_by_summonerName(summonerName:str, region:str = 'euw1'):
    parameters = {'summonerName': summonerName, 'region': region}
    summonerDto = SummonerApi.get_summoner(service,parameters)
    return Summoner(summonerDto)

def _get_summoner_by_summonerId(summonerId:str, region:str = 'euw1'):
    parameters = {'summonerId': summonerId, 'region': region}
    summonerDto = SummonerApi.get_summoner(service, parameters)
    return Summoner(summonerDto)


def _get_summoner_by_parameters(parameters):
    summonerDto = SummonerApi.get_summoner(service, parameters)
    return Summoner(summonerDto)

#############

def _request_on_summoner_by_riotId(riotId:str, routing:str = 'europe',region:str = 'euw1', request={'summonerLevel'}):
    account = _get_account_by_riotId(riotId, routing) 
    summonerDto = _get_summonerDto_by_account(account, region)
    summoner = Summoner(summonerDto)
    summoner_data = summoner.request({'data':request})
    return summoner_data


############
# Callable #
############


def get_summoner(riotId:str = '\0', summonerName:str = '\0', summonerId:str = 0, region:str = 'euw1'):
    
    if riotId != '\0':
        account = _get_account_by_riotId(riotId)
        parameters = {'puuid' : account['puuid']}

    elif summonerName != '\0':
        parameters = {'summonerName': summonerName}

    elif summonerId != 0:
        parameters = {'summonerId' : summonerId}

    else:
        raise Exception ('Error getting summoner. Please provide a method')

    parameters['region'] = region
    summoner = _get_summoner_by_parameters(parameters)
    return summoner



if __name__ == '__main__':

    hailey = get_summoner(riotId = 'Princess#060')
    diogo = get_summoner(riotId = 'Zemiranda04#EUW')
    danny = get_summoner(riotId = 'iDannuwu#EUW')
    nando = get_summoner(summonerName = 'NandoBF')
    print(diogo.id)
    print(hailey.level)
    print(danny.name)
    print(nando.level)
