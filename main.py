import os
from google.cloud import texttospeech_v1

# global variable for the access-key
# path has to be adjusted
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Users/yassinelazreg/PycharmProjects/pythonProject5/venv/text2speech-363215-594ba12ae6b8.json"

# Instantiates a client
client = texttospeech_v1.TextToSpeechClient()


# Set the text input to be synthesized
sentence = ''
synthesis_input = texttospeech_v1.SynthesisInput(text=sentence)

# Select the voice
voice = texttospeech_v1.VoiceSelectionParams(
    name='en-US-Wavenet-A', language_code="en-US"
)

# Select the type of audio file you want returned and set pitch and speaking rate
audio_config = texttospeech_v1.AudioConfig(
    # https://cloud.google.com/text-to-speech/docs/reference/rpc/google.cloud.texttospeech.v1#audioencoding
    audio_encoding=texttospeech_v1.AudioEncoding.MP3,
    #speaking_rate=1.5    # increased speach rate by 50%
    pitch=-6              # decreased pitch by 6 semitones
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)


# The response's audio_content is binary.
with open(r"controlQuetsion.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "voiceC-male-normal.mp3"')