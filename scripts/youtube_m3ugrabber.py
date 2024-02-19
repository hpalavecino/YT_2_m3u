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
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TELEFE
http://190.61.46.126:8000/play/a02r/index.m3u8
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
#EXTINF:-1 tvg-id="ElOcho.ar" tvg-logo="https://i.ibb.co/0yFbZj4/Captura.png" group-title="General",El Ocho (1080p) [Not 24/7]
https://ythlsgo.onrender.com/channel/UCYozHHDnLnQs2yc2k3t8cPA.m3u8
#########################################################################
#########################################################################
#########################################################################

#EXTINF:-1,ESPN HD
http://177.128.113.8:1/play/a07l
#EXTINF:-1,ESPN 2 HD
http://177.128.113.8:1/play/a07g
#EXTINF:-1,ESPN 3 HD
http://177.128.113.8:1/play/a081
#EXTINF:-1,ESPN 4 HD
http://177.128.113.8:1/play/a08i
#EXTINF:-1,ESPN Extra HD
http://177.128.113.8:1/play/a08v
#####
#EXTINF:-1,TyC Sports HD
http://177.128.113.8:2/play/a09v
#####
#EXTINF:-1,AMC HD
http://38.43.132.86:8000/play/a02l/index.m3u8
#EXTINF:-1,AZ Cinema HD
http://38.43.132.86:8000/play/a02t/index.m3u8
#EXTINF:-1,America TV HD
http://38.43.132.86:8000/play/a02c/index.m3u8
#EXTINF:-1,Animal Planet HD
http://38.43.132.86:8000/play/a02v/index.m3u8
#EXTINF:-1,Cartoon Network HD
http://38.43.132.86:8000/play/a02p/index.m3u8
#EXTINF:-1,Cinecanal HD
http://38.43.132.86:8000/play/a02k/index.m3u8
#EXTINF:-1,DHE HD
http://38.43.132.86:8000/play/a032/index.m3u8
#EXTINF:-1,Discovery HD
http://38.43.132.86:8000/play/a033/index.m3u8
#EXTINF:-1,Discovery World HD
http://38.43.132.86:8000/play/a02j/index.m3u8
#EXTINF:-1,E! HD
http://38.43.132.86:8000/play/a029/index.m3u8
#EXTINF:-1,ESPN EXTRA HD
http://38.43.132.86:8000/play/a02m/index.m3u8
#EXTINF:-1,ESPN HD
http://38.43.132.86:8000/play/a028/index.m3u8
#EXTINF:-1,Food Network HD
http://38.43.132.86:8000/play/a02b/index.m3u8
#EXTINF:-1,GOLPERU HD
http://38.43.132.86:8000/play/a02f/index.m3u8
#EXTINF:-1,Golden HD
http://38.43.132.86:8000/play/a026/index.m3u8
#EXTINF:-1,HBO 2 HD
http://38.43.132.86:8000/play/a02u/index.m3u8
#EXTINF:-1,HBO Family HD
http://38.43.132.86:8000/play/a035/index.m3u8
#EXTINF:-1,HBO HD
http://38.43.132.86:8000/play/a02n/index.m3u8
#EXTINF:-1,HBO XTREME HD
http://38.43.132.86:8000/play/a036/index.m3u8
#EXTINF:-1,History 2 HD
http://38.43.132.86:8000/play/a034/index.m3u8
#EXTINF:-1,Kanal D Drama HD
http://38.43.132.86:8000/play/a02o/index.m3u8
#EXTINF:-1,Las Estrellas HD
http://38.43.132.86:8000/play/a031/index.m3u8
#EXTINF:-1,Latina HD
http://38.43.132.86:8000/play/a02d/index.m3u8
#EXTINF:-1,Lolly Kids HD
http://38.43.132.86:8000/play/a02x/index.m3u8
#EXTINF:-1,Love Nature HD
http://38.43.132.86:8000/play/a02y/index.m3u8
#EXTINF:-1,MTV HD
http://38.43.132.86:8000/play/a030/index.m3u8
#EXTINF:-1,Movistar Deportes HD
http://38.43.132.86:8000/play/a025/index.m3u8
#EXTINF:-1,Nat Geo HD
http://38.43.132.86:8000/play/a02i/index.m3u8
#EXTINF:-1,Paramount HD
http://38.43.132.86:8000/play/a02q/index.m3u8
#EXTINF:-1,STAR TVE HD
http://38.43.132.86:8000/play/a02s/index.m3u8
#EXTINF:-1,Stingray Concerts HD
http://38.43.132.86:8000/play/a02a/index.m3u8
#EXTINF:-1,Studio Universal HD
http://38.43.132.86:8000/play/a02r/index.m3u8
#EXTINF:-1,TNT Novelas HD
http://38.43.132.86:8000/play/a02w/index.m3u8
#EXTINF:-1,TV+ HD
http://38.43.132.86:8000/play/a02h/index.m3u8
#EXTINF:-1,Telehit HD
http://38.43.132.86:8000/play/a027/index.m3u8
#EXTINF:-1,TyC Sports HD
http://38.43.132.86:8000/play/a02e/index.m3u8

################################################
################################################
################################################

#EXTINF:-1,ESPN
http://191.97.14.38:4000/play/a017/index.m3u8
#EXTINF:-1,ESPN 2 Latin
http://191.97.14.38:4000/play/a016/index.m3u8
#EXTINF:-1,ESPN 3
http://191.97.14.38:4000/play/a027/index.m3u8
#EXTINF:-1,ESPN 4 HD
http://191.97.14.38:4000/play/a04d/index.m3u8
#EXTINF:-1,ESPN CO
http://191.97.14.38:4000/play/a01p/index.m3u8
#EXTINF:-1,ESPN HD
http://191.97.14.38:4000/play/a04g/index.m3u8
#EXTINF:-1,TNT SPORTS 2
http://191.97.14.38:4000/play/a04u/index.m3u8
#EXTINF:-1,TyC
http://191.97.14.38:4000/play/a019/index.m3u8
###
#EXTINF:-1,EVENTOS DEPORTIVOS
http://45.5.119.155:8090/play/a057/index.m3u8
#EXTINF:-1,MTV 00s HD
http://45.5.119.155:8090/play/a0i0/index.m3u8
#EXTINF:-1,MTV 80s
http://45.5.119.155:8090/play/a0ge/index.m3u8
#EXTINF:-1,MTV Hits
http://45.5.119.155:8090/play/a0gd/index.m3u8
###
#EXTINF:-1,TyCSports HD
http://45.166.92.22:58001/play/a04d/index.m3u8
###
#EXTINF:-1,ESPN
http://181.78.105.146:2000/play/a064/index.m3u8
#EXTINF:-1,ESPN 2
http://181.78.105.146:2000/play/a063/index.m3u8
#EXTINF:-1,ESPN 3
http://181.78.105.146:2000/play/a03n/index.m3u8
###
#EXTINF:-1,ESPN
http://181.78.105.146:6060/play/a036
#EXTINF:-1,ESPN 2
http://181.78.105.146:6060/play/a037
#EXTINF:-1,ESPN 3
http://181.78.105.146:6060/play/a00x
###
#EXTINF:-1,ESPN +
http://181.78.105.146:8800/play/a04i
#EXTINF:-1,ESPN 2 HD
http://181.78.105.146:8800/play/a055
#EXTINF:-1,ESPN 3
http://181.78.105.146:8800/play/a025
#EXTINF:-1,ESPN 3 HD
http://181.78.105.146:8800/play/a054
#EXTINF:-1,ESPN 4
http://181.78.105.146:8800/play/a06r
#EXTINF:-1,ESPN 4 HD
http://181.78.105.146:8800/play/a079
#EXTINF:-1,ESPN Extra
http://181.78.105.146:8800/play/a07r
#EXTINF:-1,ESPN HD
http://181.78.105.146:8800/play/a053
###
#EXTINF:-1,TyC Sports HD
http://177.128.113.8:1/play/a09v
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

