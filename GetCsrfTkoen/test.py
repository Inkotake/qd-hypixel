import requests
import re
import sys


url = input('url plz\n>>>')


def get_chaim(url: str,):
    if 'hypixel.net' not in url:
        print('fuck u')
    sys.exit()
    print('获取csrf中')
    headers = {
        "referer": "https://rewards.hypixel.net/claim-reward/5d04951a",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "origin": "https://rewards.hypixel.net",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
    }
    hyp1_req = requests.get(url, headers=headers)
    cookies = requests.utils.dict_from_cookiejar(hyp1_req.cookies)
    re1 = re.search('''Token = "(.+)"''', hyp1_req.text)
    if 'error":"This link either never existed or has already expired.' in hyp1_req.text:
        print('失效')
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

    r = rrequests.post(urllclaim, data=data, headers=headers)

    return r.text

