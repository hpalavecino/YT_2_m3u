#! /usr/bin/python3

banner = r'''
#########################################################################
#      ____            _           _   __  __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                   |__/                                                #
#                                  >> https://github.com/benmoose39     #
#########################################################################
#EXTM3U

#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Canal 13
#EXTVLCOPT:network-caching=1000
https://live-01-02-eltrece.vodgc.net/eltrecetv/index.m3u8
#EXTINF:-1 group-title="Varios",América TV (720p)
#EXTVLCOPT:http-user-agent=iPhone
#EXTVLCOPT:network-caching=1000
https://raw.githubusercontent.com/MachineSystems/archived_m3u8/main/america_hls.m3u8
#EXTINF:-1 group-title="Varios",TELEFE
https://telefe.com/Api/Videos/GetSourceUrl/694564/0/HLS
###
#EXTINF:-1 group-title="Varios", Telefe (720p) [Geo-blocked]
https://telefe.com/Api/Videos/GetSourceUrl/694564/0/HLS?.m3u8=
#EXTINF:-1 group-title="Varios", Espn Chile
http://190.211.250.102:8000/play/a017
#EXTINF:-1 group-title="Varios", Espn 2 Chile
http://190.211.250.102:8000/play/a016
#EXTINF:-1 group-title="Varios", Fox Sports/ESPN Premium Chile
http://190.211.250.102:8000/play/a00r
#EXTINF:-1 group-title="Varios", Fox Sports 3/ ESPN 6 Chile
http://190.211.250.102:8000/play/a00n
#EXTINF:-1 group-title="Varios", GATITO-TV-ESPN
http://45.181.123.233:8000/play/a0o9
#EXTINF:-1 group-title="Varios", GATITO-TV-ESPN 2
http://45.181.123.233:8000/play/a0qt
#EXTINF:-1 group-title="Varios", GATITO-TV-ESPN 3
http://45.181.123.233:8000/play/a0p2
#EXTINF:-1 group-title="Varios", GATITO-TV-ESPN 4
http://45.181.123.233:8000/play/a164
#EXTINF:-1 group-title="Varios", GATITO-TV-Fox Sports 1
http://45.181.123.233:8000/play/a0qm
#EXTINF:-1 group-title="Varios", GATITO-TV-Fox Sports 2
http://45.181.123.233:8000/play/a0oj
#EXTINF:-1 group-title="Varios", GATITO-TV-Fox Sports 3
http://45.181.123.233:8000/play/a0ok
#EXTINF:-1 group-title="Varios", TyC Sports HD
http://190.61.44.34:1010/play/a05f/index.m3u8
#EXTINF:-1 group-title="Varios", FOX Sports 2 HD
http://190.61.44.34:1010/play/a04c/index.m3u8
#EXTINF:-1 group-title="Varios", Fox Sports 1 HD
http://190.61.44.34:1010/play/a05u/index.m3u8
#EXTINF:-1 group-title="Varios", Fox Sports 3 HD
http://190.61.44.34:1010/play/a00q/index.m3u8
#EXTINF:-1 group-title="Varios", ESPN
http://190.61.44.34:1010/play/a09o/index.m3u8
#EXTINF:-1 group-title="Varios", ESPN 2 HD
http://190.61.44.34:1010/play/a09p/index.m3u8
#EXTINF:-1 group-title="Varios", ESPN 2 HD
http://190.61.44.34:1010/play/a00d/index.m3u8
#EXTINF:-1 group-title="Varios", ESPN 3 HD
http://190.61.44.34:1010/play/a00p/index.m3u8
#EXTINF:-1 group-title="Varios", ESPN 4 HD
http://190.61.44.34:1010/play/a04b/index.m3u8
#EXTINF:-1 group-title="Varios", ESPN EXTRA HD
http://190.61.44.34:1010/play/a04r/index.m3u8
#EXTINF:-1 group-title="Varios", ESPN HD
http://190.61.44.34:1010/play/a00h/index.m3u8
###
#EXTINF:-1 group-title="Varios", EVENTOS TyC PLAY 1
https://dj8bzwveg7go9.cloudfront.net/out/v1/09e35529553d472b8f14e437af642e2f/index.m3u8
#EXTINF:-1 group-title="Varios", EVENTOS TyC PLAY 2
https://d320m3arb2wo8b.cloudfront.net/out/v1/34e0da501a8c4489b713809eb08a9bf3/index.m3u8
#EXTINF:-1 group-title="Varios",EVENTOS TyC PLAY 3
https://d1xm2jznwi5xzj.cloudfront.net/out/v1/1bcd1ee954894463b1793597891a25b6/index.m3u8
#EXTINF:-1 group-title="Varios", EVENTOS TyC PLAY 4
https://dpyzprfzko681.cloudfront.net/out/v1/366fc52554ae42c58465ea4b278eac0c/index.m3u8
#EXTINF:-1 group-title="Varios", EVENTOS TyC PLAY 5
https://d107yb993altze.cloudfront.net/out/v1/772e0b0193134726ad84693b7baca6c6/index.m3u8
#EXTINF:-1 group-title="Varios", EVENTOS TyC PLAY 6
https://d21no6qan3ol31.cloudfront.net/out/v1/a2f25f61e9d44701aa4e813ac5efc4a4/index.m3u8
#EXTINF:-1 group-title="Varios", EVENTOS TyC PLAY 7
https://d3v9hc3dccxi3a.cloudfront.net/out/v1/bccdd4d97f434c63ab2f675e5145758f/index.m3u8
#EXTINF:-1 group-title="Varios", EVENTOS TyC PLAY 8
https://dbjn2fo8vpiph.cloudfront.net/out/v1/4c8dc641a91448439388e41118924965/index.m3u8
#EXTINF:-1 group-title="Varios", EVENTOS TyC PLAY 9
https://d1scuk1wvkchtc.cloudfront.net/out/v1/19321d887c274b58a4f62fe0f6e2151b/index.m3u8
#EXTINF:-1 group-title="Varios", EVENTOS TyC PLAY 10
https://dhmxbo9piuo21.cloudfront.net/out/v1/84ee2b0cce384a30abd70b05562ddd91/index.m3u8
#EXTINF:-1 group-title="Varios", EVENTOS TyC PLAY 11
https://d2scohpz55y5r5.cloudfront.net/out/v1/c43ac17254584daa9781eaaeea1a085d/
###
#EXTINF:-1 group-title="Varios",C5N
https://ythls-v3.onrender.com/channel/UCFgk2Q2mVO1BklRQhSv6p0w.m3u8
#EXTINF:-1 group-title="Varios",TN
https://ythls-v3.onrender.com/channel/UCj6PcyLvpnIRT_2W_mwa9Aw.m3u8
#EXTINF:-1 group-title="Varios",OLGA
https://ythls-v3.onrender.com/channel/UC7mJ2EDXFomeDIRFu5FtEbA.m3u8
#EXTINF:-1 group-title="Varios",Urbana Play
https://ythls-v3.onrender.com/channel/UCC1kfsMJko54AqxtcFECt-A.m3u8
#EXTINF:-1 group-title="Varios",LaNacion+
https://ythls-v3.onrender.com/channel/UCba3hpU7EFBSk817y9qZkiA.m3u8
#EXTINF:-1 group-title="Varios",La100
https://ythls-v3.onrender.com/channel/UC2zO2jZCDplwm8SVsXUcxCQ.m3u8
#EXTINF:-1 group-title="Varios",CronicaTV
https://ythls-v3.onrender.com/channel/UCT7KFGv6s2a-rh2Jq8ZdM1g.m3u8
#EXTINF:-1 group-title="Varios",A24
https://ythls-v3.onrender.com/channel/UCR9120YBAqMfntqgRTKmkjQ.m3u8
#EXTINF:-1 group-title="Varios",RadioPOP
https://ythls-v3.onrender.com/channel/UCtc_WjDRwCrZSEq2WEwD7XQ.m3u8
#EXTINF:-1 group-title="Varios",Vorterix
https://ythls-v3.onrender.com/channel/UCvCTWHCbBC0b9UIeLeNs8ug.m3u8
#EXTINF:-1 group-title="Varios",Canal26
https://ythls-v3.onrender.com/channel/UCrpMfcQNog595v5gAS-oUsQ.m3u8
#EXTINF:-1 group-title="Varios",Radio La Red
https://ythls-v3.onrender.com/channel/UCs1U5lRXvUJHn0CgXI6oXAw.m3u8
#EXTINF:-1 group-title="Varios",Rock&POP
https://ythls-v3.onrender.com/channel/UCAlQ5f7mhnkfM6jjXeJDw7g.m3u8
#EXTINF:-1 group-title="Varios",Blender
https://ythls-v3.onrender.com/channel/UC6pJGaMdx5Ter_8zYbLoRgA.m3u8
#EXTINF:-1 group-title="Varios",Gelatina
https://ythls-v3.onrender.com/channel/UCWSfXECGo1qK_H7SXRaUSMg.m3u8
#EXTINF:-1 group-title="Varios",Bondi Live
https://ythls-v3.onrender.com/channel/UCnZidingmuqNkaT9Wm64Xxg.m3u8
#EXTINF:-1 group-title="Varios",Futurock FM
https://ythls-v3.onrender.com/channel/UCgn6r0aGRBnEQm02tE_jzbw.m3u8
#EXTINF:-1 group-title="Varios",Neura
https://ythls-v3.onrender.com/channel/UC-40U87JsevMIMn7PMw4jPw.m3u8
#EXTINF:-1 group-title="Varios",El Destape
https://ythls-v3.onrender.com/channel/UC5wAqJ9NF0fpGH9dVf3h6HA.m3u8
#EXTINF:-1 group-title="Varios",Telefe Streaming
https://ythls-v3.onrender.com/channel/UCHc3el42hXKKhjs_1vzWk9A.m3u8
#EXTINF:-1 group-title="Varios",Cenital
https://ythls-v3.onrender.com/channel/UCxHSIJgKZ8xVXwLGaGZEmKg.m3u8
#EXTINF:-1 group-title="Varios",Republica Z
https://ythls-v3.onrender.com/channel/UCmk9kjghfkM3k8I6jioDr3g.m3u8
#EXTINF:-1 group-title="Varios",La Casa Streaming
https://ythls-v3.onrender.com/channel/UC4u0BhsSi33PS20_1JHiC5A.m3u8
#EXTINF:-1 group-title="Varios",Picnic Extraterrestre
https://ythls-v3.onrender.com/channel/UCzHOIqsAR8xv-Q7SrzBQxqA.m3u8
#EXTINF:-1 group-title="Varios",Ahora Play
https://ythls-v3.onrender.com/channel/UCRyGJcJYqqiCByEaUhDLMsw.m3u8
#EXTINF:-1 group-title="Varios",Mate
https://ythls-v3.onrender.com/channel/UCTlUJTm5qFRLylSJ_8KS34A.m3u8
#EXTINF:-1 group-title="Varios",Posdata
https://ythls-v3.onrender.com/channel/UC7Hx4xBMuw_PvVUliihHEcQ.m3u8
#EXTINF:-1 group-title="Varios",Mix On
https://ythls-v3.onrender.com/channel/UCxJoozHpQKs-8IpoHon5PDg.m3u8
#EXTINF:-1 group-title="Varios",Carajo
https://ythls-v3.onrender.com/channel/UC4mdhKZXjrKoq5aVG6juHEg.m3u8
#EXTINF:-1 group-title="Varios",Eva TV
https://ythls-v3.onrender.com/channel/UCWwZpofeEFNH-R8g1DC0fHA.m3u8
#EXTINF:-1 group-title="Varios",Clank!
https://ythls-v3.onrender.com/channel/UCfXT6V8ZMhybyV1LVdSQ7-A.m3u8
#EXTINF:-1 group-title="Varios",La Gaceta Play
https://ythls-v3.onrender.com/channel/UCowbI8idnvQTl2sFxkOvnKw.m3u8
#EXTINF:-1 group-title="Varios",El Ocho TV
https://ythls-v3.onrender.com/channel/UCYozHHDnLnQs2yc2k3t8cPA.m3u8
#EXTINF:-1 group-title="Varios",America Tucuman
https://ythls-v3.onrender.com/channel/UCZ8sgVyD7HqDor8ujB-TZpg.m3u8
#EXTINF:-1 group-title="Varios",TUCMA TV
https://ythls-v3.onrender.com/channel/UCzEK8YGump2Ubaf-Kk_cfvw.m3u8
#EXTINF:-1 group-title="Varios",La Tucumana FM
https://ythls-v3.onrender.com/channel/UCS_F0326eeAQY09gFqJILCw.m3u8
#EXTINF:-1 group-title="Varios",Los Primeros
https://ythls-v3.onrender.com/channel/UCf62XaF_MK2k2-wVggZ6kuw.m3u8
#EXTINF:-1 group-title="Varios",El Observador
https://ythls-v3.onrender.com/channel/UC-rI_XNppHJO-Ga4RW_CDKw.m3u8
#EXTINF:-1 group-title="Varios",TyC Sports Streaming
https://ythls-v3.onrender.com/channel/UC72ZaBKI-Bo5fjmWEYonhJw.m3u8
#EXTINF:-1 group-title="Varios",Radio Rivadavia
https://ythls-v3.onrender.com/channel/UCLAj5TzCrNbqe3LosSKHLcQ.m3u8
#EXTINF:-1 group-title="Varios",Fm TOP 104.9
https://ythls-v3.onrender.com/channel/UCQE5K3FdK8Q0CFtAMEFz09g.m3u8
#EXTINF:-1 group-title="Varios",Costa Febre Monumental
https://ythls-v3.onrender.com/channel/UCzbLuIuaZLt7JhJ_aI6mMXA.m3u8
'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')
print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
