#!/bin/bash

# NOTES
# runonrobot [file]
# - ssh into robotpi
# - delete run folder on robotpi
# - copy $1 into robotpi
# - execute robotpi
# - exit ssh

# ssh-keygen
# ssh-copy-id piX@piX
# ssh piX
# mkdir run
# https://serverfault.com/questions/241588

# https://unix.stackexchange.com/questions/106480

# ssh -t piX 'python $1; exit'

# Edge case, if not connect then run code locally

# Check if RobotPi name argument exist
if [ -z "$1" ]
then
    echo "No name of RobotPi supplied"
    exit 1
fi

# Ask to provide an ip address of the robot
echo "Please provide the ip address of the robot: $1"
# shellcheck disable=SC2162
read ip_address

# Remove any prior ssh key associated with the robot, silently
ssh-keygen -R "$1" 2> /dev/null
ssh-keygen -R "$ip_address" 2> /dev/null

# Genereate a new ssh key for the robot and copy it to the robot
ssh-keygen;
ssh-copy-id "$1"@"$ip_address";

# Check if the robot is connected
if ssh -q -t "$1" 'mkdir -p run; exit';
then
    echo "RobotPi is connected"
else
    echo "RobotPi failed to connect, setup could not complete..."
    exit 1
fi

# if not installed before
if [ ! -d ~/Desktop/runonboot ]; then
    # Create a runonboot folder in the desktop directory
    mkdir -p ~/Desktop/runonboot

    # Append function to local bashrc
    # The function will copy the file to the robot and execute it
    # If the robot fails to connect, it will execute the file locally and put it in the runonboot folder
    echo "function runonrobot() {
        if ssh -q -o ConnectTimeout=1 -t \"$1\" 'mkdir -p run; exit';
        then
            scp \"\$1\" \"$1:~/run\"
            ssh -t \"$1\" \"python3 ~/run/\$1; exit\"
        else
            echo \"RobotPi failed to connect, running the file locally...\"
            rm -rf ~/Desktop/runonboot/*
            cp \"\$1\" ~/Desktop/runonboot/
            python3 ~/Desktop/runonboot/\$1
        fi
    }" >> ~/.bashrc

    # Add "if there are any files in runonboot folder, then open a new terminal and run the python files on boot" to the bashrc
    echo "if [ -n \"\$(ls -A ~/Desktop/runonboot)\" ]; then
        gnome-terminal -- python3 ~/Desktop/runonboot/*
    fi" >> ~/.bashrc

    # Source the bashrc to apply the changes
    source ~/.bashrc
fi