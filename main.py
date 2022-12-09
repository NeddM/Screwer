
import audio_effects as ae
from pydub import AudioSegment

audio = AudioSegment.from_file("test.mp3")

octavas = -0.3

newSampleRate = int(audio.frame_rate * (2.0 ** octavas))
audio = audio._spawn(audio.raw_data, overrides={'frame_rate': newSampleRate})

audio.export("audioLento.mp3", format="mp3")
