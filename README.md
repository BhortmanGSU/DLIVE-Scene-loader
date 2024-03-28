# DLIVE-Scene-loader
  This is a script I made to load scenes on our Allen and Heath DLive. It's setup for scene 1-128.

# Requirements 
1: You must have Allen and Heath MIDI Control installed: https://www.allen-heath.com/hardware/controllers/midi-control/resources/
   I would install it to run on startup. You'll select your device, the protocol is MIDI thru,tcp/ip and connect. It should connect at startup from now on. 

2: Python 3.11

3: Install mido          pip install mido

4: you'll need to open the file in notepad and adjust this part for your script:

# Scene number to recall
scene_number = 25  # Replace with your scene number 1-128

# To do
  Figure out how to conect directly to the console 
