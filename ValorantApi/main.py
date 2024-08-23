import asyncio
import sys, json, os
from src.riot_auth import auth_ssl
import src.dailyShop as dailyShop
import src.getInfo as getInfo
import pprint, random


async def main():
    creds = ("ID", "Password")
    auth = auth_ssl.RiotAuth(username=creds[0])
    if os.path.exists(f"cookies/{creds[0]}.json"):
        reauth_result = await auth.reauthorize(load=True)
    else:
        reauth_result = await auth.authorize(*creds)
        cookies_dict = {cookie.key: cookie.value for cookie in auth._cookie_jar}
        with open(f"cookies/{creds[0]}.json", "w") as f:
            json.dump(cookies_dict, f, indent=4)
    list = await dailyShop.getDailyShop(*creds)
    pprint.pprint(list)

if __name__ == '__main__':
    asyncio.run(main())