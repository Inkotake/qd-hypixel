import requests
import re
import sys

from requests.api import get


url = input('url plz\n>>>')


def get_chaim(url: str,):
    if not 'hypixel' in url:
        print('Failed: Not a Hypixel url')
        sys.exit()
    print('Csrf loading... Speed depond on GFW')
    headers = {
        "referer": "https://rewards.hypixel.net/claim-reward/5d04951a",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "origin": "https://rewards.hypixel.net",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
    }
    hyp1_req = requests.get(url, headers=headers)
    re1 = re.search('''Token = "(.+)"''', hyp1_req.text)
    if 'error":"This link either never existed or has already expired.' in hyp1_req.text:
        print('Failed: invalid url')
        sys.exit()

    data = {
        "watchedFallback": 'false',
        '_csrf': re1.group().replace("Token = ", '').replace('''"''', ''),
        'activeAd': '2',
        'option': '0',
        'id': '',
    }

    # hypurl.replace('https://hypixel.net/claim-reward/','')
    urllclaim = "https://rewards.hypixel.net/claim-reward/claim" + '?' + str(data).replace("{", "").replace(
        "}", "").replace(':', '=').replace(',', '&').replace('"', '').replace("'", '').replace(" ", '')
    headers['cookie'] = '; '.join(
        [x.name + '=' + x.value for x in hyp1_req.cookies])

    r = requests.post(urllclaim, data=data, headers=headers)

    return r.text


print(get_chaim(url))

#window.appData = '{"rewards":[{"amount":10,"rarity":"COMMON","reward":"dust"},{"package":"specialoccasion_reward_card_skull_pot_o\'_gold","rarity":"COMMON","reward":"housing_package"},{"gameType":"SURVIVAL_GAMES","amount":3000,"rarity":"COMMON","reward":"coins"}],"id":"197d6535","skippable":false,"dailyStreak":{"value":0,"score":0,"highScore":0,"keeps":true,"token":false},"ad":{"video":"TRsCiBNYY7M","duration":28,"link":"https://store.hypixel.net/?utm_source=rewards-video&utm_medium=website&utm_content=TRsCiBNYY7M&utm_campaign=Rewards","buttonText":"Visit the Store"},"activeAd":0,"playwire":false}';
