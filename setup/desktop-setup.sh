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