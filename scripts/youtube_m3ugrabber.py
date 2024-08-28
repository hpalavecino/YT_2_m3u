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
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTBangladeshLogo.png" tvg-id="", TN
#EXTVLCOPT:network-caching=1000
https://live-01-01-tn.vodgc.net/TN24/index.m3u8
#EXTINF:-1 tvg-id="AmericaTucuman.ar" tvg-logo="https://i.imgur.com/TJmzwv9.png" group-title="Varios",América Tucumán (720p) [Not 24/7]
https://ythlsgo.onrender.com/channel/UCZ8sgVyD7HqDor8ujB-TZpg.m3u8
#EXTINF:-1 tvg-id="C5N.ar" tvg-logo="https://i.imgur.com/5ZNZYjO.png" group-title="Varios",C5N (1080p) [Not 24/7]
https://ythlsgo.onrender.com/channel/UCFgk2Q2mVO1BklRQhSv6p0w.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Canal 26
https://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Tec TV
https://tv.initium.net.ar:3939/live/tectvmainlive.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TVP
https://cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TyC
https://d3055hobuue3je.cloudfront.net/out/v1/188a8f3baf914a35868453bd5d0b0fd2/index_1.m3u8
#EXTINF:-1 group-title="Varios",TELEFE
https://telefe.com/Api/Videos/GetSourceUrl/694564/0/HLS
#EXTINF:-1 tvg-id="ElOcho.ar" tvg-logo="https://i.ibb.co/0yFbZj4/Captura.png" group-title="Varios",El Ocho (1080p) [Not 24/7]
https://ythlsgo.onrender.com/channel/UCYozHHDnLnQs2yc2k3t8cPA.m3u8    
###
#EXTINF:-1 group-title="Varios", Telefe (720p) [Geo-blocked]
https://telefe.com/Api/Videos/GetSourceUrl/694564/0/HLS?.m3u8=
#EXTINF:-1 group-title="Varios", ARG: DIRECTV SPORTS
http://iptv-tn.com:8080/23871776875/23871776875/60830
#EXTINF:-1 group-title="Varios", ARG: ESPN HD
http://iptv-tn.com:8080/23871776875/23871776875/60845
#EXTINF:-1 group-title="Varios", ARG: ESPN HD
http://iptv-tn.com:8080/23871776875/23871776875/60846
#EXTINF:-1 group-title="Varios", ARG: ESPN 2  HD
http://iptv-tn.com:8080/23871776875/23871776875/60842
#EXTINF:-1 group-title="Varios", ARG: TyC Sports
http://iptv-tn.com:8080/23871776875/23871776875/60891
#EXTINF:-1 group-title="Varios", ARG: TYC SPORTS LOCAL
http://iptv-tn.com:8080/23871776875/23871776875/60895
###
#EXTINF:-1 group-title="Varios", ARG: DIRECTV SPORTS
http://iptv-tn.com:8080/23871776875/23871776875/60830
#EXTINF:-1 group-title="Varios", ARG: ESPN HD
http://iptv-tn.com:8080/23871776875/23871776875/60845
#EXTINF:-1 group-title="Varios", ARG: ESPN HD
http://iptv-tn.com:8080/23871776875/23871776875/60846
#EXTINF:-1 group-title="Varios", ARG: ESPN 2  HD
http://iptv-tn.com:8080/23871776875/23871776875/60842
#EXTINF:-1 group-title="Varios", ARG: TyC Sports
http://iptv-tn.com:8080/23871776875/23871776875/60891
#EXTINF:-1 group-title="Varios", ARG: TYC SPORTS LOCAL
http://iptv-tn.com:8080/23871776875/23871776875/60895
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
