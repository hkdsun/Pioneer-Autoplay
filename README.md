Pioneer-Autoplay
================

If you are in love with a radio station like [Radio Paradise](www.radioparadise.com) like I am and you want it to play on your Pioneer receiver 24/7 then there is a solution.

This hack exploits Pioneer's Telnet capable receivers. So, the first step would be to try to find out the port on which your receiver can create a telnet session.

Use the command
`sudo nmap -n -PN -sT -sU -p- remote_host`
,where `remote_host` is your receiver's IP, to find out your telnet port.

This is by no means a secure solution. So, use it with security in mind.

#Requirements
* A network-enabled Pioneer receiver (tested on VSX-823); add your station as a favorite on your device [this website is your friend](pioneer.vtuner.com)
* A home server running [EventGhost](http://www.eventghost.org)
* Access to your home server outside your network (optional); this can be done with port-forwarding and a [dynamic DNS](www.noip.com)
* An Android device with [Tasker](tasker.dinglisch.net) installed (optional automation)

#Usage
The purpose of this repository is to provide reliable code that can interact with your Pioneer receiver. There are plenty of resources on EventGhost, Tasker, and accessing your host remotely

#Tutorial
* Open up EG and right-click Autostart in your Configuration Tree
* Choose Plugin > Other > Webserver
* Setup webserver on port of your choice and enable that port on your router
* Generate an event by browsing to `http://user:password@serveraddress:port/?EventName` for example: `http://admin:1234@localhost:80/?PioneerON`
	- user, password, and port are setup in eventghost's webserver plugin
	- you will get a 404 when you go to the URLs above but an event is generated regardless
	- you could bind it to a simple html document if you wish. see the webserver plugin support
* You should now see an event logged `HTTP.PioneerON []` in your eventghost log
* Add a new macro (e.g. `Turn Pioneer ON`) by right-clicking your configuration tree and drag the generated event (e.g. `HTTP.PioneerON []`) into it
* Right-click the macro `Turn Pioneer ON` and select "Add Action > EventGhost > Python Script" and paste the code
* Test your macro by right-clicking and selecting "Execute Item"
* Browsing to `http://admin:1234@localhost:80/?PioneerON` will now trigger the macro
* Use an automation application like Tasker, where HTTP Get is supported, to trigger your macro