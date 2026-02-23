import sys
import urllib.parse
import xbmcgui
import xbmcplugin

# Základné nastavenia
HANDLE = int(sys.argv[1])
BASE_URL = sys.argv[0]

def build_url(query):
    return BASE_URL + '?' + urllib.parse.urlencode(query)

def main_menu():
    """Hlavná obrazovka s výberom krajiny"""
    # SLOVENSKO
    url_sk = build_url({'mode': 'list_sk'})
    li_sk = xbmcgui.ListItem(label='[B]Slovenské TV[/B]')
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=url_sk, listitem=li_sk, isFolder=True)

    # ČESKO
    url_cz = build_url({'mode': 'list_cz'})
    li_cz = xbmcgui.ListItem(label='[B]České TV[/B]')
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=url_cz, listitem=li_cz, isFolder=True)

    xbmcplugin.endOfDirectory(HANDLE)

def list_slovak_tv():
    """Zoznam slovenských staníc"""
    # TV JOJ (ten tvoj link)
    url = "https://live.cdn.joj.sk/live/andromeda/joj-1080.m3u8"
    headers = "|User-Agent=Mozilla/5.0&Referer=https://www.joj.sk/"
    
    li = xbmcgui.ListItem(label='TV JOJ')
    li.setInfo('video', {'title': 'TV JOJ'})
    li.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=url + headers, listitem=li, isFolder=False)
    
    xbmcplugin.endOfDirectory(HANDLE)

def list_czech_tv():
    """Zoznam českých staníc"""
    # Tu si neskôr pridáš české linky podobne ako Jojku
    li = xbmcgui.ListItem(label='ČT1 (Príklad)')
    li.setInfo('video', {'title': 'ČT1'})
    li.setProperty('IsPlayable', 'true')
    # Zatiaľ prázdny link
    xbmcplugin.addDirectoryItem(handle=HANDLE, url="http://priklad.cz/ct1.m3u8", listitem=li, isFolder=False)
    
    xbmcplugin.endOfDirectory(HANDLE)

# Logika smerovania (Routing)
params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
mode = params.get('mode')

if mode is None:
    main_menu()
elif mode == 'list_sk':
    list_slovak_tv()
elif mode == 'list_cz':
    list_czech_tv()
    
