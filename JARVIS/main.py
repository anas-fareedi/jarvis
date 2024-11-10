import  speech_recognition as sr
import pyttsx3
import webbrowser

recognizer=sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__=="__main__":
    speak("welcome I am jarvis. vertual assistant of Mr. anas ... ")
    
    while True:
        try:
       
            with sr.Microphone() as source:
                print("listining")
                audio = recognizer.listen(source,timeout=5)
                
            print("recognizing..")
        
            try :
                command = recognizer.recognize_google(audio)
                print(command)
                
                if  "jarvis" in command.lower():
                    speak("hello sir . ")
                
                elif "command" in command.lower():
                    speak("i can do everything for you sir . give me command")
                    
                elif "google" in command.lower():
                    webbrowser.open("https://www.google.com")
                    speak("Opening Google.") 
                
                elif "brave" in command.lower():
                    webbrowser.open("https://www.brave.com")
                    speak("Opening brave.")
                    
                elif "instagram" in command.lower():
                    webbrowser.open("https://www.instagram.com")
                    speak("Opening instagram.")
                    
                elif "facebook" in command.lower():
                    webbrowser.open("https://www.facebook.com")
                    speak("Opening facebook.")
                    
                elif "youtube" in command.lower():
                    webbrowser.open("https://www.youtube.com")
                    speak("Opening youtube.")
                
                elif " linkedin" in command.lower():
                    webbrowser.open("https://www.linkedin.com")
                    speak("Opening linkedin .")
                    
            except sr.UnknownValueError:
                print("Could not understand the audio.")
                speak("Sorry, I did not catch that.")
                
        except Exception as e:
             print("Error; {0}".format(e))

print("I am always available for you ")
        