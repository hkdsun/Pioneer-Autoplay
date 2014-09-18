import getpass
import sys
import telnetlib

HOST = "192.168.0.100" #Reserve this address through your router
PORT = 8102 #May be different for your receiver. see readme.

tn = telnetlib.Telnet(HOST, PORT) #Open telnet session

tn.write("PO\r\n") #Power on
tn.write("?P\r\n") #Get power status
if(tn.expect(["PWR0\r\n"], 1)[0] == 0): #Once successfully on, report back
    print "Pioneer succesfully on"
while 1:
    tn.write("VD\r\n") #Lower the volume to 0
    tn.write("?VOL\r\n")  
    if(tn.expect(["VOL000\r\n"], 0.2)[0] == 0):
        print "Volume set to zero"
        break
while 1:
    tn.write("VU\r\n") #Raise up volume to desired level step-by-step
    tn.write("?VOL\r\n")
    if(tn.expect(["VOL029\r\n"], 1)[0] == 0): #Careful when testing this part
        print "Volume set to 14"
        break
tn.write("45FN\r\n") #Set input to number 45 (Favourites in my case)
tn.write("?FN\r\n")
if(tn.expect(["FN45\r\n"],1)[0] == 0):
    print "Favourites Loaded"
tn.write("30PB\r\n") #Play now
print "Radio playing now"
tn.close() #Close telnet connection