import requests
import re
import sys
import json
import warnings
url = input('Please input hypixel url\n>>>')


def get_chaim(url: str,):
    if not 'hypixel.net/claim-reward' in url:
        print('Failed: Not a Hypixel url')
        sys.exit()
    print('Csrf loading... Speed depend on GFW')
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

    rewardjss = re.findall(r"window.appData \= \'(.*)\';",hyp1_req.text)
    rewardjs = json.loads(rewardjss[0])
    for x in rewardjs['rewards']:
        print (x['reward'])



    rechoose = input('Please choose a reward (0~2)\n>>>')
    data = {
        "watchedFallback": 'false',
        '_csrf': re1.group().replace("Token = ", '').replace('''"''', ''),
        'activeAd': rechoose,
        'option': '0',
        'id': rewardjs['id'],
    }

    print('You choose',rechoose,'Now Post reward api...')

    # hypurl.replace('https://hypixel.net/claim-reward/','')
    urllclaim = "https://rewards.hypixel.net/claim-reward/claim" + '?' + str(data).replace("{", "").replace(
        "}", "").replace(':', '=').replace(',', '&').replace('"', '').replace("'", '').replace(" ", '')
    headers['cookie'] = '; '.join(
        [x.name + '=' + x.value for x in hyp1_req.cookies])

    r = requests.post(urllclaim, data=data, headers=headers)

    return r.text


print(get_chaim(url))

# window.appData = '{"rewards":[{"intlist":[4],"rarity":"RARE","reward":"mystery_box"},{"amount":1,"rarity":"RARE","reward":"adsense_token"},{"amount":20,"rarity":"RARE","reward":"dust"}],"id":"3f45f1e0","skippable":false,"dailyStreak":{"value":0,"score":0,"highScore":0,"keeps":true,"token":false},"ad":{"video":"GNhbZ5guqO0","duration":30,"link":"https://store.hypixel.net/?utm_source=rewards-video&utm_medium=website&utm_content=GNhbZ5guqO0&utm_campaign=Rewards","buttonText":"Visit the Store"},"activeAd":2,"playwire":false}';
# window.appData = '{"rewards":[{"amount":10,"rarity":"COMMON","reward":"dust"},{"package":"specialoccasion_reward_card_skull_pot_o\'_gold","rarity":"COMMON","reward":"housing_package"},{"gameType":"SURVIVAL_GAMES","amount":3000,"rarity":"COMMON","reward":"coins"}],"id":"197d6535","skippable":false,"dailyStreak":{"value":0,"score":0,"highScore":0,"keeps":true,"token":false},"ad":{"video":"TRsCiBNYY7M","duration":28,"link":"https://store.hypixel.net/?utm_source=rewards-video&utm_medium=website&utm_content=TRsCiBNYY7M&utm_campaign=Rewards","buttonText":"Visit the Store"},"activeAd":0,"playwire":false}';
