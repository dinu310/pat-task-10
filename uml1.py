import random

class AudioFile:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.rating = 0

    def set_rating(self, new_rating):
        if 1 <= new_rating <= 5:
            self.rating = new_rating
        else:
            print('Invalid rating. Rating should be between 1 and 5.')

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.rating = 0
        self.audios = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def update_average_rating(self):
        total_rating = sum(audio.rating for audio in self.audios)
        self.rating = total_rating / len(self.audios) if len(self.audios) > 0 else 0

class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def add_playlist(self, playlist):
        self.playlists.append(playlist)

    def search_audio_by_name(self, name):
        for playlist in self.playlists:
            for audio in playlist.audios:
                if audio.name == name:
                    return audio
        return None

    def search_playlist_by_name(self, name):
        for playlist in self.playlists:
            if playlist.name == name:
                return playlist
        return None

# Example usage:
audio1 = AudioFile('Song 1', 'https://example.com/song1.mp3')
audio2 = AudioFile('Song 2', 'https://example.com/song2.mp3')

playlist1 = Playlist('Playlist 1', 'Pop')
playlist2 = Playlist('Playlist 2', 'Rock')

playlist1.add_audio(audio1)
playlist2.add_audio(audio2)

music_player = MusicPlayer()
music_player.add_playlist(playlist1)
music_player.add_playlist(playlist2)

# Randomly generate ratings for playlists and audios
for _ in range(3):
    random_playlist = random.choice(music_player.playlists)
    random_audio = random.choice(random_playlist.audios)
    random_playlist.update_average_rating()
    random_audio.set_rating(random.randint(1, 5))

# Display average ratings
for playlist in music_player.playlists:
    print(f"Playlist '{playlist.name}' - Average Rating: {playlist.rating:.2f}")
    for audio in playlist.audios:
        print(f"  Audio '{audio.name}' - Rating: {audio.rating}")
