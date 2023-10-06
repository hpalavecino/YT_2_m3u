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

#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Canal 13
https://live-01-02-eltrece.vodgc.net/eltrecetv/index.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Canal 9
https://ythls.onrender.com/channel/UC6Qf8b2jcHHilkcr2wpQ9jA.m3u8
#EXTINF:-1 group-title="Varios",América TV (720p)
#EXTVLCOPT:http-user-agent=iPhone
#EXTVLCOPT:network-caching=1000
https://raw.githubusercontent.com/MachineSystems/archived_m3u8/main/america_hls.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TELEFE
https://cdn2.eco.cdn.moderntv.eu/econocable/stream/TELEFE/40-hls/live-media.m3u8?_cdn_attrs=account%3Deconocable%2Cresource%3DTELEFE_stream_te&_cdn_session=1269356507&_cdn_timestamp=1696774307&_cdn_token=ffc692f53a10bccfa0b990bac154fd9ba8fdecdc
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TN
https://live-01-01-tn.vodgc.net/TN24/index.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", A24
https://ythls.onrender.com/channel/UCR9120YBAqMfntqgRTKmkjQ.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", America Tucuman
https://ythls.onrender.com/channel/UCZ8sgVyD7HqDor8ujB-TZpg.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", C5N
https://ythls.onrender.com/channel/UCFgk2Q2mVO1BklRQhSv6p0w.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Canal 26
https://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Canal5 Tucuman
https://videohd.live:19360/8090/8090.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", CineAr
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Cronica TV
https://ythls.onrender.com/channel/UCT7KFGv6s2a-rh2Jq8ZdM1g.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", DeporTV
https://538d0bde28ccf.streamlock.net/live-cont.ar/deportv/playlist.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", El Ocho TV
https://ythls.onrender.com/channel/UCYozHHDnLnQs2yc2k3t8cPA.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", IP TV
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/5ee6e167-1167-4a85-9d8d-e08a3f55cff3.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", LN+
https://ythls.onrender.com/channel/UCba3hpU7EFBSk817y9qZkiA.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", Tec TV
https://tv.initium.net.ar:3939/live/tectvmainlive.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TN
https://ythls.onrender.com/channel/UCj6PcyLvpnIRT_2W_mwa9Aw.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TVP
https://cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all.m3u8
#EXTINF:-1 group-title="Varios" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/2/20/GTVBangladeshLogo.png/220px-GTVBangladeshLogo.png" tvg-id="", TyC
https://d3055hobuue3je.cloudfront.net/out/v1/188a8f3baf914a35868453bd5d0b0fd2/index_1.m3u8
#########################################################################
#########################################################################
#########################################################################
#EXTM3U
#EXTINF:-1,A&E HD
http://190.61.46.126:8000/play/a00l/index.m3u8
#EXTINF:-1,AMC HD
http://190.61.46.126:8000/play/a01l/index.m3u8
#EXTINF:-1,AXN HD
http://190.61.46.126:8000/play/a00o/index.m3u8
#EXTINF:-1,AZ Cinema HD
http://190.61.46.126:8000/play/a01s/index.m3u8
#EXTINF:-1,Animal Planet HD
http://190.61.46.126:8000/play/a01v/index.m3u8
#EXTINF:-1,Baby TV
http://190.61.46.126:8000/play/a033/index.m3u8
#EXTINF:-1,CABLENOTICIAS
http://190.61.46.126:8000/play/a02q/index.m3u8
#EXTINF:-1,CANAL UNO
http://190.61.46.126:8000/play/a03u/index.m3u8
#EXTINF:-1,CARACOL HD
http://190.61.46.126:8000/play/a03m/index.m3u8
#EXTINF:-1,CARTOONITO
http://190.61.46.126:8000/play/a03z/index.m3u8
#EXTINF:-1,CINE PREMIUN
http://190.61.46.126:8000/play/a00d/index.m3u8
#EXTINF:-1,CNN.
http://190.61.46.126:8000/play/a037/index.m3u8
#EXTINF:-1,Canal Capital
http://190.61.46.126:8000/play/a020/index.m3u8
#EXTINF:-1,Canal 13
http://190.61.46.126:8000/play/a02i/index.m3u8
#EXTINF:-1,Canal Institucional
http://190.61.46.126:8000/play/a03v/index.m3u8
#EXTINF:-1,Canal TRO
http://190.61.46.126:8000/play/a01y/index.m3u8
#EXTINF:-1,Caracol
http://190.61.46.126:8000/play/a01w/index.m3u8
#EXTINF:-1,Cartoon Network HD
http://190.61.46.126:8000/play/a01p/index.m3u8
#EXTINF:-1,Cinecanal HD
http://190.61.46.126:8000/play/a01k/index.m3u8
#EXTINF:-1,City TV
http://190.61.46.126:8000/play/a032/index.m3u8
#EXTINF:-1,Cristovisiðn
http://190.61.46.126:8000/play/a026/index.m3u8
#EXTINF:-1,DHE HD
http://190.61.46.126:8000/play/a03o/index.m3u8
#EXTINF:-1,DISCOVERY SCIEN
http://190.61.46.126:8000/play/a03w/index.m3u8
#EXTINF:-1,DISNEY JR
http://190.61.46.126:8000/play/a00c/index.m3u8
#EXTINF:-1,De PelŦcula
http://190.61.46.126:8000/play/a02y/index.m3u8
#EXTINF:-1,Discovery H&H HD
http://190.61.46.126:8000/play/a016/index.m3u8
#EXTINF:-1,Discovery HD
http://190.61.46.126:8000/play/a03p/index.m3u8
#EXTINF:-1,Discovery Kids HD
http://190.61.46.126:8000/play/a015/index.m3u8
#EXTINF:-1,Discovery Theater HD
http://190.61.46.126:8000/play/a017/index.m3u8
#EXTINF:-1,Discovery Turbo
http://190.61.46.126:8000/play/a02l/index.m3u8
#EXTINF:-1,Discovery World HD
http://190.61.46.126:8000/play/a01j/index.m3u8
#EXTINF:-1,Disney HD
http://190.61.46.126:8000/play/a00w/index.m3u8
#EXTINF:-1,E!
http://190.61.46.126:8000/play/a03x/index.m3u8
#EXTINF:-1,ESPN
http://190.61.46.126:8000/play/a00b/index.m3u8
#EXTINF:-1,ESPN 2 HD
http://190.61.46.126:8000/play/a00s/index.m3u8
#EXTINF:-1,ESPN 3 HD
http://190.61.46.126:8000/play/a00y/index.m3u8
#EXTINF:-1,ESPN 4 HD
http://190.61.46.126:8000/play/a01a/index.m3u8
#EXTINF:-1,ESPN EXTRA HD
http://190.61.46.126:8000/play/a01m/index.m3u8
#EXTINF:-1,ESPN HD
http://190.61.46.126:8000/play/a00u/index.m3u8
#EXTINF:-1,EWTN
http://190.61.46.126:8000/play/a047/index.m3u8
#EXTINF:-1,El Gourmet
http://190.61.46.126:8000/play/a02m/index.m3u8
#EXTINF:-1,El Gourmet HD
http://190.61.46.126:8000/play/a013/index.m3u8
#EXTINF:-1,Enlace
http://190.61.46.126:8000/play/a025/index.m3u8
#EXTINF:-1,Europa Europa
http://190.61.46.126:8000/play/a02e/index.m3u8
#EXTINF:-1,FOX Sports 2 HD
http://190.61.46.126:8000/play/a01b/index.m3u8
#EXTINF:-1,FX HD
http://190.61.46.126:8000/play/a01f/index.m3u8
#EXTINF:-1,Film&Arts
http://190.61.46.126:8000/play/a024/index.m3u8
#EXTINF:-1,Fox Sports 1 HD
http://190.61.46.126:8000/play/a03q/index.m3u8
#EXTINF:-1,Fox Sports 3 HD
http://190.61.46.126:8000/play/a00z/index.m3u8
#EXTINF:-1,GOLDEN
http://190.61.46.126:8000/play/a040/index.m3u8
#EXTINF:-1,HBO 2 HD
http://190.61.46.126:8000/play/a01t/index.m3u8
#EXTINF:-1,HBO Family
http://190.61.46.126:8000/play/a03d/index.m3u8
#EXTINF:-1,HBO Family HD
http://190.61.46.126:8000/play/a03s/index.m3u8
#EXTINF:-1,HBO HD
http://190.61.46.126:8000/play/a01n/index.m3u8
#EXTINF:-1,HBO MUNDI
http://190.61.46.126:8000/play/a02z/index.m3u8
#EXTINF:-1,HBO Plus
http://190.61.46.126:8000/play/a03f/index.m3u8
#EXTINF:-1,HBO Signature
http://190.61.46.126:8000/play/a03g/index.m3u8
#EXTINF:-1,HBO XTREME
http://190.61.46.126:8000/play/a03e/index.m3u8
#EXTINF:-1,HBO XTREME HD
http://190.61.46.126:8000/play/a03t/index.m3u8
#EXTINF:-1,HGTV
http://190.61.46.126:8000/play/a02k/index.m3u8
#EXTINF:-1,HOGAR TV
http://190.61.46.126:8000/play/a044/index.m3u8
#EXTINF:-1,HTV
http://190.61.46.126:8000/play/a02o/index.m3u8
#EXTINF:-1,History 2 HD
http://190.61.46.126:8000/play/a03r/index.m3u8
#EXTINF:-1,History Channel HD
http://190.61.46.126:8000/play/a00k/index.m3u8
#EXTINF:-1,ID HD
http://190.61.46.126:8000/play/a011/index.m3u8
#EXTINF:-1,Kanal D Drama HD
http://190.61.46.126:8000/play/a01o/index.m3u8
#EXTINF:-1,LA KALLE
http://190.61.46.126:8000/play/a00a/index.m3u8
#EXTINF:-1,Las Estrellas
http://190.61.46.126:8000/play/a02n/index.m3u8
#EXTINF:-1,Las Estrellas HD
http://190.61.46.126:8000/play/a03n/index.m3u8
#EXTINF:-1,Lifetime
http://190.61.46.126:8000/play/a02u/index.m3u8
#EXTINF:-1,Lolly Kids HD
http://190.61.46.126:8000/play/a049/index.m3u8
#EXTINF:-1,Love Nature HD
http://190.61.46.126:8000/play/a03i/index.m3u8
#EXTINF:-1,MAS CHIC
http://190.61.46.126:8000/play/a043/index.m3u8
#EXTINF:-1,MTV
http://190.61.46.126:8000/play/a036/index.m3u8
#EXTINF:-1,MTV HD
http://190.61.46.126:8000/play/a03l/index.m3u8
#EXTINF:-1,NTN 24
http://190.61.46.126:8000/play/a02p/index.m3u8
#EXTINF:-1,Nat Geo HD
http://190.61.46.126:8000/play/a01i/index.m3u8
#EXTINF:-1,Nuestra Tele
http://190.61.46.126:8000/play/a02h/index.m3u8
#EXTINF:-1,Paramount HD
http://190.61.46.126:8000/play/a01q/index.m3u8
#EXTINF:-1,Pasiones
http://190.61.46.126:8000/play/a02b/index.m3u8
#EXTINF:-1,Pasiones HD
http://190.61.46.126:8000/play/a00v/index.m3u8
#EXTINF:-1,Playboy HD
http://190.61.46.126:8000/play/a01d/index.m3u8
#EXTINF:-1,RCN HD
http://190.61.46.126:8000/play/a01h/index.m3u8
#EXTINF:-1,RCN SD
http://190.61.46.126:8000/play/a02g/index.m3u8
#EXTINF:-1,RUMBA TV
http://190.61.46.126:8000/play/a009/index.m3u8
#EXTINF:-1,STAR CHANNEL HD
http://190.61.46.126:8000/play/a00t/index.m3u8
#EXTINF:-1,Seæal Colombia
http://190.61.46.126:8000/play/a02f/index.m3u8
#EXTINF:-1,Sony HD
http://190.61.46.126:8000/play/a00m/index.m3u8
#EXTINF:-1,Space HD
http://190.61.46.126:8000/play/a00p/index.m3u8
#EXTINF:-1,Studio Universal HD
http://190.61.46.126:8000/play/a01r/index.m3u8
#EXTINF:-1,Sun Channel
http://190.61.46.126:8000/play/a02v/index.m3u8
#EXTINF:-1,Sun Channel HD
http://190.61.46.126:8000/play/a014/index.m3u8
#EXTINF:-1,TELEHIT
http://190.61.46.126:8000/play/a041/index.m3u8
#EXTINF:-1,TELEMUNDO
http://190.61.46.126:8000/play/a008/index.m3u8
#EXTINF:-1,TELENOSTALGIA
http://190.61.46.126:8000/play/a042/index.m3u8
#EXTINF:-1,TELEVEN
http://190.61.46.126:8000/play/a045/index.m3u8
#EXTINF:-1,TLC
http://190.61.46.126:8000/play/a035/index.m3u8
#EXTINF:-1,TLNOVELAS
http://190.61.46.126:8000/play/a007/index.m3u8
#EXTINF:-1,TLT
http://190.61.46.126:8000/play/a048/index.m3u8
#EXTINF:-1,TNT HD
http://190.61.46.126:8000/play/a00x/index.m3u8
#EXTINF:-1,TNT Novelas HD
http://190.61.46.126:8000/play/a03h/index.m3u8
#EXTINF:-1,TNT Series
http://190.61.46.126:8000/play/a03c/index.m3u8
#EXTINF:-1,TNT Series HD
http://190.61.46.126:8000/play/a01e/index.m3u8
#EXTINF:-1,TRU TV HD
http://190.61.46.126:8000/play/a012/index.m3u8
#EXTINF:-1,TV AGRO
http://190.61.46.126:8000/play/a046/index.m3u8
#EXTINF:-1,Teleantioquia
http://190.61.46.126:8000/play/a031/index.m3u8
#EXTINF:-1,Telecafe
http://190.61.46.126:8000/play/a01z/index.m3u8
#EXTINF:-1,Telecaribe
http://190.61.46.126:8000/play/a01x/index.m3u8
#EXTINF:-1,TelefØ
http://190.61.46.126:8000/play/a02r/index.m3u8
#EXTINF:-1,Telepacifico
http://190.61.46.126:8000/play/a030/index.m3u8
#EXTINF:-1,Tooncast
http://190.61.46.126:8000/play/a034/index.m3u8
#EXTINF:-1,UNIVERSAL CHANNEL HD
http://190.61.46.126:8000/play/a019/index.m3u8
#EXTINF:-1,UNIVISION
http://190.61.46.126:8000/play/a006/index.m3u8
#EXTINF:-1,V PLUS
http://190.61.46.126:8000/play/a005/index.m3u8
#EXTINF:-1,Warner Channel HD
http://190.61.46.126:8000/play/a00n/index.m3u8
#EXTINF:-1,Win Sports HD
http://190.61.46.126:8000/play/a00r/index.m3u8
#EXTINF:-1,Win Sports+ HD
http://190.61.46.126:8000/play/a01u/index.m3u8
#EXTINF:-1,ZOOMOO
http://190.61.46.126:8000/play/a03y/index.m3u8
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
