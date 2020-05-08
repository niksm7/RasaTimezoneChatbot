# RasaTimezoneChatbot
Rasa is a very powerful tool of python that helps in building bots using some nlu and python along.
Rasa can be installed using the command:
```pip install rasa```
Once you have installed rasa you can create the basic rasa template using command
```rasa init```
If you are using my code you don't need to do this.
Once you have got the basic template and made changes in it according to your needs we need to go to the basic template 
directory(in our case timezonebot) in two of the terminal windows.
<b>First Window</b>
We need to run the action server as:
```rasa run actions```

<b>Second Window</b>
We can train the model as:
```rasa train```
Then to run the actual shell we do:
```rasa shell``

Inside the shell you can the bot about timezone of a particular city as example:
* What is the time zone of London?
* time zone of Mumbai

Also if you just enter # timezone without specifying the city it will ask you for the city name.

Note : You can view how the bot approaches to a conclusion based on the confidence level using the command:
```rasa nlu```
And then type your question.
