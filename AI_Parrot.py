# Author: Endri Dibra

# Below i call the required libraries
import speech_recognition as sp
from gtts import gTTS
from playsound import playsound


# Below i create my object and initialize in it, the Recognizer() method
recognizer = sp.Recognizer()

# The following code will run until an exception occurs
while True:

    try:

        # Using the required method to use computer's microphone
        # to take my speech from audio
        with sp.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic)

            # Converting my speech to text
            text = recognizer.recognize_google(audio)
            text = text.lower()

            # Initializing the type of audio and language
            audio = 'speech.mp3'
            language = "en"

            # Initializing input, language and speed
            sp = gTTS(text=text, lang=language, slow=False)

            # Saving input(text from speech) token from the user and playing it
            sp.save(audio)
            playsound(audio)

    except sp.UnknownValueError():

        # continues till an exception occurs
        recognizer = sp.Recognizer()

        continue
