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
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TN
#EXTVLCOPT:network-caching=1000
https://live-01-01-tn.vodgc.net/TN24/index.m3u8
#EXTINF:-1 tvg-id="AmericaTucuman.ar" tvg-logo="https://i.imgur.com/TJmzwv9.png" group-title="News",América Tucumán (720p) [Not 24/7]
https://ythlsgo.onrender.com/channel/UCZ8sgVyD7HqDor8ujB-TZpg.m3u8
#EXTINF:-1 tvg-id="C5N.ar" tvg-logo="https://i.imgur.com/5ZNZYjO.png" group-title="News",C5N (1080p) [Not 24/7]
https://ythlsgo.onrender.com/channel/UCFgk2Q2mVO1BklRQhSv6p0w.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Canal 26
https://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Tec TV
https://tv.initium.net.ar:3939/live/tectvmainlive.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TVP
https://cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TyC
https://d3055hobuue3je.cloudfront.net/out/v1/188a8f3baf914a35868453bd5d0b0fd2/index_1.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TyC
https://d3055hobuue3je.cloudfront.net/out/v1/188a8f3baf914a35868453bd5d0b0fd2/index_4.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TELEFE
http://200.115.120.1:8000/play/ca063/index.m3u8
#EXTINF:-1 tvg-id="TELEFE" tvg-logo="https://i.ibb.co/0yFbZj4/Captura.png" group-title="General",TELEFE
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/3536
#EXTINF:-1,TELEFE
https://telefe.com/Api/Videos/GetSourceUrl/694564/0/HLS
#EXTINF:-1 tvg-id="ElOcho.ar" tvg-logo="https://i.ibb.co/0yFbZj4/Captura.png" group-title="General",El Ocho (1080p) [Not 24/7]
https://ythlsgo.onrender.com/channel/UCYozHHDnLnQs2yc2k3t8cPA.m3u8
###
#EXTINF:-1,ESPN 1 ARGENTINA FULL HD
http://restreamus.com:8080/play2022/XASFqNvz3ThB/242596
#EXTINF:-1,││ARG││ ESPN PREMIUM [SD]
http://restreamus.com:8080/play2022/XASFqNvz3ThB/99
#EXTINF:-1,││ARG││  TNT SPORTS ARGENTINA [HD]
http://restreamus.com:8080/play2022/XASFqNvz3ThB/147
#EXTINF:-1,││ARG││  TNT SPORTS ARGENTINA [FHD]
http://restreamus.com:8080/play2022/XASFqNvz3ThB/386
#EXTINF:-1,││ARG││ TYC SPORTS [HD1]
http://restreamus.com:8080/play2022/XASFqNvz3ThB/267
#EXTINF:-1,││ARG││  TYC SPORTS ARGENTINA  [HD] (N)
http://restreamus.com:8080/play2022/XASFqNvz3ThB/148
#EXTINF:-1,││ARG││ TYC SPORTS OPC1 [HD] (N)
http://restreamus.com:8080/play2022/XASFqNvz3ThB/26868
#EXTINF:-1,││ARG││  TYC SPORTS HD (OPC)
http://restreamus.com:8080/play2022/XASFqNvz3ThB/27864
#EXTINF:-1,││ARG││ FOX SPORTS (OPC) [HD] 
http://restreamus.com:8080/play2022/XASFqNvz3ThB/27860
#EXTINF:-1,││ARG││ FOX SPORTS ARGENTINA [FHD] (N)
http://restreamus.com:8080/play2022/XASFqNvz3ThB/144
#EXTINF:-1,││CULT HD││ H2 
http://restreamus.com:8080/play2022/XASFqNvz3ThB/164
#EXTINF:-1,││CINE HD││ DISNEY
http://restreamus.com:8080/play2022/XASFqNvz3ThB/112
#EXTINF:-1,││CINE HD││PARAMOUT (N)
http://restreamus.com:8080/play2022/XASFqNvz3ThB/123
###
SP: ARG: ESPN 1 SD
http://62.4.15.182:8880/agos201910/661619291/317178
SP: ARG: ESPN 1 HD
http://62.4.15.182:8880/agos201910/661619291/317179
SP: ARG: ESPN 1 FHD
http://62.4.15.182:8880/agos201910/661619291/317180
SP: ARG: ESPN Premium SD
http://62.4.15.182:8880/agos201910/661619291/317189
SP: ARG: ESPN Premium HD
http://62.4.15.182:8880/agos201910/661619291/317190
SP: ARG: ESPN Premium FHD
http://62.4.15.182:8880/agos201910/661619291/317191
SP: ARG: TyC Sports Internacional SD
http://62.4.15.182:8880/agos201910/661619291/317173
SP: ARG: TyC Sports Internacional HD
http://62.4.15.182:8880/agos201910/661619291/317174
SP: ARG: Directv Sports 1 HD
http://62.4.15.182:8880/agos201910/661619291/317175
SP: ARG: Fox Sports 1 SD
http://62.4.15.182:8880/agos201910/661619291/317192
SP: ARG: Fox Sports 1 HD
http://62.4.15.182:8880/agos201910/661619291/317193
SP: ARG: TNT Sports (Movil)
http://62.4.15.182:8880/agos201910/661619291/317200
SP: ARG: TNT Sports SD
http://62.4.15.182:8880/agos201910/661619291/317201
SP: ARG: TNT Sports HD
http://62.4.15.182:8880/agos201910/661619291/317202
SP: ARG: TNT Sports FHD
http://62.4.15.182:8880/agos201910/661619291/317203
###
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

print(banner)

