import sys
import xbmcgui
import xbmcplugin
import xbmcaddon

# 1. Získanie ID doplnku a adresy (handle)
ADDON_HANDLE = int(sys.argv[1])
ADDON = xbmcaddon.Addon()

def list_channels():
    """Vytvorí zoznam TV kanálov v Kodi"""
    
    # Príklad jedného kanála (napr. Jednotka)
    name = "Jednotka (SK)"
    url = "https://adresa-streamu.m3u8" # Sem pôjde tvoj zdroj
    thumb = "https://cesta-k-logu.png"

    # Vytvorenie položky v zozname
    list_item = xbmcgui.ListItem(label=name)
    list_item.setArt({'thumb': thumb, 'icon': thumb})
    
    # Nastavenie, že ide o video (stream)
    list_item.setProperty('IsPlayable', 'true')
    list_item.setInfo('video', {'title': name})

    # Pridanie do zoznamu
    xbmcplugin.addDirectoryItem(handle=ADDON_HANDLE, url=url, listitem=list_item, isFolder=False)

    # Ukončenie zoznamu
    xbmcplugin.endOfDirectory(ADDON_HANDLE)

if __name__ == '__main__':
    list_channels()
    
