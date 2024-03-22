import requests



class RiotApiService():
    #This class needs error handling
    def __init__(
        self,
        api_key:str
    ):
        self.api_key = api_key
        self._headers = {"X-Riot-Token":api_key}
    
    def _validate_parameters(
        self,
        parameters:dict,
        necessary_parameters:dict = {}, #ONE OF THESE
        needed_parameters:dict = {} #ALL OF THESE

    ):
        #Returns True if parameters has at least one of the required parameters
        #If it doesn't return False.
        #Prevents a lot of errors that might occur due to incorrect syntax
        necessary = False
        needed = True
        for param in necessary_parameters:
            if param in parameters:
                necessary = True
        if necessary_parameters == {}: necessary = True
        for param in needed_parameters:
            if param not in parameters:
                needed = False
        if needed_parameters == {}: needed = True
        return (necessary and needed)
    

    def _set_defaults(
        self,
        parameters:dict
    ):
        # transforms the 'query' element of parameters from a dictionary
        # to a string for the url
        query = parameters['query']
        query_params = 'ids?'

        if 'startTime' not in query:
            query_params += ''
        else:
            value = query['startTime']
            query_params += f'startTime={value}&'

        if 'endTime' not in query:
            query_params += ''
        else:
            value = query['endTime']
            query_params += f'endTime={value}&'

        if 'queue' not in query:
            query_params += ''
        else:
            value = query['queue']
            query_params += f'queue={value}&'

        if 'type' not in query:
            query_params += ''
        else:
            value = query['type']
            query_params += f'type={value}&'
        
        if 'start' not in query:
            query_params += 'start=0&'
        else:
            value = query['start']
            query_params += f'start={value}&'

        if 'count' not in query:
            query_params += f'count=20'
        else:
            value = query['count']
            query_params += f'count={value}'

        parameters['query'] = query_params
        return parameters


    def _get(
        self,
        url:str,
        parameters: dict
    ):
        request = RiotApiRequest(
            service=self,
            url=url,
            parameters=parameters
        )
        try:
            return request()
        except requests.exceptions.HTTPError as errh:
            return (f'HTTPError - {errh.args[0]}')
    
    def _handle_error(
        self,
        error
    ):
        if error == 'Incorrect Parameters':
            return f'Detected error: {error}.'
        else:
            return f'Raised exception: {error}'



class RiotApiRequest(object):
    #This class needs error handling based on the riot api error codes
    def __init__(
        self,
        service: RiotApiService,
        url:str,
        parameters:str
    ):
        self.service = service
        self.url = url
        self.parameters = parameters


    def __call__(self):
        try:
            header = self.service._headers
            response = requests.get(self.url, headers=header)
            if response.status_code == 200:
                return response.json()
            else:
                return self._handle_errorcode(response.status_code)

        except requests.exceptions.InvalidHeader as error:
            print(f'Invalid Header')
            return(self.service._headers)
        except requests.exceptions.HTTPError as errh:
            print(f'HTTPError - {errh.args[0]}')
            return self._retry_request_on_error(errh)
    
    def _retry_request_on_error(self, errh):
        print(errh)
        #since I do not know how it reports the error it will stay unhandled for now
        
    def _handle_errorcode(self, code):
        if code == 400:
            return (f'Request failed with status code {code}: Bad request')
        elif code == 403:
            return (f'Request failed with status code {code}: Forbidden')
        elif code == 429:
            return (f'Request failed with status code {code}: Rate Limit Exceeded')

        


if __name__ == '__main__':
    pass
