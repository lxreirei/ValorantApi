import asyncio
import json
import time
import aiohttp

async def fetch_skins_all():
    url = "https://valorant-api.com/v1/weapons/skins"
    headers = {'Connection': 'close'}
    params = {"language": "ja-JP"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            res_skin = json.loads(await response.text())['data']
            with open('json/skinInfo.json','w', encoding="utf-8") as r:
                r.write(json.dumps(res_skin, ensure_ascii=False))

def showSkin(user, uuid):
    allSkins = json.load(open('json/skinInfo.json', 'r', encoding="utf-8"))
    allBundles = json.load(open('json/bundleInfo.json', 'r', encoding="utf-8"))
    data = {}
    for skin in allSkins:
        for i in skin['levels']:
            if (i['uuid']) == uuid:
                data["uuid"] = uuid
                data["contentTierUuid"] = skin['contentTierUuid']
                data["displayName"] = skin['displayName']
                if i['displayIcon'] is not None:
                    data["displayIcon"] = i['displayIcon']
                else:
                    data["displayIcon"] = skin['displayIcon']
                found_bundle = next((bundle for bundle in allBundles if bundle['displayName'] in skin['displayName']), None)
                if found_bundle:
                    data["bundle"] = found_bundle['displayName']
                else:
                    data["bundle"] = None
    return data

async def fetch_bundles_all():
    url = "https://valorant-api.com/v1/bundles"
    headers = {'Connection': 'close'}
    params = {"language": "ja-JP"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            res_bundle = json.loads(await response.text())['data']
            for bundle in res_bundle:
                print(bundle['displayName'], bundle['displayIcon'])
            with open('json/bundleInfo.json','w', encoding="utf-8") as r:
                r.write(json.dumps(res_bundle, ensure_ascii=False))



async def fetch_version():
    url = "https://valorant-api.com/v1/version"
    headers = {'Connection': 'close'}
    params = {"language": "ja-JP"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            res_version = json.loads(await response.text())['data']
            with open('json/versionInfo.json','w') as r:
                r.write(json.dumps(res_version))

if __name__ == '__main__':
    asyncio.run(fetch_skins_all())
    asyncio.run(fetch_bundles_all())
    asyncio.run(fetch_version())