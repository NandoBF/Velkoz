from Velkoz.data import (Champion, RiotJson)


def _get_splash(champ:Champion, number:int):
    splash = champ.skins.get_splash(number)
    return splash


def _get_loading(champ:Champion, number:int):
    loading = champ.skins.get_loading(number)
    return loading

