
import concurrent.futures
from utils import *

if __name__ == '__main__':

    radios_list = [
        ("https://61115b0a477b5.streamlock.net:8443/chamgeifm/chamgeifm/playlist.m3u8", "Chamgei fm"),
        ("https://61115b0a477b5.streamlock.net:8443/inoorofm/inoorofm/playlist.m3u8", "inooro fm"),
        ("https://61115b0a477b5.streamlock.net:8443/mulembefm/mulembefm/playlist.m3u8", "mulembe fm"),
        ("https://61115b0a477b5.streamlock.net:8443/wimwarofm/wimwarofm/playlist.m3u8", "wimwaro fm"),
        ("https://61115b0a477b5.streamlock.net:8443/hot96fm/hot96fm/playlist.m3u8", "hot 96 fm"),
        ("https://61115b0a477b5.streamlock.net:8443/radiocitizen/radiocitizen/playlist.m3u8", "radio citizen"),
        ("https://61115b0a477b5.streamlock.net:8443/musyifm/musyifm/playlist.m3u8", "musyi fm"),
        ("https://61115b0a477b5.streamlock.net:8443/muugafm/muugafm/playlist.m3u8", "muuga fm"),
        ("https://61115b0a477b5.streamlock.net:8443/egesafm/egesafm/playlist.m3u8", "egesa fm"),
        ("https://61115b0a477b5.streamlock.net:8443/sulwefm/sulwefm/playlist.m3u8", "sulwe fm"),
        ("https://61115b0a477b5.streamlock.net:8443/ramogifm/ramogifm/playlist.m3u8", "ramogi fm"),
        ("https://61115b0a477b5.streamlock.net:8443/vuukafm/vuukafm/playlist.m3u8", "vuuka fm")
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as excecutor:
        excecutor.map(record_radio_station, radios_list)































