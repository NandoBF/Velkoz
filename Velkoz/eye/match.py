

class Match():

    def __init__(self, matchDto:dict):
        self.metadataDto = matchDto['metadata']
        self.infoDto = matchDto['info']
        self._define_metadata(self.metadataDto)
        self._define_info(self.infoDto)


    def _define_metadata(self, metadata:dict):
        self.version = metadata['dataVersion']
        self.matchId = metadata['matchId']
        self.participants = metadata['participants']

    def _define_info(self, kwargs):
        self.creation = kwargs.get('gameCreation', None)
        self.duration = kwargs.get('gameDuration', None)
        self.end = kwargs.get('gameEndTimestamp', None)
        self.gameId = kwargs.get('gameId', None)
        self.gameMode = kwargs.get('gameMode', None)
        self.start = kwargs.get('gameStartTimestamp', None)
        self.gameType = kwargs.get('gameType', None)
        self.mapId = kwargs.get('mapId',None)
        self.platformId = kwargs.get('platformId', None)
        self.queueId = kwargs.get('queueId', None)
        self.teams = kwargs.get('teams', None)
        self.tournamentCode = kwargs.get('tournamentCode', None)
        self.gameVersion = kwargs.get('gameVersion', None)
    
    def _get_participant_by_puuid(self, puuid:str):
        i = 0
        while (i<10):
            if self.participants[i] == puuid:
                return i
            else: i += 1
        raise Exception ('Participant not found.')


    def _get_participant_by_riotId(self, riotId:str):
        i = 0
        while (i < 10):
            riotName = self.infoDto['participants'][i].get('riotIdGameName', None)
            tagline = self.infoDto['participants'][i].get('riotIdTagline', None)
            if riotId == f'{riotName}#{tagline}': return i
            else: i += 1
        raise Exception ('Participant not found.')
    

    def get_participant(self, index:int = 0, puuid:str = '\0', riotId:str = '\0'):
        if puuid != '\0':
            i = self._get_participant_by_puuid(puuid)
        
        elif riotId != '\0':
            i = self._get_participant_by_riotId(riotId)

        else:
            #when index is provided 
            i = index
            if index < 0 or index > len(self.participants) + 1:
                raise Exception ('Invalid index')

        return Participant(self.infoDto['participants'][i])
    



class Participant():

    def __init__(self, kwargs):
        self.participantDto = kwargs
        self.assists = kwargs.get('assists', None)
        self.baronKills = kwargs.get('baronKills', None)
        self.bountyLevel = kwargs.get('bountyLevel', None)
        self.champExperience = kwargs.get('champExperience', None)
        self.champLevel = kwargs.get('champLevel', None)
        self.championId = kwargs.get('championId', None) #Prior to 11.4 could give errors
        self.championName = kwargs.get('championName', None)
        self.championTransform = kwargs.get('championTransform', None) #Only applicable to Kayn
        self.consumablesPurchased = kwargs.get('consumablesPurchased', None)
        self.damageDealtToBuildings = kwargs.get('damageDealtToBuildings', None)
        self.damageDealtToObjectives = kwargs.get('damageDealtToObjectives', None)
        self.damageDealtToTurrets = kwargs.get('damageDealtToTurrets',None)
        self.deaths = kwargs.get('deaths', None)
        self.detectorWardsPlaced = kwargs.get('detectorWardsPlaced', None)
        self.doubleKills = kwargs.get('doubleKills', None)
        self.dragonKills = kwargs.get('dragonKills', None)
        self.firstBloodKill = kwargs.get('firstBloodKill', None)
        self.firstTowerKill = kwargs.get('firstTowerKill', None)
        self.gameEndedInEarlySurrender = kwargs.get('gameEndedInEarlySurrender', None)
        self.gameEndedInSurrender = kwargs.get('gameEndedInSurrender', None)
        self.goldEarned = kwargs.get('goldEarned', None)
        self.goldSpent = kwargs.get('goldSpent', None)
        self.position = kwargs.get('teamPosition', None) #could also use individualPosition
        self.inhibitorKills = kwargs.get('inhibitorKills', None)
        self.inhibitorsLost = kwargs.get('inhibitorsLost', None)
        #Items to array
        i = 0
        items = []
        while i < 7:
            items.append(kwargs.get(f'item{i}', None))
            i += 1
        ##
        self.kills = kwargs.get('kills', None)
        self.lane = kwargs.get('lane', None)
        self.largestMultiKill = kwargs.get('largestMultiKill', None)
        self.longestTimeSpentLiving = kwargs.get('longestTimeSpentLiving', None)
        self.magicDamageDealtToChampions = kwargs.get('magicDamageDealtToChampions', None)
        self.magicDamageTaken = kwargs.get('magicDamageTaken', None)
        self.cs = kwargs.get('neutralMinionsKilled', None)
        self.objectivesStolen = kwargs.get('objectivesStolen', None)
        self.id = kwargs.get('participantId', None)
        self.pentaKills = kwargs.get('pentaKills', None)
        self.physicalDamageDealtToChampions = kwargs.get('physicalDamageDealtToChampions', None)
        self.physicalDamageTaken = kwargs.get('physicalDamageTaken', None)
        self.profileIcon = kwargs.get('profileIcon', None)
        self.puuid = kwargs.get('puuid', None)
        self.quadraKills = kwargs.get('quadraKills', None)
        try:
            self.riotId = (kwargs.get('riotIdGameName', None) + '#' + kwargs.get('riotIdTagline', None))
        except:
            self.riotIdName = kwargs.get('riotIdGameName', None)
            self.riotIdTagline = kwargs.get('riotIdTagline', None)
        self.role = kwargs.get('role', None)
        self.sightWardsBoughtInGame = kwargs.get('sightWardsBoughtInGame', None)
        self.Qcasts = kwargs.get('spell1Casts', None)
        self.Wcasts = kwargs.get('spell2Casts', None)
        self.Ecasts = kwargs.get('spell3Casts', None)
        self.Rcasts = kwargs.get('spell4Casts', None)
        self.Dcasts = kwargs.get('summoner1Casts', None)
        self.Fcasts = kwargs.get('summoner2Casts', None)
        self.Did = kwargs.get('summoner1Id', None)
        self.Fid = kwargs.get('summoner2Id', None)
        self.summonerLevel = kwargs.get('summonerLevel', None)
        self.summonerName = kwargs.get('summonerName', None)
        self.teamId = kwargs.get('teamId', None)
        self.timeCCingOthers = kwargs.get('timeCCingOthers', None)
        self.timePlayed = kwargs.get('timePlayed', None)
        self.totalDamageDealtToChampions = kwargs.get('totalDamageDealtToChampions', None)
        self.totalDamageTaken = kwargs.get('totalDamageTaken', None)
        self.totalHeal = kwargs.get('totalHeal', None)
        self.totalHealsOnTeammates = kwargs.get('totalHealsOnTeammates', None)
        self.totalTimeCCDealt = kwargs.get('totalTimeCCDealt', None)
        self.totalTimeSpentDead = kwargs.get('totalTimeSpentDead', None)
        self.tripleKills = kwargs.get('tripleKills', None)
        self.trueDamageDealtToChampions = kwargs.get('trueDamageDealtToChampions', None)
        self.unrealKills = kwargs.get('unrealKills', None)
        self.visionScore = kwargs.get('visionScore', None)
        self.wardsKilled = kwargs.get('wardsKilled', None)
        self.win = kwargs.get('win', None)
   
    
    #this function can be used to get any key of participantDto that has not been defined above
    def get(self, parameter:str): 
        return self.participantDto.get(parameter, None)












