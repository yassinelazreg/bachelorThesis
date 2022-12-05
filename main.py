import os
from google.cloud import texttospeech_v1


# https://cloud.google.com/text-to-speech/docs/libraries
# global variable for the access-key
# path has to be adjusted
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"addPath"

# create a client instance
c = texttospeech_v1.TextToSpeechClient()


# choose text input that will be turned into speech
sentence = ''
text = texttospeech_v1.SynthesisInput(text=sentence)

# Select the voice and the language
speaker = texttospeech_v1.VoiceSelectionParams(
    name='en-US-Wavenet-A', language_code="en-US"
)

# choose file encoding type, speech rate, and pitch level
params = texttospeech_v1.AudioConfig(
    # https://cloud.google.com/text-to-speech/docs/reference/rpc/google.cloud.texttospeech.v1#audioencoding
    audio_encoding=texttospeech_v1.AudioEncoding.MP3,
    #speaking_rate=1.5    # increased speach rate by 50%
    pitch=-6              # decreased pitch by 6 semitones
)

# make TTS request with the chosen text input and speech parameters
speech = c.synthesize_speech(
    input=text, voice=speaker, audio_config=params
)


# The response's audio_content is binary.
with open(r"controlQuetsion.mp3", "wb") as out:
    # save the generated speech sample
    out.write(speech.audio_content)