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
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", America TV
http://claymorej2.pinals.xyz:8080/TomasClicKTv/TKm9apZJ2qHP/81270
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
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TELEFE
http://200.115.120.1:8000/play/ca063/index.m3u8
#EXTINF:-1 tvg-id="TELEFE" tvg-logo="https://i.ibb.co/0yFbZj4/Captura.png" group-title="General",TELEFE
http://claymorej2.pinals.xyz:8080/TomasClicKTv/TKm9apZJ2qHP/81277
#EXTINF:-1 tvg-id="ElOcho.ar" tvg-logo="https://i.ibb.co/0yFbZj4/Captura.png" group-title="General",El Ocho (1080p) [Not 24/7]
https://ythlsgo.onrender.com/channel/UCYozHHDnLnQs2yc2k3t8cPA.m3u8
#########################################################################
#########################################################################
#########################################################################

#EXTINF:-1,ESPN Premium HD
http://209.45.101.38:7500/play/a0bu
#EXTINF:-1,TNT Sports HD
http://209.45.101.38:7500/play/a0aw
#EXTINF:-1,TYC Sports HD
http://209.45.101.38:7500/play/a0au


#EXTINF:-1,ESPN ARG HD
http://190.90.154.73:8080/play/a012/index.m3u8 
#EXTINF:-1,ESPN 2 HD
http://190.90.154.73:8080/play/a00y/index.m3u8
#EXTINF:-1,ESPN 3 HD
http://190.90.154.73:8080/play/a01x/index.m3u8
#EXTINF:-1,ESPN 4 HD
http://190.90.154.73:8080/play/a02s/index.m3u8
#EXTINF:-1,ESPN EXTRA HD
http://190.90.154.73:8080/play/a03f/index.m3u8
#EXTINF:-1,TyC Sports
http://190.90.154.73:8080/play/a062/index.m3u8
###
#EXTINF:-1,ESPN ARG
http://181.78.23.26:45000/play/a01i
#EXTINF:-1,ESPN 2
http://181.78.23.26:45000/play/a00m
#EXTINF:-1,ESPN 2 Latin
http://181.78.23.26:45000/play/a01h
#EXTINF:-1,ESPN 3
http://181.78.23.26:45000/play/a037
#EXTINF:-1,ESPN 4
http://181.78.23.26:45000/play/a025
#EXTINF:-1,ESPN CO
http://181.78.23.26:45000/play/a02p
###
#EXTINF:-1 tvg-id="" tvg-name="DIRECTV SPORT + EC" tvg-logo="" group-title="DEPORTE",DIRECTV SPORT + EC
http://redima.pro:8880/MOREIRAL/9512/685
#EXTINF:-1 tvg-id="" tvg-name="ESPN" tvg-logo="http://1000marcas.net/wp-content/uploads/2020/02/logo-ESPN.png" group-title="DEPORTE",ESPN
http://redima.pro:8880/MOREIRAL/9512/571
###
#EXTINF:-1,AMC HD
http://38.43.132.86:8000/play/a02l/index.m3u8
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

#EXTINF:-1,ESPN ARG
http://191.97.14.38:4000/play/a017/index.m3u8
#EXTINF:-1,ESPN 2 Latin
http://191.97.14.38:4000/play/a016/index.m3u8
#EXTINF:-1,ESPN 3
http://191.97.14.38:4000/play/a027/index.m3u8
#EXTINF:-1,ESPN 4 HD
http://191.97.14.38:4000/play/a04d/index.m3u8
#EXTINF:-1,ESPN CO
http://191.97.14.38:4000/play/a01p/index.m3u8
#EXTINF:-1,ESPN ARG HD
http://191.97.14.38:4000/play/a04g/index.m3u8
#EXTINF:-1,TyC
http://191.97.14.38:4000/play/a019/index.m3u8
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
#EXTINF:-1 group-title="Bics Variados",ESPN 2
http://181.78.105.146:2000/play/a063/index.m3u8
#EXTINF:-1 group-title="Bics Variados",ESPN
http://181.78.105.146:2000/play/a064/index.m3u8
#EXTINF:-1 group-title="Bics Variados",ESPN3
http://181.78.105.146:2000/play/a03n/index.m3u8
###
#EXTINF:-1 group-title="Bics DEPORTES", ESPN Extra  MX
http://home-playtv.com:8080/restreamhome/HUvCLa351719/21229
#EXTINF:-1 group-title="Bics DEPORTES", ESPN 1 PE
http://home-playtv.com:8080/restreamhome/HUvCLa351719/220727
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN ARG SD ►℗
http://home-playtv.com:8080/restreamhome/HUvCLa351719/219173
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN 1 PE HD ►℗
http://home-playtv.com:8080/restreamhome/HUvCLa351719/219172
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN ARG HD
http://home-playtv.com:8080/restreamhome/HUvCLa351719/219171
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN 1 MX HD
http://home-playtv.com:8080/restreamhome/HUvCLa351719/9380
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN 1 MX SD
http://home-playtv.com:8080/restreamhome/HUvCLa351719/185154
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN 2 AR
http://home-playtv.com:8080/restreamhome/HUvCLa351719/185666
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN 2 MX HD
http://home-playtv.com:8080/restreamhome/HUvCLa351719/36391
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN 3  AR HD
http://home-playtv.com:8080/restreamhome/HUvCLa351719/21220
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN 3 MX HD  ►℗
http://home-playtv.com:8080/restreamhome/HUvCLa351719/186774
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN Deportes SD
http://home-playtv.com:8080/restreamhome/HUvCLa351719/54094
#EXTINF:-1 group-title="Bics DEPORTES",DEP | ESPN Extra BRA
http://home-playtv.com:8080/restreamhome/HUvCLa351719/168997
#EXTINF:-1 group-title="Bics DEPORTES",DEP | FOX Deportes
http://home-playtv.com:8080/restreamhome/HUvCLa351719/36396
#EXTINF:-1 group-title="Bics DEPORTES",DEP | FOX Sports 2 ARG HD ►℗
http://home-playtv.com:8080/restreamhome/HUvCLa351719/19652
#EXTINF:-1 group-title="Bics DEPORTES",DEP | FOX Sports 2 HD BRA
http://home-playtv.com:8080/restreamhome/HUvCLa351719/48540
#EXTINF:-1 group-title="Bics DEPORTES",DEP | FOX Sports 2 MEX HD
http://home-playtv.com:8080/restreamhome/HUvCLa351719/19495
#EXTINF:-1 group-title="Bics DEPORTES",DEP | FOX Sports 3 ARG HD ►℗
http://home-playtv.com:8080/restreamhome/HUvCLa351719/19496
#EXTINF:-1 group-title="Bics DEPORTES",DEP | FOX Sports 3 HD MEX
http://home-playtv.com:8080/restreamhome/HUvCLa351719/9538
#EXTINF:-1 group-title="Bics DEPORTES",DEP | SKY Sports 16 HD
http://home-playtv.com:8080/restreamhome/HUvCLa351719/149063
#EXTINF:-1 group-title="Bics DEPORTES",DEP | TNT Sports CL
http://home-playtv.com:8080/restreamhome/HUvCLa351719/211363
#EXTINF:-1 group-title="Bics DEPORTES",DEP | TNT Sports ARG
http://home-playtv.com:8080/restreamhome/HUvCLa351719/36424
#EXTINF:-1 group-title="Bics DEPORTES",DEP | TNT Sports 3 HD
http://home-playtv.com:8080/restreamhome/HUvCLa351719/19638
#EXTINF:-1 group-title="Bics DEPORTES",DEP | TYC Sports Internacional HD
http://home-playtv.com:8080/restreamhome/HUvCLa351719/188939
###
#EXTINF:-1  group-title="Bics DEPORTES", FOX Sports 
http://stream.flynetwifi.com:1935/live/mobile-010/playlist.m3u8
#EXTINF:-1  group-title="Bics DEPORTES", ESPN 2
http://2hubs.ddns.net:25461/crAig1s/myG32Vd21@/63193
#EXTINF:-1  group-title="Bics DEPORTES", ESPN 3
http://2hubs.ddns.net:25461/crAig1s/myG32Vd21@/63194
###
#EXTINF:-1  group-title="Bics DEPORTES", FOX SPORTS PREMIUM SD
http://europass.site:8080/sebastianbenitezchapatan10/CDCBpNCuY7/252733
###
#EXTINF:-1 #EXTINF:-1  group-title="Bics DEPORTES", FOX SPORTS 3 SD
http://europass.site:8080/sebastianbenitezchapatan10/CDCBpNCuY7/981
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

