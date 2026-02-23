# -*- coding: utf-8 -*-
import sys
import urllib.parse
import xbmcgui
import xbmcplugin

# Získanie základných premenných od Kodi
_url = sys.argv[0]
_handle = int(sys.argv[1])

def get_url(**kwargs):
    """Vytvorí URL adresu pre prepojenie v menu"""
    return _url + '?' + urllib.parse.urlencode(kwargs)

def main_menu():
    """Vytvorí hlavné menu (priečinky)"""
    # SLOVENSKO
    li_sk = xbmcgui.ListItem(label='[B]Slovenské TV[/B]')
    url_sk = get_url(action='list_sk')
    xbmcplugin.addDirectoryItem(handle=_handle, url=url_sk, listitem=li_sk, isFolder=True)

    # ČESKO
    li_cz = xbmcgui.ListItem(label='[B]České TV[/B]')
    url_cz = get_url(action='list_cz')
    xbmcplugin.addDirectoryItem(handle=_handle, url=url_cz, listitem=li_cz, isFolder=True)

    xbmcplugin.endOfDirectory(_handle)

def list_sk():
    """Zoznam slovenských staníc"""
    # TV JOJ
    joj_url = "https://live.cdn.joj.sk/live/andromeda/joj-1080.m3u8"
    # Dôležité: Bez User-Agent a Referer to Jojka neprehrá!
    headers = "|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) &Referer=https://www.joj.sk/"
    
    li = xbmcgui.ListItem(label='TV JOJ')
    li.setArt({'thumb': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/TV_JOJ_logo_2015.png'})
    li.setInfo('video', {'title': 'TV JOJ Live', 'plot': 'Živé vysielanie TV JOJ'})
    li.setProperty('IsPlayable', 'true')
    
    xbmcplugin.addDirectoryItem(handle=_handle, url=joj_url + headers, listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(_handle)

def list_cz():
    """Zoznam českých staníc"""
    li = xbmcgui.ListItem(label='[I]České stanice pripravujeme...[/I]')
    xbmcplugin.addDirectoryItem(handle=_handle, url='', listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(_handle)

def router(paramstring):
    """Logika, ktorá rozhodne, čo sa má zobraziť"""
    params = dict(urllib.parse.parse_qsl(paramstring))
    
    if params:
        if params['action'] == 'list_sk':
            list_sk()
        elif params['action'] == 'list_cz':
            list_cz()
    else:
        main_menu()

if __name__ == '__main__':
    # Spustenie smerovača s parametrami od Kodi
    router(sys.argv[2][1:])
    
