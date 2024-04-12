from .tentacles import ( #dont forget the dots
    AccountApi,
    SummonerApi,
    api_key,
    RiotApiService,
    MatchApi
    )

from .eye import ( #dont forget the dots
    Summoner,
    Match,
    Participant,
    Account
        )

from .supp import ( #dont forget the dots
    summoner as summ,
    account as acc,
    match as mat,
    champion_mastery as mastery

        ) 

#CHANGE THIS
#ERROR HANDLING FOR INVALID API_KEY

def set_api_key(api_key:str):
    global service
    service = RiotApiService(api_key)


def _initialize_service(api_key=api_key):
    return RiotApiService(api_key) # Service should be initiated in the needed file




def _handle_missing_parameters(request:str):

    raise Exception (f'Error fulfilling request {request}. Make sure you are passing the correct arguments')




#for now only used in champion_mastery functions
def _get_puuid(puuid:str, riotId:str, routing:str = 'europe'):

    if puuid != '\0':
        return puuid
    elif riotId != '\0':
        account = get_account(riotId=riotId, routing=routing)
        return account.puuid
    else:
        _handle_missing_parameters('_get_puuid')



############
# Callable #
############



'''
Function to get account
Usage: Must be provided a riotId or puuid. If both are provided it will default to using riotId. Routing parameter defaults to 'europe' so it is optional, but it's recommended to provide it with the nearest routing to you.
'''
def get_account(riotId:str = '\0', puuid:str = '\0', routing:str = 'europe'):

    parameters = {}
    if riotId != '\0':
        parameters['riotId'] = riotId
    elif puuid != '\0':
        parameters['puuid'] = puuid
    else:
        raise Exception ('Error getting account. Please provide a riotId or puuid')

    parameters['routing'] = routing
    account = acc._get_account_by_parameters(service, parameters)
    return account

'''
Function to get summoner
Usage: Must be provided with a riotId, summonerName or summonerId. Having priority in the order they were mentioned here. Region parameter defualts to 'euw1', but should be changed if the summoner you are looking for is not from the euw server.
'''
def get_summoner(riotId:str = '\0', summonerName:str = '\0', summonerId:str = 0, region:str = 'euw1'):
    
    if riotId != '\0':
        account = acc._get_account_by_riotId(service, riotId)
        parameters = {'puuid' : account.puuid}

    elif summonerName != '\0':
        parameters = {'summonerName': summonerName}

    elif summonerId != 0:
        parameters = {'summonerId' : summonerId}

    else:
        raise Exception ('Error getting summoner. Please provide a riotId, summonerName or summonerId')

    parameters['region'] = region
    summoner = summ._get_summoner_by_parameters(service, parameters)
    return summoner



'''
Function to get a list of matches given a riotId or puuid
needs more arguments, possibly use args to get the query
returns an array with the match ids
'''
def get_match_list(riotId:str = '\0', puuid:str = '\0', routing:str = 'europe', count:int = 20):
    
    if riotId != '\0':
        account = acc._get_account_by_riotId(service, riotId) 
        parameters = {'puuid': account.puuid}

    elif puuid != '\0':
        parameters = {'puuid': puuid}

    parameters['routing'] = routing
    query = {'count' : count}
    parameters['query'] = query
    match_list = MatchApi.get_match_list(service, parameters)
    return match_list
        
'''
Function to get a Match by a matchId
Usage: Must be provided a matchId. Routing parameter is not necessary since it defaults to 'europe', but must be changed if the match is not from european servers.
'''

def get_match(matchId:str, routing:str = 'europe'):

    parameters = {'matchId' : matchId, 'routing': routing}
    matchDto = mat._get_matchDto_by_parameters(service, parameters)
    match = Match(matchDto)
    return match





####################
# Champion Mastery 
####################

def get_all_masteries(puuid:str = '\0', riotId:str = '\0', region = 'euw1', routing = 'europe'):
    
    new_puuid = _get_puuid(puuid, riotId, routing)

    return mastery._get_all_masteries_by_puuid(service, new_puuid, region = region)


def get_champion_mastery(puuid:str = '\0', riotId:str = '\0', championId:int = 1 ,region:str = 'euw1', routing:str = 'europe'):

    new_puuid = _get_puuid(puuid, riotId, routing)


    return mastery._get_champion_mastery(service=service, puuid = new_puuid, championId = championId,region = region)

def get_top_masteries(puuid:str = '\0', riotId:str = '\0', region:str = 'euw1', routing:str = 'europe', **kwargs):

    new_puuid = _get_puuid(puuid, riotId, routing)

    query = {}
    for key, value in kwargs.items():
        query[key] = value

    return mastery._get_top_masteries(service, puuid=puuid, query=query, region=region)


def get_masteryscore(puuid:str='\0', riotId:str='\0',region:str='euw1', routing:str='europe'):

    new_puuid = _get_puuid(puuid, riotId, routing)

    return mastery._get_masteryscore(service, puuid=new_puuid, region=region)





#############
# DEBUGGING #
#############

if __name__ == '__main__':
    pass 
