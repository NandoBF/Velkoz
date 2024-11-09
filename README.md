
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

Unfortunately I haven't made a proper Documentation yet :(
