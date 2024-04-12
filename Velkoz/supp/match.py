
from Velkoz.tentacles import (MatchApi)

from Velkoz.eye import Match


#############
# Get Match #
#############

def _get_matchDto_by_parameters(service, parameters:dict):
    matchDto = MatchApi.get_matchDto(service, parameters)
    return matchDto


