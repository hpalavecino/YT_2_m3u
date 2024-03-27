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

#########################################################################
#########################################################################
#########################################################################
#EXTINF:-1,ES-PN Premium (AR) (i)
http://budtvlight.com:25461/bud-1883584/ac2a351b3d/38746
#EXTINF:-1,ES-PN | AR (i)
http://budtvlight.com:25461/bud-1883584/ac2a351b3d/37817
#EXTINF:-1,TyC Sports HD (i)
http://budtvlight.com:25461/bud-1883584/ac2a351b3d/46603
#EXTINF:-1,TYC Sports Internacional
http://budtvlight.com:25461/bud-1883584/ac2a351b3d/69636
###
#EXTINF:-1,Low | ESPN (Low)
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/3851
#EXTINF:-1,ARG: ESPN Pʳᵉᵐⁱᵘᵐ ʜᴅ
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/4938
#EXTINF:-1,ARG: ESPN ᴾᴿᴵᴹᴱᴿᴬ ᴬᴿᴳᴱᴺᵀᴵᴺᴬ
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/151113
#EXTINF:-1,ARG: TNT SPORTS ᴬᴿᴳᴱᴺᵀᴵᴺᴬ ᴴᴰ
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/131980
#EXTINF:-1,Sᴘᴏʀᴛs Sᴰᵀ | TNT SPORTS
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/132285
#EXTINF:-1,ARG: TNT SPORTS FHD
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/148458
#EXTINF:-1,ARG: TNT SPORTS ᴾᴿᴵᴹᴱᴿᴬ ᴬᴿᴳᴱᴺᵀᴵᴺᴬ
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/148459
#EXTINF:-1,Pᴀᴄᴋ Fᴜᴛʙᴏʟ ᴴᴰ | TNT SPORTS UHD ARG.
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/2688
#EXTINF:-1,ARG: TYC SPORTS ᴬᴿᴳᴱᴺᵀᴵᴺᴬ ᴴᴰ
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/125863
#EXTINF:-1,Sᴘᴏʀᴛs Sᴰᵀ  | TYC SPORTS
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/132284
#EXTINF:-1,ARG: TyC SPORTS ᴾᴿᴵᴹᴱᴿᴬ ᴬᴿᴳᴱᴺᵀᴵᴺᴬ
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/148456
#EXTINF:-1,ARG: TyC SPORTS INTERNACIONAL
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/148457
#EXTINF:-1,Pᴀᴄᴋ Fᴜᴛʙᴏʟ ᴴᴰ | TYC SPORTS
http://magmas5.com:8000/LocalRestreamIntercambio/GX3FMT14FH/137121
###
#EXTINF:-1,Espn 1 ARG (TV)(1080)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/166827
#EXTINF:-1,Espn Premium ARG (L)(720)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/154050
#EXTINF:-1,Espn Premium ARG (X)(1080)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/154049
#EXTINF:-1,ESPN Premium ARG (X)(1080)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/1528
#EXTINF:-1,Directv Sports 1 (ARG) (X)(1080)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/4668
#EXTINF:-1,TyC Sports INT (TV)(720)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/2076
#EXTINF:-1,TyC Sports INT (T)(720)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/27530
#EXTINF:-1,ARG-TNT Sports (L)(720)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/309414
#EXTINF:-1,ARG-TNT Sports (X)(720)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/153802
#EXTINF:-1,ARG-TYC Sports Local (X)(720)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/22127
#EXTINF:-1,ARG-TyC Sports Local (L)(SD)
http://tv.fuxxionpro.online:8080/Mar12334GFGFSDrddklqkd123/paD7AGyaLj/59813
###
#EXTINF:-1,#EXTINF:-1,EVENTOS STAR+ HD
http://magmas5.com:8000/1724T3XM15/G1V1DURAQR/152908
#EXTINF:-1,ESPN STAR+ FHD (SOLO EVENTOS)
http://magmas5.com:8000/1724T3XM15/G1V1DURAQR/160069
#EXTINF:-1,ESPN Premium 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/148460
#EXTINF:-1,ESPN Premium 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/148461
#EXTINF:-1,ESPN Premium 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/151113
#EXTINF:-1,TNT Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/131980
#EXTINF:-1,TNT Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/132285
#EXTINF:-1,TNT Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/148458
#EXTINF:-1,TNT Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/148459
#EXTINF:-1,TNT Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/2688
#EXTINF:-1,TyC Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/4945
#EXTINF:-1,TyC Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/132284
#EXTINF:-1,TyC Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/145440
#EXTINF:-1,TyC Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/145441
#EXTINF:-1,TyC Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/148455
#EXTINF:-1,TyC Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/148456
#EXTINF:-1,TyC Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/148457
#EXTINF:-1,TyC Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/133844
#EXTINF:-1,TyC Sports 1280x720
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/137121
#EXTINF:-1,ESPN 1920x1080
http://magmas5.com:8000/UK0NMK78C3/6XA15D0TF9/2823
###
#EXTINF:-1,TNT SPORTS  1280x720
http://magmas5.com:8000/rances123/9IFBBCRBIX/131980
#EXTINF:-1,ESPN PREMIUM  1280x720
http://magmas5.com:8000/rances123/9IFBBCRBIX/148461
#EXTINF:-1,ESPN  1280x720
http://magmas5.com:8000/rances123/9IFBBCRBIX/151113
#EXTINF:-1,ESPN 832x480
http://magmas5.com:8000/vidal130884/461G2TP4DW/4938
#EXTINF:-1,TNT SPORTS 1280x720
http://magmas5.com:8000/vidal130884/461G2TP4DW/131980
#EXTINF:-1,DIRECTV SPORTS 1280x720
http://magmas5.com:8000/vidal130884/461G2TP4DW/135642
#EXTINF:-1,TyC SPORTS INTERNACIONAL 1280x720
http://magmas5.com:8000/vidal130884/461G2TP4DW/148457
###
#EXTINF:-1,TNT SPORTS  1280x720
http://magmas5.com:8000/1724T3XM15/G1V1DURAQR/131980
#EXTINF:-1,TNT SPORTS ᴾᴿᴵᴹᴱᴿᴬ ᴬᴿᴳᴱᴺᵀᴵᴺᴬ
http://magmas5.com:8000/1724T3XM15/G1V1DURAQR/132285
#EXTINF:-1,TNT SPORTS
http://magmas5.com:8000/1724T3XM15/G1V1DURAQR/148459
#EXTINF:-1,TNT SPORTS UHD ARG.
http://magmas5.com:8000/1724T3XM15/G1V1DURAQR/2688
#EXTINF:-1,ESPN PREMIUM HD
http://magmas5.com:8000/1724T3XM15/G1V1DURAQR/148461
#EXTINF:-1,ESPN ARG 1280x720
http://181.78.23.26:45000/play/a01i
###
#EXTINF:-1,ESPN
http://redima.pro:8880/MOREIRAL/9512/571
###
#EXTINF:-1,ESPN
http://45.65.137.206:8000/play/a0gb/index.m3u8
#EXTINF:-1,History Channel
http://45.65.137.206:8000/play/a0fa/index.m3u8
###
#EXTINF:-1,ESPN
http://45.228.234.210:4000/play/a00r/index.m3u8
#EXTINF:-1,H2
http://45.228.234.210:4000/play/a02b/index.m3u8
###
#EXTINF:-1,ESPN HD
http://204.199.119.6:1012/play/a04h
#EXTINF:-1,HBO
http://204.199.119.6:1012/play/a09y
#EXTINF:-1,History 2 HD
http://204.199.119.6:1012/play/a01u
#EXTINF:-1,Paramount HD
http://204.199.119.6:1012/play/a019
###
#EXTINF:-1,ESPN
http://181.78.27.128:8000/play/a03q/index.m3u8
#EXTINF:-1,HBO
http://181.78.27.128:8000/play/a030/index.m3u8
#EXTINF:-1,HBO Family
http://181.78.27.128:8000/play/a029/index.m3u8
###
#EXTINF:-1,TyCSports 1920x1080
http://45.166.92.22:58001/play/a04d/index.m3u8
#EXTINF:-1,ESPN 544x480
http://181.78.105.146:6060/play/a036
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

