from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3(
    "./music/Different Heaven & EH!DE - My Heart [NCS Release].mp3"
)
print("Playing...")
play(song)
