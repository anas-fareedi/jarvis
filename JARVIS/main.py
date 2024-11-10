import  speech_recognition as sr
import pyttsx3
import webbrowser

recognizer=sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__=="__main__":
    speak("initialize jarvis ")
    
    while True:
        try:
       
            with sr.Microphone() as source:
                print("listining")
                audio = recognizer.listen(source,timeout=3)
                
            print("recognizing..")
        
            try :
                command = recognizer.recognize_google(audio)
                print(command)
                
            except sr.UnknownValueError:
                print("Could not understand the audio.")
                speak("Sorry, I did not catch that.")
                
        except Exception as e:
             print("Error; {0}".format(e))
        