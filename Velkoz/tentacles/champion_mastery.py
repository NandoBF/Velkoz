from .common import RiotApiService

class ChampionMasteryApi(RiotApiService):

    def get_all_masteries(
        self,
        parameters:dict
    ):
        necessary_parameters = {}
        needed_parameters = {'region', 'puuid'}
        are_param_valid = self._validate_parameters(parameters, necessary_parameters, needed_parameters)
        
        if not are_param_valid: return self._handle_error('Incorrect Parameters')
        
        region = parameters['region'].lower()
        puuid = parameters['puuid']
        try:
            url =f'https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}' 
            return self._get(url=url, parameters=parameters)

        except requests.exceptions.APINotFoundError as error:
            return error

    
    def get_mastery(
        self,
        parameters:dict
    ):
        necessary_parameters={}
        needed_parameters={'puuid', 'championId', 'region'}
        are_param_valid = self._validate_parameters(parameters, necessary_parameters, needed_parameters)
        
        if not are_param_valid: return self._handle_error('Incorrect Parameters')
        region = parameters['region'].lower()
        puuid = parameters['puuid']
        championId = parameters['championId']
        try:
            url = f'https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{championId}'

            return self._get(url=url, parameters=parameters)

        except requests.exceptions.APINotFoundError as error:
            return error

    def get_top_masteries(
        self,
        parameters:dict
    ):
        necessary_parameters = {}
        needed_parameters = {'puuid', 'region', 'query'}
        are_param_valid = self._validate_parameters(parameters, necessary_parameters, needed_parameters)
        
        if not are_param_valid: return self._handle_error('Incorrect Parameters')
        
        query = parameters['query']
        if 'count' not in query:
            query_params = ''
        else:
            value = query['count']
            query_params = f'?count={value}'

        region = parameters['region'].lower()
        puuid = parameters['puuid']
        try:
            url = f'https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top{query_params}'
 
            return self._get(url=url, parameters=parameters)

        except requests.exceptions.APINotFoundError as error:
            return error

    def get_masteryscore(
        self,
        parameters:dict
    ):
        necessary_parameters = {}
        needed_parameters = {'puuid', 'region'}
        are_param_valid = self._validate_parameters(parameters, necessary_parameters, needed_parameters)
        
        if not are_param_valid: return self._handle_error('Incorrect Parameters')
       
        puuid = parameters['puuid']
        region = parameters['region'].lower()
        try:
            url = f'https://{region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-puuid/{puuid}'

            return self._get(url=url, parameters=parameters)

        except requests.exceptions.APINotFoundError as error:
            return error





