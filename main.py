import sys
import urllib.parse
import xbmcgui
import xbmcplugin

# 1. Nastavenia doplnku
HANDLE = int(sys.argv[1])
BASE_URL = sys.argv[0]

def build_url(query):
    return BASE_URL + '?' + urllib.parse.urlencode(query)

def main_menu():
    """Vytvorí hlavné menu: Slovenské a České"""
    # SLOVENSKO
    url_sk = build_url({'mode': 'list_sk'})
    li_sk = xbmcgui.ListItem(label='[COLOR yellow][B]Slovenské TV[/B][/COLOR]')
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=url_sk, listitem=li_sk, isFolder=True)

    # ČESKO
    url_cz = build_url({'mode': 'list_cz'})
    li_cz = xbmcgui.ListItem(label='[COLOR blue][B]České TV[/B][/COLOR]')
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=url_cz, listitem=li_cz, isFolder=True)

    xbmcplugin.endOfDirectory(HANDLE)

def list_slovak_tv():
    """Zoznam slovenských staníc"""
    # TV JOJ (tvoj link)
    url_joj = "https://live.cdn.joj.sk/live/andromeda/joj-1080.m3u8"
    headers = "|User-Agent=Mozilla/5.0&Referer=https://www.joj.sk/"
    
    li = xbmcgui.ListItem(label='TV JOJ')
    li.setInfo('video', {'title': 'TV JOJ Live'})
    li.setProperty('IsPlayable', 'true')
    # Nastavenie ikony (voliteľné)
    li.setArt({'icon': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/TV_JOJ_logo_2015.png'})
    
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=url_joj + headers, listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(HANDLE)

def list_czech_tv():
    """Zoznam českých staníc"""
    # Tu si môžeš pridať ďalšie stanice neskôr
    li = xbmcgui.ListItem(label='ČT1 (Testovací link)')
    li.setInfo('video', {'title': 'ČT1'})
    li.setProperty('IsPlayable', 'true')
    
    # Príklad cesty, ak by si mal iný link
    test_url = "http://priklad.com/test.m3u8"
    
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=test_url, listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(HANDLE)

# --- LOGIKA SPÚŠŤANIA ---
# Rozoberie URL parametre, aby doplnok vedel, čo má zobraziť
params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
mode = params.get('mode')

if mode is None:
    # Ak sme práve otvorili doplnok, ukáž hlavné menu
    main_menu()
elif mode == 'list_sk':
    # Ak používateľ klikol na Slovenské TV
    list_slovak_tv()
elif mode == 'list_cz':
    # Ak používateľ klikol na České TV
    list_czech_tv()
    
