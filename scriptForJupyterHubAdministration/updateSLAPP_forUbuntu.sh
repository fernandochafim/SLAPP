#!/bin/bash

rm -R --force SLAPP
git clone https://github.com/terna/SLAPP

cd SLAPP
rm -R ./-pictures
rm SLAPP_Reference_Handbook.pdf
rm iRunShell.ipynb
mv iRunShell.ipynb.onlineVersion iRunShell.ipynb

cd ~/SLAPP/6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX
git clone https://github.com/terna/oligopoly

cd
