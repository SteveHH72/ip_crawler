# ip_crawler
IP crawler to scan the entire IP address space of a country using the AS numbers


Dependicies:
***********

- Up to Date Linux
- python 3
- installes Beautiful Soup 4

To install Beatiful Soup 4 you can use 2 Options:

apt install python3-bs4

Or 

pip install beautifulsoup4


Usage of the script
*******************

In the first you have to tell the script which county it have to use. Go to the source code and change this line: 

COUNTRY = "de"

(Here you can find all county codes: https://www.laenderdaten.info/laendercodes.php)

Save the script and run it. 

python3 crawler.py

After some seconds the script starts and crawl all IP ranges of the county. After completion you can find a .txt file in the folder of the script and use it for other things ;-)




Join our Pentesting Discord Server: 

https://discord.gg/qeTtcB7U
