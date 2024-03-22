
class Account():

    def __init__(self, accountDto:dict):
        self.accountDto = accountDto
        self.puuid = accountDto['puuid']
        if 'gameName' in accountDto:
            self.gameName = accountDto['gameName']
        if 'tagLine' in accountDto:
            self.tagLine = accountDto['tagLine']
            try:
                self.riotId = self.gameName + '#' + self.tagLine
            except:
                self.riotId = ''

    def save(self, author):
        print('saved account')
