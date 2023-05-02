GNU nano 5.4                                                                  scan.py
##############################################################
# extract all IP ranges in CIDR notation.                    #
# Useful if You want to scan the whole Internet of a country #
#                                                            #
# written in 5/2023 bý Steve                                 #
# visit our Pentesting and Coding Discord:                   #
# https://discord.gg/qeTtcB7U                                #
##############################################################


import requests
from bs4 import BeautifulSoup

COUNTRY = "de"

print("*****************************************************************")
print("IP Range Scanner - written in 05/2023 by Steve")
print("Visit our Pentesting  Discord Server: https://discord.gg/qeTtcB7U")
print("*****************************************************************")

headers = { "User-Agent": "Chrome/90.0.4430.93 Safari/537.36" }

country_html = requests.get("https://ipinfo.io/countries/" + COUNTRY).text
country_soup = BeautifulSoup(country_html, 'html.parser')

cidr_ranges = []
for ans_link in country_soup.find_all('a'):
    if "AS" in ans_link.text and not ' ' in ans_link.text:
        print(f"[i] Work in progress [{ans_link.text}]...")
        asn_html = requests.get("https://ipinfo.io/" + ans_link.text, headers=headers).text
        asn_soup = BeautifulSoup(asn_html, 'html.parser')
        for cidr_link in asn_soup.find_all('a'):
            if "/" in cidr_link.text and not ' ' in cidr_link.text and not ':' in cidr_link.text:
                cidr_ranges.append(cidr_link.text)

with open("AR-IP-BLOCK-ALL.txt", 'w') as f:
    for cidr in cidr_ranges:
        f.write(cidr + '\n')

    f.flush()
