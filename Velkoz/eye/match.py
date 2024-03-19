

class Match():

    def __init__(self, matchDto):
        self.matchDto = matchDto


    def _get_metadata(metadata_request:dict):
        pass
    

    def request(self, requests:dict):
        to_return = {}
        for request in requests:
            if request == 'metadata':
                to_return['metadata'] = self._get_metadata(request['metadata'])

            elif request == 'info':
                self._get_info(request['info'])

            else:
                return f'Invalid request for {request}'


        
