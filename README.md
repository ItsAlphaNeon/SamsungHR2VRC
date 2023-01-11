

# Samsung Wearable Heart Rate to VRChat - OSC
A simple application to send your heartrate from a Samsung Wearable device to VRChat through OSC. This can be used to control items and animation on your avatar, as well as a wide range of things.
## Features

- Custom time delays for sending HR to VRChat
- Choose the minimum and maximum values to calculate the float values
- Configure a custom port to recieve HR data from
- Easy to use GUI
- Persistant Settings


## Installation

* Extract the current release .zip to anywhere on your PC
* Open the folder you extracted and run `HRServer.exe`
* You may want to create a shortcut to this file for easy access when you launch VRChat
That is all that is needed for the PC side. Go to the Samsung Wearable store and download the app `HeartRateToWeb`
* Open the app on the watch, and **ensure that the watch is connected to Wi-Fi and not Bluetooth**. This will prevent the server application from seeing your device.
* Enter the same port you enter in the GUI, and double check the IP.
* When you are ready to begin transmitting, start VRChat and click the `Start` button on the application.
* The app should connect, and begin transmitting OSC messages at your defined rate
    
## Acknowledgements / Credits

 - [Wearable HR Server code forked from loic2665](https://github.com/loic2665/HeartRateToWeb)
 - [Inspiration From Here](https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7)


## Roadmap

- Both Integer and Float value support, with options to toggle between them

- The option to start up with VRChat automatically

- Built in port testing and troubleshooting


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

