import urllib2 
import twitter, datetime #Imports Twitter and time stamp

currentSession = open("/Users/zchild/Library/Application Support/Google/Chrome/Default/Current Session") #This finds the history or 'current session' folder for Google Chrome on the machine 
#This varies depending on which machine you are on
lastSession = currentSession.read() 
user = 3096330147 

file = open("MyKeys.txt") #This loads in my twitter credentials from my twitter credentials file 
credCut = file.readline().strip().split(",") #This reads through my 'MyKeys' and splits each section up that is sperated by a comma (much like the Chatbot exercise) 

start = lastSession.rfind("http") #The rfind looks at the most recent item in the browsing history - without this it woud find the oldest item in the history
end = lastSession.find(chr(0), start) 

url = lastSession[start:end] 
print(url)
urlfound = urllib2.urlopen(url) 
html = urlfound.read()

api = twitter.Api(consumer_key=credCut[0],consumer_secret=credCut[1],
		  access_token_key=credCut[2],access_token_secret=credCut[3]) 

titleStart = html.find("<title>") + len("<title>") 
titleEnd = html.find("</title>", titleStart)
theTitle = html[titleStart:titleEnd] 


time = datetime.datetime.utcnow() #Stores the timestamp in the variable time

response = api.PostUpdate( url + " at " + str(time) + " Title is: " + str(theTitle)) #The url is called along with text of my choice and the time 

