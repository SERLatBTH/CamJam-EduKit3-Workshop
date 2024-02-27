# Introduction
This is a repository for a custom workshop that utilizes an [Education Kit 3 from Cambridge Raspberry Jam](https://camjam.me/?page_id=1035).

# Setup the workshop
There are X steps to setup the workshop
1. Get all the parts for the robot as seen in [robotparts](robotparts.md) 
2. Setup the two Raspberry Pis, one with OS Lite to run the robot and one regular to run the desktop environment.
3. Print out the instructions to assemble and/or code the robot.

## Setting up the Raspberry Pis
We found it difficult for our workshop takers to plug in the robot to a screen every time they needed to change code. In addition to the hassle, the robot would still be on and the motors may still run, making the workshop takers to turn the batteries off and on every debug session. Not a good experience for our use case where the workshop takers are beginners to wiring and coding anything technical. Our solution, or comprimise, is to use two Raspberry Pis where one remote control the other through SSH.

### RobotPi (reciever)
Setting up the recieving Pi is quick and easy with the official [Raspberry Pi Imager](https://www.raspberrypi.com/software/) provided by the Raspberry Pi team.

1. In the imager select the "Raspberry Pi OS (other)" and then the Lite version. Select a storage to write to and you'll recieve a pop-up to edit customizable settings.  
2. Select to edit them and set the hostname, username and password to pi1. This is the only variable that will change depending on however many teams will participate in the workshop, change the variable to pi2, pi3, etc. Password could optionally be safer, but this is a small workshop on a private network.  
3. Configure the wireless LAN and locale settings to match.  
4. Switch to the next tab and enable SSH and to use password authentication.  
5. Save the settings and flash the storage with the new image.
6. When it is done plug the raspberry pi to a screen and log in (we had trouble setting it up with SSH without a first login)
7. Bonus; run `hostname -I` in the terminal and write down the given ip adress, this will be used in DesktopPi.
The RobotPi should all be setup for now :)

### DesktopPi (sender)
Setting up the sending Pi requires more steps. We use the same [Raspberry Pi Imager](https://www.raspberrypi.com/software/) as before, but this time we select the regular desktop OS instead of Lite.

1. Select the default Raspberry OS (typically the top most one) and select a storage to flash to.
2. In the customizable settings, remove the hostname and change the username/password to desktop1, desktop2, etc for each corresponding RobotPi.
3. Configure wireless LAN and locale settings to be the same as th ecorresponding RobotPis.
4. Disable the SSH setting in the other tab.
5. Flash the storage and when it is done connect a screen and log in.
6. Download or Transfer this git repository to the DesktopPi.
7. Go into `setup` directory and run ```chmod +x desktop-setup.sh; sudo ./desktop-setup.sh pi1``` It will install VS Code and add a function to `.bashrc` named "runonrobot" that will connect to pi1 and make it run the selected python file.
8. The script will ask you what ip address pi1 has, type in the answer recieved in step 7 of RobotPi above.
9. As a backup, if SSH would fail for whatever reason, there will be a "runonboot" folder on the desktop that will open a terminal and execute any python file on boot. This is to ensure our workshop participants can still run code by just swapping the sd card between DesktopPi and RobotPi.

## Building the robot

## Coding the robot


# TODO
- The DesktopPi should open visual studio code on boot in the correct directory with all files.