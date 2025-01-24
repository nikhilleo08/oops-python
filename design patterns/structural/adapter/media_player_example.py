# Target Interface
class MediaPlayer:
    def play(self, audio_type, file_name):
        pass

# Adaptee 1: MP3Player
class MP3Player:
    def play_mp3(self, file_name):
        print(f"Playing MP3 file: {file_name}")

# Adaptee 2: MP4Player
class MP4Player:
    def play_mp4(self, file_name):
        print(f"Playing MP4 file: {file_name}")

# Adaptee 3: VLCPlayer
class VLCPlayer:
    def play_vlc(self, file_name):
        print(f"Playing VLC file: {file_name}")

# Adaptee 3: VLCPlayer
class WMVPlayer:
    def play_wmv(self, file_name):
        print(f"Playing WMV file: {file_name}")

# Generic Adapter
class MediaAdapter(MediaPlayer):
    def __init__(self, player, play_method):
        self.player = player
        self.play_method = play_method

    def play(self, audio_type, file_name):
        # Dynamically call the appropriate play method
        play_func = getattr(self.player, self.play_method, None)
        if callable(play_func):
            play_func(file_name)
        else:
            print(f"Error: Unsupported method '{self.play_method}' for type '{audio_type}'")

# Client class: MediaPlayerClient
class MediaPlayerClient:
    def __init__(self):
        self.adapters = {}

    def register_adapter(self, audio_type, adapter: MediaPlayer):
        self.adapters[audio_type] = adapter

    def play(self, audio_type, file_name):
        adapter = self.adapters.get(audio_type)
        if adapter:
            adapter.play(audio_type, file_name)
        else:
            print(f"Error: No adapter found for audio type '{audio_type}'")

# Testing the Refactored Code
mp3_player = MP3Player()
mp4_player = MP4Player()
vlc_player = VLCPlayer()
wmv_player = WMVPlayer()

# Register adapters for different formats
client = MediaPlayerClient()
client.register_adapter("mp3", MediaAdapter(mp3_player, "play_mp3"))
client.register_adapter("mp4", MediaAdapter(mp4_player, "play_mp4"))
client.register_adapter("vlc", MediaAdapter(vlc_player, "play_vlc"))
client.register_adapter("mwv", MediaAdapter(wmv_player, "play_wmv"))

# Playing various media formats
client.play("mp3", "song.mp3")   # Playing MP3 file
client.play("mp4", "znmd.mp4")   # Playing MP4 file
client.play("vlc", "znmd.vlc")   # Playing VLC file
client.play("mwv", "znmd.mwv")   # Playing VLC file
client.play("avi", "znmd.avi")   # Error: No adapter found for audio type 'avi'
