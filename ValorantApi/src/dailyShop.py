import json
import time
import aiohttp
import os
import base64, pprint
from src.riot_auth import auth_ssl


async def fetch_skins_all_price(user, passwd):
    auth = auth_ssl.RiotAuth(user)
    reauth_result = await auth.reauthorize(load=True)
    access_token = auth.access_token
    if access_token == None:
        return False
    entitlements_token = auth.entitlements_token
    client_platform = {
        "platformType": "PC",
        "platformOS": "Windows",
        "platformOSVersion": "10.0.19042.1.256.64bit",
        "platformChipset": "Unknown"
    }
    url = "https://pd.ap.a.pvp.net/store/v1/offers/"
    client_platform = base64.b64encode(json.dumps(client_platform).encode()).decode()
    with open('json/versionInfo.json','r') as r:
        version = json.load(r)
        version = version['riotClientVersion']
    headers = {
        "Content-Type": "application/json",
        "X-Riot-ClientPlatform": client_platform,
        "X-Riot-ClientVersion": version,
        "X-Riot-Entitlements-JWT": entitlements_token,
        "Authorization": "Bearer " + access_token
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            res = json.loads(await response.text())
            return res

async def nightmarket(user, passwd):
    auth = auth_ssl.RiotAuth(user)
    auth_toekn = await auth.reauthorize(load=True)
    if auth_toekn == False:
        return False
    access_token = auth.access_token
    if access_token == None:
        return False
    entitlements_token = auth.entitlements_token
    auth_user_id = auth.user_id
    client_platform = {
        "platformType": "PC",
        "platformOS": "Windows",
        "platformOSVersion": "10.0.19042.1.256.64bit",
        "platformChipset": "Unknown"
    }
    url = "https://pd.ap.a.pvp.net/store/v2/storefront/" + auth_user_id
    client_platform = base64.b64encode(json.dumps(client_platform).encode()).decode()
    with open('json/versionInfo.json','r') as r:
        version = json.load(r)
        version = version['riotClientVersion']
    headers = {
        "Content-Type": "application/json",
        "X-Riot-ClientPlatform": client_platform,
        "X-Riot-ClientVersion": version,
        "X-Riot-Entitlements-JWT": entitlements_token,
        "Authorization": "Bearer " + access_token
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            res = json.loads(await response.text())
            return res["BonusStore"]["BonusStoreOffers"]



async def getDailyShop(user, passwd):
    auth = auth_ssl.RiotAuth(user)
    auth_toekn = await auth.reauthorize(load=True)
    if auth_toekn == False:
        return False
    access_token = auth.access_token
    if access_token == None:
        return False
    entitlements_token = auth.entitlements_token
    auth_user_id = auth.user_id
    client_platform = {
        "platformType": "PC",
        "platformOS": "Windows",
        "platformOSVersion": "10.0.19042.1.256.64bit",
        "platformChipset": "Unknown"
    }
    url = "https://pd.ap.a.pvp.net/store/v2/storefront/" + auth_user_id
    client_platform = base64.b64encode(json.dumps(client_platform).encode()).decode()
    with open('json/versionInfo.json','r') as r:
        version = json.load(r)
        version = version['riotClientVersion']
    headers = {
        "Content-Type": "application/json",
        "X-Riot-ClientPlatform": client_platform,
        "X-Riot-ClientVersion": version,
        "X-Riot-Entitlements-JWT": entitlements_token,
        "Authorization": "Bearer " + access_token
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            res = json.loads(await response.text())
            return res["SkinsPanelLayout"]["SingleItemOffers"]




async def fetch_content(user, passwd):
    auth = auth_ssl.RiotAuth(user)
    auth_toekn = await auth.reauthorize(load=True)
    access_token = auth.access_token
    entitlements_token = auth.entitlements_token
    auth_user_id = auth.user_id
    client_platform = {
        "platformType": "PC",
        "platformOS": "Windows",
        "platformOSVersion": "10.0.19042.1.256.64bit",
        "platformChipset": "Unknown"
    }
    url = f'https://pd.ap.a.pvp.net/mmr/v1/players/' + auth_user_id
    client_platform = base64.b64encode(json.dumps(client_platform).encode()).decode()
    with open('json/versionInfo.json','r') as r:
        version = json.load(r)
        version = version['riotClientVersion']
    headers = {
        "Content-Type": "application/json",
        "X-Riot-ClientPlatform": client_platform,
        "X-Riot-ClientVersion": version,
        "X-Riot-Entitlements-JWT": entitlements_token,
        "Authorization": "Bearer " + access_token
    }
    async with aiohttp.ClientSession() as session:
        async with session.get("https://shared.ap.a.pvp.net/content-service/v3/content", headers=headers) as response:
            res = json.loads(await response.text())
            return res

async def players(user, passwd):
    auth = auth_ssl.RiotAuth(user)
    auth_toekn = await auth.reauthorize(load=True)
    access_token = auth.access_token
    entitlements_token = auth.entitlements_token
    auth_user_id = auth.user_id
    client_platform = {
        "platformType": "PC",
        "platformOS": "Windows",
        "platformOSVersion": "10.0.19042.1.256.64bit",
        "platformChipset": "Unknown"
    }
    url = f'https://pd.ap.a.pvp.net/mmr/v1/players/' + auth_user_id
    client_platform = base64.b64encode(json.dumps(client_platform).encode()).decode()
    with open('json/versionInfo.json','r') as r:
        version = json.load(r)
        version = version['riotClientVersion']
    headers = {
        "Content-Type": "application/json",
        "X-Riot-ClientPlatform": client_platform,
        "X-Riot-ClientVersion": version,
        "X-Riot-Entitlements-JWT": entitlements_token,
        "Authorization": "Bearer " + access_token
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            res = json.loads(await response.text())
            data = res['QueueSkills']['competitive']
            rank_list = []
            for i in data['SeasonalInfoBySeasonID']:
                if not data['SeasonalInfoBySeasonID'][i]['Rank'] == 0:
                    rank_list.append(data['SeasonalInfoBySeasonID'][i])
                else:
                    rank_list.append(data['SeasonalInfoBySeasonID'][i])
            return rank_list




async def my_all_showSkin(user, passwd):
    auth = auth_ssl.RiotAuth(user)
    auth_toekn = await auth.reauthorize(load=True)
    if auth_toekn == False:
        return False
    access_token = auth.access_token
    entitlements_token = auth.entitlements_token
    auth_user_id = auth.user_id
    url = f"https://pd.ap.a.pvp.net/store/v1/entitlements/{auth_user_id}/e7c63390-eda7-46e0-bb7a-a6abdacd2433"
    client_platform = {
        "platformType": "PC",
        "platformOS": "Windows",
        "platformOSVersion": "10.0.19042.1.256.64bit",
        "platformChipset": "Unknown"
    }
    client_platform = base64.b64encode(json.dumps(client_platform).encode()).decode()
    with open('json/versionInfo.json','r') as r:
        version = json.load(r)
        version = version['riotClientVersion']
    headers = {
        "Content-Type": "application/json",
        "X-Riot-ClientPlatform": client_platform,
        "X-Riot-ClientVersion": version,
        "X-Riot-Entitlements-JWT": entitlements_token,
        "Authorization": "Bearer " + access_token
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            res = json.loads(await response.text())
            return res["Entitlements"]


async def players_competitiveupdates(user, passwd):
    auth = auth_ssl.RiotAuth(user)
    auth_toekn = await auth.reauthorize(load=True)
    if auth_toekn == False:
        return False
    access_token = auth.access_token
    entitlements_token = auth.entitlements_token
    auth_user_id = auth.user_id
    client_platform = {
        "platformType": "PC",
        "platformOS": "Windows",
        "platformOSVersion": "10.0.19042.1.256.64bit",
        "platformChipset": "Unknown"
    }
    url = f'https://pd.ap.a.pvp.net/mmr/v1/players/' + auth_user_id + '/competitiveupdates'
    client_platform = base64.b64encode(json.dumps(client_platform).encode()).decode()
    with open('json/versionInfo.json','r') as r:
        version = json.load(r)
        version = version['riotClientVersion']
    headers = {
        "Content-Type": "application/json",
        "X-Riot-ClientPlatform": client_platform,
        "X-Riot-ClientVersion": version,
        "X-Riot-Entitlements-JWT": entitlements_token,
        "Authorization": "Bearer " + access_token
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            res = json.loads(await response.text())
            return res



def findAllAuthFiles():
    file_dir = 'auth/'
    for root, dirs, files in os.walk(file_dir):
        return files

def findAuth(user):
    allFile = findAllAuthFiles()
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    file = ""
    for file in allFile:
        if date in file and (user + '.txt') in file:
            print(file)
    with open('auth/'+ file,'r') as f:
        username = f.readline()
        access_token = f.readline().split()[1].strip()
        entitlements_token = f.readline().split()[1].strip()
        auth_user_id = f.readline().split()[1].strip()
        return access_token,entitlements_token,auth_user_id






