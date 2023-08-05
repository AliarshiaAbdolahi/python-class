from gtts import gTTS

def convert_text_to_speach(text):
    audio = gTTS(text)
    audio.save("voice.mp3")

text = input("Please enter your text: ")
convert_text_to_speach(text)