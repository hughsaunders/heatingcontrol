#Central Heating Control Project: Software Design Notes

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
