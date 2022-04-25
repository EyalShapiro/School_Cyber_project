# https://docs.microsoft.com/en-us/answers/questions/539476/text-to-speech-poor-quality-python.html
from azure.cognitiveservices.speech import *
from azure.cognitiveservices.speech.audio import *


class AzureTTS:
    def __init__(self, subscription, region):
        self.speech_config = SpeechConfig(
            subscription=subscription, region=region)
        self.audio_config = AudioOutputConfig(use_default_speaker=True)
        self.synthesizer = SpeechSynthesizer(
            speech_config=self.speech_config, audio_config=self.audio_config)

    def constructAudio(self, text):
        ssml_string = """
                       <speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts"
                       xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
                       <voice name="en-US-AmberNeural"><prosody rate="0%" pitch="6%">
                       """
        ssml_string += text + '</prosody></voice></speak>'
        self.synthesizer.speak_ssml_async(ssml_string)


if __name__ == "__main__":
    testAzure = AzureTTS("key", "region")
    testAzure.constructAudio("Text here! This is a test run!")
