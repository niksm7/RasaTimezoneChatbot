# RasaTimezoneChatbot
Rasa is a very powerful tool of python that helps in building bots using some nlu and python along.<br>
Rasa can be installed using the command:<br>
```pip install rasa```<br>

Once you have installed rasa you can create the basic rasa template using command<br>
```rasa init```<br>
If you are using my code you don't need to do this.<br>

Once you have got the basic template and made changes in it according to your needs we need to go to the basic template <br>
directory(in our case timezonebot) in two of the terminal windows.<br>

<b>First Window</b><br>
We need to run the action server as:<br>
```rasa run actions```<br>

<b>Second Window</b><br>
We can train the model as:<br>
```rasa train```<br>
Then to run the actual shell we do:<br>
```rasa shell```<br>

Inside the shell you can the bot about timezone of a particular city as example:<br>
* What is the time zone of London?<br>
* time zone of Mumbai<br>

Also if you just enter timezone without specifying the city it will ask you for the city name.<br>

Note : You can view how the bot approaches to a conclusion based on the confidence level using the command:<br>
```rasa shell nlu```<br>
And then type your question.
