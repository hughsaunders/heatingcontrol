#Central Heating Control Project

The aim of this project is for it to one day control my home central heating. 
There will be a few Rasberry Pis (or similar) collecting temperatures around the house, and one turning the heating on and off via a relay (connected as a thermostat would be).  

This application will collect and store the data from the probes, and decide when to turn the heating on/off. It will also query google calendar to get the current requirements for heating (minimum temperature etc). 


##Django App

Models
  - TempRecording
    - ID
    - Timestamp
    - Temperature
    - ProbeID
  - Probe
    - ID
    - Name
    - IP
    - Location
    - Sensor Type

##Time based events
Cron task to kick off django every few minutes. Flow:

- Check google calendar, if event:
  -	Retrieve temperature from event
  - Retrieve strategy from event
  - turn heating on / off if necessary according to strategy

##Data Collection
Temp probes hit django url to record current temperature in their location

##Calendar Entries
Temperature strategies vary by time of day - specify in calendar entry
EG:
  - Night:	temp=15 probe=bedroom 
  - Day:	temp=18 

If probe not specified, average is used. 
If temp not specified use default, probably 15. 
If no event, use frost protection temp = 3.
