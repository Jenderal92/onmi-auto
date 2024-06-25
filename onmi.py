# -*- coding: utf-8 -*-
import os
import re
import time
import random
import json
import string
import requests

def RandomGenerator(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def genmail():
    RandomStringForPREFIX = RandomGenerator(8)
    domains = ["1secmail.com", "1secmail.org", "1secmail.net", "icznn.com", "ezztt.com", "vjuum.com", "laafd.com", "txcct.com"]
    domain = random.choice(domains)
    return "{}@{}".format(RandomStringForPREFIX, domain)

def main():
    print("\nOmni Auto Reff + Bypass Follow | Shin Code\n")
    totals_reff = raw_input("How Much Reff U need? : " )
    invite_codes = raw_input("Reff Code : " )
    for i in range(int(totals_reff)):
        sess = requests.Session()
        email = genmail()
        user_name = email.split("@")[0]
        try:
            print("[{}] {} => Account => {}".format(i, email,invite_codes))
            register = sess.post(
                "https://onmi-waitlist.rand.wtf/api/register",
                json={
                    "email": email,
                    "nickname": user_name,
                    "password": "Shin_Code403",
                    "password_confirmation": "Shin_Code403",
                    "invite_code": invite_codes,
                },
            ).json()

            if register["status"] == "inactive":
                print("• Account successfully registered!")
                print("• Get verification code...")
                time.sleep(5)

                usern = email.split("@")[0]
                domain = email.split("@")[1]

                messages = requests.get(
                    "https://www.1secmail.com/api/v1/?action=getMessages&login={}&domain={}".format(usern, domain)
                ).json()
                
                if messages:
                    pesan = messages[0]
                    baca_pesan = requests.get(
                        "https://www.1secmail.com/api/v1/?action=readMessage&login={}&domain={}&id={}".format(usern, domain, pesan['id'])
                    ).json()["body"]

                    regex_url = re.findall('href="(.*?)"', baca_pesan)[0]
                    proses_verif = requests.get(regex_url, allow_redirects=True)
                    code = proses_verif.url.split("?verify_code=")[1]

                    print("• Code : {}".format(code))
                    print("• Verify account...")
                    time.sleep(5)

                    activate_account = sess.post(
                        "https://onmi-waitlist.rand.wtf/api/activate",
                        json={"code": code}
                    ).json()

                    if activate_account["status"] == "active":
                        print("• Account successfully verified!")
                        username = activate_account["nickname"]
                        print("• Success Verify account... : {}".format(username))
                        print("• Get Token")
                        time.sleep(5)

                        login_token = sess.post(
                            "https://onmi-waitlist.rand.wtf/api/login",
                            json={"email": email, "password": "Shin_Code403"}
                        ).json()["token"]

                        print("• Token successfully obtained!")
                        print("• Bypass Auto Follow")
                        time.sleep(5)

                        headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
                            "Accept": "*/*",
                            "Accept-Language": "id,en-US;q=0.7,en;q=0.3",
                            "Accept-Encoding": "gzip, deflate",
                            "Referer": "https://onmi.io/",
                            "Content-Type": "application/json",
                            "Authorization": "Bearer: " + login_token,
                            "Origin": "https://onmi.io",
                            "Connection": "close",
                            "Sec-Fetch-Dest": "empty",
                            "Sec-Fetch-Mode": "cors",
                            "Sec-Fetch-Site": "cross-site",
                            "Priority": "u=4"
                        }
                        
                        follow_types = [
                            ("follow_vivi", "Vivi"),
                            ("follow_instagram_nk", "Instagram"),
                            ("follow_twitter_nk", "X"),
                            ("follow_discord", "Discord"),
                            ("follow_telegram", "Telegram"),
                        ]

                        for source, name in follow_types:
                            payload = {"source": source}
                            response = sess.post("https://onmi-waitlist.rand.wtf/api/link_social", headers=headers, data=json.dumps(payload))
                            
                            print("• Success bypass {} Community!".format(name))
                            time.sleep(5)

        except Exception as e:
            print("Error occurred: {}".format(e))

if __name__ == "__main__":
    main()
