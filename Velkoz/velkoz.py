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

#CHANGE THIS
#ERROR HANDLING FOR INVALID API_KEY
service = RiotApiService(api_key)

def _initialize_service(api_key=api_key):
    return RiotApiService(api_key) # Service should be initiated in the needed file


###############
# Get Account #
###############


def _get_account_by_riotId(riotId:str, routing:str = 'europe'):
    parameters = {'riotId': riotId, 'routing' : routing}
    accountDto = AccountApi.get_account(service, parameters)
    account = Account(accountDto)
    return account

def _get_account_by_parameters(parameters:dict):
    accountDto = AccountApi.get_account(service, parameters)
    account = Account(accountDto)
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
# Get Match #
#############

def _get_matchDto_by_parameters(parameters:dict):
    matchDto = MatchApi.get_matchDto(service, parameters)
    return matchDto



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
    account = _get_account_by_parameters(parameters)
    return account

'''
Function to get summoner
Usage: Must be provided with a riotId, summonerName or summonerId. Having priority in the order they were mentioned here. Region parameter defualts to 'euw1', but should be changed if the summoner you are looking for is not from the euw server.
'''
def get_summoner(riotId:str = '\0', summonerName:str = '\0', summonerId:str = 0, region:str = 'euw1'):
    
    if riotId != '\0':
        account = _get_account_by_riotId(riotId)
        parameters = {'puuid' : account.puuid}

    elif summonerName != '\0':
        parameters = {'summonerName': summonerName}

    elif summonerId != 0:
        parameters = {'summonerId' : summonerId}

    else:
        raise Exception ('Error getting summoner. Please provide a riotId, summonerName or summonerId')

    parameters['region'] = region
    summoner = _get_summoner_by_parameters(parameters)
    return summoner



'''
Function to get a list of matches given a riotId or puuid
needs more arguments, possibly use args to get the query
returns an array with the match ids
'''
def get_match_list(riotId:str = '\0', puuid:str = '\0', routing:str = 'europe', count:int = 20):
    
    if riotId != '\0':
        account = _get_account_by_riotId(riotId) 
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
    matchDto = _get_matchDto_by_parameters(parameters)
    match = Match(matchDto)
    return match


#############
# DEBUGGING #
#############

if __name__ == '__main__':
    # match_list = get_match_list('Princess#060')
    # last_match_id = match_list[0]
    # match = get_match(last_match_id)
    # participant = match.get_participant(riotId = 'Princess#060')
    # print(participant.win)
    pass
