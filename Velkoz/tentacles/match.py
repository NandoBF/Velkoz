from .config import api_key ## debug only
from .common import RiotApiService

class MatchApi(RiotApiService):

    def get_match_list(
        self,
        parameters:dict
    ):
        necessary_parameters = {'puuid'}
        needed_parameters = {'routing', 'query'}
        are_param_valid = self._validate_parameters(parameters, necessary_parameters, needed_parameters)
        if not are_param_valid: return self._handle_error('Incorrect Parameters')
 
        parameters = self._set_defaults(parameters)
        routing = parameters['routing'].lower()
        puuid = parameters['puuid']
        query = parameters['query']
        try:
            url = f'https://{routing}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/{query}'

            return self._get(url=url, parameters=parameters)

        except requests.exceptions.APINotFoundError as error:
            return error


    # Will have to handle all the info in match accordingly
    def get_match(
        self,
        parameters:dict
    ):
        necessary_parameters = {'matchId'}
        needed_parameters = {'routing'}
        are_param_valid = self._validate_parameters(parameters, necessary_parameters, needed_parameters)
        if not are_param_valid: return self._handle_error('Incorrect Parameters')
 

        routing = parameters['routing'].lower()
        matchId = parameters['matchId']

        try:
            url = f'https://{routing}.api.riotgames.com/lol/match/v5/matches/{matchId}'
            return self._get(url=url, parameters=parameters)

        except requests.exceptions.APINotFoundError as error:
            return error



if __name__ == '__main__':
    service = RiotApiService(api_key=api_key)
    parameters = {'puuid': 'AD2f5GhQOeuMeJ_XAle6mfO1sPqrHeru0qGpri3vJGoS3bO22_iUWW2JtRP3CkefhPhtolDSvfUdhg', 'routing': 'EUROPE', 'query' : {}}
    parameters1 = {'matchId':'EUW1_6860598923', 'routing': 'europe'}
    print(MatchApi.get_match_list(service, parameters))
   



