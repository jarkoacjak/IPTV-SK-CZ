# -*- coding: utf-8 -*-
import sys
import urllib.parse
import xbmcgui
import xbmcplugin

# 1. Získanie ID a URL doplnku
HANDLE = int(sys.argv[1])
BASE_URL = sys.argv[0]

def build_url(query):
    """Pomocná funkcia na vytváranie odkazov v menu"""
    return BASE_URL + '?' + urllib.parse.urlencode(query)

def main_menu():
    """Hlavná obrazovka: Výber Slovensko alebo Česko"""
    # SLOVENSKO
    li_sk = xbmcgui.ListItem(label='[B]SLOVENSKÉ STANICE[/B]')
    url_sk = build_url({'mode': 'list_sk'})
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=url_sk, listitem=li_sk, isFolder=True)

    # ČESKO
    li_cz = xbmcgui.ListItem(label='[B]ČESKÉ STANICE[/B]')
    url_cz = build_url({'mode': 'list_cz'})
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=url_cz, listitem=li_cz, isFolder=True)

    xbmcplugin.endOfDirectory(HANDLE)

def list_slovak_tv():
    """Zoznam slovenských staníc"""
    # TV JOJ
    joj_url = "https://live.cdn.joj.sk/live/andromeda/joj-1080.m3u8"
    # Dôležité hlavičky pre Jojku
    headers = "|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) &Referer=https://www.joj.sk/"
    
    li = xbmcgui.ListItem(label='TV JOJ')
    li.setInfo('video', {'title': 'TV JOJ Live'})
    li.setProperty('IsPlayable', 'true')
    # Pridanie loga (voliteľné)
    li.setArt({'thumb': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/TV_JOJ_logo_2015.png'})
    
    xbmcplugin.addDirectoryItem(handle=HANDLE, url=joj_url + headers, listitem=li, isFolder=False)
    
    xbmcplugin.endOfDirectory(HANDLE)

def list_czech_tv():
    """Zoznam českých staníc (zatiaľ prázdny)"""
    li = xbmcgui.ListItem(label='[I]Tu zatiaľ nič nie je[/I]')
    xbmcplugin.addDirectoryItem(handle=HANDLE, url='', listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(HANDLE)

# 2. Logika prepínania medzi menu (Routing)
params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
mode = params.get('mode')

if mode is None:
    main_menu()
elif mode == 'list_sk':
    list_slovak_tv()
elif mode == 'list_cz':
    list_czech_tv()
    
