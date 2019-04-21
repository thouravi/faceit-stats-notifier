from win10toast import ToastNotifier
import requests

name = str(input("Enter FACEIT username:"))
url = 'https://open.faceit.com/data/v4/players?nickname={0}&game=csgo&access_token=584bb8a8-8b74-4126-b7a8-d003d99f2d49'.format(name)
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
