from win10toast import ToastNotifier
import requests

name = str(input("Enter FACEIT username:"))
url = 'https://open.faceit.com/data/v4/players?nickname={0}&game=csgo&access_token={token}'.format(name)
r = requests.get(url).json()

stats = {
    'name' : r['nickname'],
    'level' : r['games']['csgo']['skill_level'],
    'elo' : r['games']['csgo']['faceit_elo'],
    'region' : r['games']['csgo']['region'],
    'afk' : r['infractions']['afk'],
    'leave' : r['infractions']['leaver'],
    'membership' : r['membership_type']
}

toaster = ToastNotifier()
toaster.show_toast(stats['name'] + " - FACEIT Stats:","\nLevel: " + str(stats['level']) + " - Elo: " + str(stats['elo'])
                   + "\nCurrent Region: " + stats['region'] +
                   "\nAFK: " + str(stats['afk']) + " Times" +
                   " - Leaves: " + str(stats['leave']) + " Times" +
                   "\nMembership: " + stats['membership'],
                   icon_path="faceit.ico",duration=10)
