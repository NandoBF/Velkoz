import requests

from config import api_key






def account_by_riotid(riotid, routing="europe", api_key=api_key):
   riot_id = riotid.split('#',1)
   api_url = f'https://{routing.lower()}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id[0]}/{riot_id[1]}' + '?api_key=' + api_key
   response = requests.get(api_url)
   return response.json()



def summoner_by_puuid(puuid, server='euw1', api_key=api_key):
    api_url = f'https://{server}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}' + '?api_key=' + api_key
    response = requests.get(api_url)
    return response.json()



def summoner_by_riotid(riotid, routing='europe',server='euw1', api_key=api_key):
    account = account_by_riotid(riotid,routing, api_key)
    account_puuid = account['puuid']
    return summoner_by_puuid(account_puuid,server,api_key)

if __name__ == '__main__':
    print(summoner_by_riotid("Romans 8 11#06020"))
