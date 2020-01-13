# reminder
This should be a program that remind a groupe of people via Email to Events.



# Specifications:
Config file with Email address and Names.\
Config file with Events an there repeats actions.\
The Email should contain a file for the easy input in a personal calender.\
  https://developers.google.com/calendar/v3/reference/events/import\
actual status / logging / save File, so it can run in crontab.\


# First Structure:
Class:
* Email Client
* Creating Event File
* Load/save Configurations
\
\
The Save File will be created from the config Files and the actual status.



# Need To Debug
If the "AttributeError: 'list' object has no attribute 'encode'"\
appeared from  "text = msg.as_string()", the msg['to'] does not accept lists