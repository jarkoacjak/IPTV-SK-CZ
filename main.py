import sys
import urllib.parse
import xbmcgui
import xbmcplugin
import xbmcaddon

# Získanie ID tvojho add-onu
ADDON_HANDLE = int(sys.argv[1])
ADDON_URL = sys.argv[0]

# Zoznam kanálov (tu si neskôr môžeš pridať ďalšie alebo ich načítavať z externého URL)
CHANNELS = [
    {
        "name": "RTVS Šport",
        "url": "https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8", # Toto je len testovací stream
        "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/RTVS_Sport_logo.svg/200px-RTVS_Sport_logo.svg.png"
    },
    {
        "name": "ČT24",
        "url": "https://ct24-live.ctcdn.net/hls/live/2024110/ct24/master.m3u8", # Príklad (môže vyžadovať CZ IP)
        "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/ČT24_logo.svg/200px-ČT24_logo.svg.png"
    }
]

def list_channels():
    """Vytvorí zoznam kanálov v menu Kodi."""
    for channel in CHANNELS:
        # Vytvorenie položky v zozname
        list_item = xbmcgui.ListItem(label=channel["name"])
        list_item.setArt({'icon': channel["icon"], 'thumb': channel["icon"]})
        list_item.setInfo('video', {'title': channel["name"], 'genre': 'Live TV'})
        
        # Nastavenie, že ide o video, ktoré sa dá spustiť
        list_item.setProperty('IsPlayable', 'true')
        
        # URL pre spustenie (v tomto prípade priamo link na stream)
        url = channel["url"]
        
        # Pridanie do zoznamu
        xbmcplugin.addDirectoryItem(handle=ADDON_HANDLE, url=url, listitem=list_item, isFolder=False)

    xbmcplugin.endOfDirectory(ADDON_HANDLE)

if __name__ == '__main__':
    # V tomto jednoduchom príklade rovno zobrazíme zoznam kanálov
    list_channels()

