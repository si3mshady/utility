import requests, pyttsx3,re
import speech_recognition as sr
from bs4 import BeautifulSoup as soup

#create class to parse user query into google search engine returning a result 

class GetGoogleResponse:
    def __init__(self,query):
        self.url_base='https://www.google.com/search?q='
        self.query=query
        self.markup=requests.get(self.url_base + self.query).content
        self.google_soup=soup(self.markup,'html.parser')
    def fetch_response(self):
        try:
            self.results=self.google_soup.findAll('div',{'class':'g'})  #key attribute that holds description of searched data in goole 
            return(self.results[0].text)
        except:
            return("Unable to locate an appropriate response for the query = {}".format(self.query))

def machine_speak(dialogue='What do you want to know?'):  
    ghost_in_machine = pyttsx3.init()
    ghost_in_machine.say(dialogue)
    ghost_in_machine.runAndWait()
  
def begin():        
    while True:
        recording = sr.Recognizer()      #initialize speech recognition    
        machine_speak()
        try:
            with sr.Microphone() as the_voice:  #activate microphone - use with clause to ensure mic is terminated when it detects no more voice input 
                audio_stream=recording.listen(the_voice)                         
            speech_to_text=recording.recognize_google(audio_stream)  #use google api to transcribe audio into text
        except:
            machine_speak('Unable to record from microphone. Terminating ')
            break
        if 'quit' in speech_to_text:
            machine_speak(dialogue='goodbye')
            break                 
        ggr=GetGoogleResponse(speech_to_text)
        response=ggr.fetch_response()
        response=re.sub(r'(http\S*)','',response)  #use regular expressions to clean up response.  Strip away any http string that may appear in response 
        machine_speak(dialogue=response)
        print(response)

begin()

#Python Projects/exerices - Using speech_recognition, text_to_speech and BeautifulSoup to create a primitive voice assistant returning search results from Google - wip Elliott Arnold  3-28-19 







