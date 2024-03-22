from .common import RiotApiService

class SummonerApi(RiotApiService):

    def get_summoner(
        self,
        parameters:dict
    ):
        necessary_parameters = {'puuid', 'summonerName', 'accountId'}
        needed_parameters = {'region'}
        are_param_valid = self._validate_parameters(parameters, necessary_parameters, needed_parameters)
        if not are_param_valid: return self._handle_error('Incorrect Parameters')

        region = parameters['region'].lower()
        
        # Summonerids are not supported because of potential blacklists
        if 'puuid' in parameters:
           puuid = parameters['puuid']
           url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}'
        
        elif 'summonerName' in parameters:
            summonerName = parameters['summonerName']
            url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}'
        
        elif 'accountId' in parameters:
            accountId = parameters['accountId']
            url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{accountId}' 


        else:
            return 'HOW DID WE EVEN GET HERE'


        try:
            return self._get(url=url, parameters=parameters)

        except requests.exceptions.APINotFoundError as error:
            return error


