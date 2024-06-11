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
fi
if [ -z "$2" ]
then
    echo "No ip address of RobotPi supplied"
    echo "desktop-setup.sh [name] [ip]"
    exit 1
fi

name=$1
ip=$2

# Remove any prior ssh key associated with the robot, silently
ssh-keygen -R "$name" 2> /dev/null
ssh-keygen -R "$ip" 2> /dev/null

# Genereate a new ssh key for the robot and copy it to the robot
ssh-keygen;
ssh-copy-id "$name"@"$ip";

# Check if the robot is connected
if ssh -q -t "$name"@"$ip" 'mkdir -p run; exit';
then
    echo "RobotPi is connected"
else
    echo "RobotPi failed to connect, setup could not complete..."
    exit 1
fi

# if not installed before
if [ ! -f ~/.bashrc_camjam ]; then
    touch ~/.bashrc_camjam
    echo "if [ -f ~/.bashrc_camjam]; then
        . ~/.bashrc_camjam
    fi
    " >> ~/.bashrc
fi
if [ ! -d ~/Desktop/runonboot ]; then
    # Create a runonboot folder in the desktop directory
    mkdir -p ~/Desktop/runonboot
fi

    # Append function to bashrc_camjam
    # The function will copy the file to the robot and execute it
    # If the robot fails to connect, it will execute the file locally and put it in the runonboot folder
    echo "function runonrobot() {
        if ssh -q -o ConnectTimeout=1 -t \"$name\"@\"$ip\" 'mkdir -p run; exit';
        then
            echo \"RobotPi is connected, copying the file to the robot...\"
            scp -q \"\$1\" \"$name@$ip:~/run\"
            echo \"Running the file on the robot...\"
            ssh -t \"$name@$ip\" \"python3 ~/run/\$(basename \$1); exit\"
        else
            echo \"RobotPi failed to connect, running the file locally...\"
            rm -rf ~/Desktop/runonboot/*
            cp \"\$1\" ~/Desktop/runonboot/
            python3 ~/Desktop/runonboot/\$1
        fi
    }" > ~/.bashrc_camjam

    # Add "if there are any files in runonboot folder, execute them" to the bashrc
    echo "if [ -n \"\$(ls -A ~/Desktop/runonboot)\" ]; then
        python3 ~/Desktop/runonboot/*
    fi" >> ~/.bashrc_camjam

    # Source the bashrc to apply the changes
    source ~/.bashrc

    sudo apt-get install -y code