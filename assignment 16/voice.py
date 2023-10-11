from gtts import gTTS

def convert_text_to_speach(text,name):
    audio = gTTS(text)
    audio.save(f"assignment 16/{name}.mp3")

text_1 = input("Please enter your text 1: ")
text_2 = input("Please enter your text 2: ")
text_3 = input("Please enter your text 3: ")
name = input("Please enter name of voice: ")

if len(text_1) > len(text_2) and len(text_1) > len(text_3):
    convert_text_to_speach(text_1,name)

elif len(text_2) > len(text_1) and len(text_2) > len(text_3):
    convert_text_to_speach(text_2,name)

elif len(text_3) > len(text_1) and len(text_3) > len(text_2):
    convert_text_to_speach(text_3,name)