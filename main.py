# -*- coding: utf-8 -*-
import sys
import urllib.parse
import xbmcgui
import xbmcplugin

_handle = int(sys.argv[1])

def main_menu():
    # Kategória Slovensko
    li_sk = xbmcgui.ListItem(label='[B]SLOVENSKÉ STANICE[/B]')
    url_sk = sys.argv[0] + '?' + urllib.parse.urlencode({'mode': 'sk'})
    xbmcplugin.addDirectoryItem(handle=_handle, url=url_sk, listitem=li_sk, isFolder=True)

    # Kategória Česko
    li_cz = xbmcgui.ListItem(label='[B]ČESKÉ STANICE[/B]')
    url_cz = sys.argv[0] + '?' + urllib.parse.urlencode({'mode': 'cz'})
    xbmcplugin.addDirectoryItem(handle=_handle, url=url_cz, listitem=li_cz, isFolder=True)
    
    xbmcplugin.endOfDirectory(_handle)

def list_sk():
    # TV JOJ Link
    url = "https://live.cdn.joj.sk/live/andromeda/joj-1080.m3u8"
    headers = "|User-Agent=Mozilla/5.0&Referer=https://www.joj.sk/"
    
    li = xbmcgui.ListItem(label='TV JOJ')
    li.setInfo('video', {'title': 'TV JOJ'})
    li.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=_handle, url=url + headers, listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(_handle)

# Spúšťacia logika
params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
mode = params.get('mode')

if mode is None:
    main_menu()
elif mode == 'sk':
    list_sk()
    
