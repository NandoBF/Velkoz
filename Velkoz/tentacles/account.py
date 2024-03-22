from .common import RiotApiService

class AccountApi(RiotApiService):

    def get_account(
            self, parameters:dict):
        necessary_parameters = {'puuid', 'riotId'}
        needed_parameters = {'routing'}
        #Checks if the given parameters are valid for this function
        are_param_valid = self._validate_parameters(parameters, necessary_parameters, needed_parameters)
        if not are_param_valid: return self._handle_error('Incorrect Parameters')

        if 'riotId' in parameters:
            riotid = parameters['riotId'].split('#', 1)
            routing = parameters['routing']
            url = f'https://{routing.lower()}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riotid[0]}/{riotid[1]}'
        elif 'puuid' in parameters:
            puuid = parameters['puuid']
            routing = parameters['routing']
            url = f'https://{routing.lower()}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}'
        else:
            raise Exception ('HOW DID WE GET HERE LMAO')

        try:
            return self._get(url=url, parameters=parameters)
        except requests.exceptions.APINotFoundError as error:
            return error

