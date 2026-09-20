#AI chat bot project 
#greetings with time 

import time
import datetime 

name = input("what is your name:")
currentTime= datetime.datetime.now().hour

if 5<= currentTime <=11:
   print( "Good Morning",name)
elif 11< currentTime <17:
   print(" Good Afternoon",name)
elif 17<= currentTime <=19:
   print("Good Evening",name)
else :
    print("Good night",name)

print("Welcome here I am your favourite chatbot mewmew ")
print(" You can ask me anything type hi to start the chat.")
print(" type bye to stop the chat")

#responses

responses = {
    "hello" : "Hi!How can I help you?",
    "how are you?": "I am good.How is your day going?",
    "I am fine"  : "good to hear that.",
    "what are you?" :"I am hear to chat with you",
    "what is your name?":"My name is mewmew.What is your name?",
    "bye" : "have a good day,bye bye."
}


#functioning on the bot's reply 

def replyOfbot(userQuestion):
    if userQuestion in responses:
        return responses[userQuestion]
    else:
      return "I am sorry to let you know that I have no answer for that."





#asking for user input and continue to chat till the user says bye.
while True:
  userInput = input("You:")
  userQuestion = userInput.lower()
  reply = replyOfbot(userQuestion)
  print("mewmew",reply)
 
  if userQuestion=="bye":
   
   break 

