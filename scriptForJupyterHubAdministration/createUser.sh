#!/bin/bash

sudo useradd -d /home/$1 -m $1
sudo passwd $1
