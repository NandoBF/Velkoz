
# Velkoz
Velkoz is a python package that allows you to easily use Riot Games public api and their database DDragon.
It is currently focused only on League of Legends and does not support Valorant or any other games.

Current Velkoz version: 0.1.0


## Instalation

Install Velkoz using python pip

```bash
  pip install Velkoz
```

## Use/Example
To use Velkoz first import it using python and set your Riot Games api key.
If you still do not have an api key you can get one on Riot Games developer portal: https://developer.riotgames.com/

```python
  import Velkoz as vel
  vel.set_api_key('YOUR_API_KEY')
```
If you require or want to use DDragon you will have to manually download it and set the path to its folder using
```python
  vel.set_ddragon('PATH_TO_DDRAGON')
```
After this you're ready to go! For more functions I recommend you reading the documentation below.



## Documentation


#### Get a summoners account
```python
  vel.get_account(riotId,puuid,routing)
```

| Parameter   | type       | Description                          |
| :---------- | :--------- | :---------------------------------- |
| `riotId` | `string` | **Optional.** The summoners riot id |
| `puuid` | `string` | **Optional.** The summoners puuid |
| `routing` | `string` | **Optional.** The summoners server |
| | | You need to provide a riotId or a puuid

* Returns an account

#### Get a summoner
```python
  vel.get_summoner(riotId=,summonerName,summonerId,region)
```

| Parameter   | type       | Description                         |
| :---------- | :--------- | :---------------------------------- |
| `riotId` | `string` | **Optional.** The summoners riot id |
| `summonerName` | `string` | **Optional.** The summoners name* |
| `summonerId` | `string` | **Optional.** The summoners id |
| `region` | `string` | **Optional.** The summoners region |
| | | You need to provide a riotId, summonerId or summonerName

* **For accounts created before Riot's summoner name changes, the summoner name can be different from their riotId**
* Returns a summoner

#### Get list of recent matches ids
```python
  vel.get_match_list(riotId,puuid,routing, matches_count)
```
| Parameter   | type       | Description                          |
| :---------- | :--------- | :---------------------------------- |
| `riotId` | `string` | **Optional.** The summoners riot id |
| `puuid` | `string` | **Optional.** The summoners puuid |
| `routing` | `string` | **Optional.** The summoners server |
| `matches_count` | `integer(max 100)` | **Optional.** The number of matches to get|
| | | You need to provide a riotId or a puuid

* Returns an array of match ids

#### Get a matches details
```python
  vel.get_match(matchId, routing)
```

| Parameter   | type       | Description                          |
| :---------- | :--------- | :---------------------------------- |
| `matchId` | `string` | **Mandatory** The match id |
| `routing` | `string` | **Optional.** The matches server |

* Returns a match

# UNFINISHED DOCUMENTATION
