# -*- coding: utf-8 -*-
import sys
import urllib.parse
import xbmcgui
import xbmcplugin

_url = sys.argv[0]
_handle = int(sys.argv[1])

def get_url(**kwargs):
    return _url + '?' + urllib.parse.urlencode(kwargs)

def main_menu():
    # Slovensko
    li = xbmcgui.ListItem(label='[B]Slovenské TV[/B]')
    xbmcplugin.addDirectoryItem(handle=_handle, url=get_url(action='sk'), listitem=li, isFolder=True)
    # Česko
    li = xbmcgui.ListItem(label='[B]České TV[/B]')
    xbmcplugin.addDirectoryItem(handle=_handle, url=get_url(action='cz'), listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(_handle)

def list_sk():
    url = "https://live.cdn.joj.sk/live/andromeda/joj-1080.m3u8"
    headers = "|User-Agent=Mozilla/5.0&Referer=https://www.joj.sk/"
    li = xbmcgui.ListItem(label='TV JOJ')
    li.setInfo('video', {'title': 'TV JOJ Live'})
    li.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=_handle, url=url + headers, listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(_handle)

if __name__ == '__main__':
    params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
    if not params:
        main_menu()
    elif params.get('action') == 'sk':
        list_sk()
        
