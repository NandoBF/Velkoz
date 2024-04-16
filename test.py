import Velkoz as vel
vel.set_api_key('RGAPI-dba809a2-6dcd-43e0-a4bd-6d23a1d85214')
vel.set_ddragon('Velkoz/ddragon')
#
# mlist = vel.get_match_list(riotId='Romans 8 11#06020', count = 3)
# match = vel.get_match(mlist[0])
# part = match.get_participant(riotId='Romans 8 11#06020')


aatrox = vel.get_champion('Aatrox')
image = vel.get_champ_image('Aatrox')
print(image)
