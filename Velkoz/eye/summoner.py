
class Summoner():
    
    def __init__(self, summonerDto:dict):
        self.summonerDto = summonerDto
        self.id = summonerDto['id']
        self.accountId = summonerDto['accountId']
        self.puuid = summonerDto['puuid']
        self.name = summonerDto['name']
        self.profileIcon = summonerDto['profileIconId']
        self.revisionDate = summonerDto['revisionDate']
        self.level = summonerDto['summonerLevel']

    def _save_summoner(self, author):
        print(f'Summoner saved with author {author}(actually did nothing)')


    def _validate_data_request(self,data_request:dict):
        for item in data_request:
            if item not in self.summonerDto:
                return 'Request for invalid data'
            
    #Gets specific data from summonerDto
    def _get_data(self,data_request:dict):
        
        self._validate_data_request(data_request)
        
        answer_data = []
        for item in data_request:
            answer_data.append(self.summonerDto[item])
        return answer_data


    def request(self, requests:dict):
        to_return = 'Requests have been met'
        for request in requests:
            if request == 'data':
                to_return = self._get_data(requests['data'])
            elif request == 'save':
                self._save_summoner(requests['save'])
            else:
                return 'invalid request'

        return to_return


if __name__ == '__main__':

    summonerDto ={'id': 'Cdp1KXJgqkSMIMwwhuxkv3_YfUfwNW_9n9gcwbE1mfkhrIc', 'accountId': 'xGsuWPAHONj6AuzPQk2sdjcWIuxnOoUE5qNXQHhDjUnu5so', 'puuid': 'AD2f5GhQOeuMeJ_XAle6mfO1sPqrHeru0qGpri3vJGoS3bO22_iUWW2JtRP3CkefhPhtolDSvfUdhg', 'name': 'Zemiranda04', 'profileIconId': 5495, 'revisionDate': 1710790106920, 'summonerLevel': 121}
    
    requests = {'data':{'name', 'summonerLevel'}, 'save': 'diogo'}
    sumo = Summoner(summonerDto)
    answer = sumo.request(requests)
    print(answer)
