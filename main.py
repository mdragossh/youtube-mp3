import youtube_dl as d


def download_song(link_to_song, **kwargs):
    with d.YoutubeDL(kwargs) as ydl:
        ydl.download([link_to_song])


if __name__ == '__main__':
    download_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with open('song_list.txt', 'r') as song_list:
        clear_char_from_links = map(lambda x: x.strip(), song_list.readlines())
        songs = filter(None, list(clear_char_from_links))

        for song in songs:
            download_song(song, **download_options)