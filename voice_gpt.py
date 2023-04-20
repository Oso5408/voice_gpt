import openai
import speech_recognition as sr
import pyttsx3
from pyttsx3.voice import Voice
import time 
import os
import shutil  


# Initialize OpenAI API
openai.api_key = "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"
# Initialize the text to speech engine 
engine=pyttsx3.init()


def transcribe_audio_to_test(filename):
    recogizer=sr.Recognizer()
    with sr.AudioFile(filename)as source:
        audio=recogizer.record(source) 
    try:
        return recogizer.recognize_google(audio)
    except:
        print("skipping unkown error")

def generate_response(prompt):
    response= openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt + '; please answer in traditional chinese'},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
    ]
    )
    print('response:', response)
    return response["choices"][0]["message"]["content"]
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def print_text(text):
    print(text)
    speak_text(text)

def main():
    while True:
        #Waith for user say "genius"
        start_word = "Hey Anne".lower()
        print(f"Say '{start_word}' to start recording your question")
        with sr.Microphone() as source:
            recognizer=sr.Recognizer()
            recognizer.pause_threshold = 1
            print("start listening...")
            audio=recognizer.listen(source, timeout=2, phrase_time_limit=3)
            print("recognize_google...")
            try:
                transcription = recognizer.recognize_google(audio)
                print('transcription:', transcription)
                if transcription[0:3].lower()=="hey":
                    #record audio
                    filename ="input.wav"
                    with sr.Microphone() as source:
                        recognizer=sr.Recognizer()
                        source.pause_threshold=1
                        print_text("What's next?")
                        audio=recognizer.listen(source,phrase_time_limit=10,timeout=5)
                        with open(filename,"wb")as f:
                            f.write(audio.get_wav_data())
                            
                            
                        
                        
                    #transcript audio to test 
                    text=transcribe_audio_to_test(filename)
                    if text:
                        print(f"you said: {text}")
                        
                        #Generate the response
                        response = generate_response(text)
                        print(f"chat gpt 3 say: {response}")
                            
                        #read resopnse using GPT3
                        speak_text(response)
            except Exception as e:
                
                print("An error ocurred : {}".format(e))
if __name__=="__main__":
    path = os.getenv('PATH')
    print("Path is: %s" % (path,))
    print("shutil_which gives location: %s" % (shutil.which('flac')))
    voices = engine.getProperty('voices')
    for i, v in enumerate(voices):
        print('voices:', i, v)
    engine.setProperty('voice', 'com.apple.voice.compact.zh-HK.Sinji')
    # engine.setProperty('voice', 'com.apple.voice.compact.ja-JP.Kyoko')
    # engine.setProperty('voice', 'com.apple.eloquence.es-MX.Grandma')
    # engine.setProperty('rate', 180)
    main()