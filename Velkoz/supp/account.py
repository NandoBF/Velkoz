from tentacles import (
    AccountApi

        )

from eye import (
    Account
        )


###############
# Get Account #
###############


def _get_account_by_riotId(service, riotId:str, routing:str = 'europe'):
    parameters = {'riotId': riotId, 'routing' : routing}
    accountDto = AccountApi.get_account(service, parameters)
    account = Account(accountDto)
    return account

def _get_account_by_parameters(service, parameters:dict):
    accountDto = AccountApi.get_account(service, parameters)
    account = Account(accountDto)
    return account

