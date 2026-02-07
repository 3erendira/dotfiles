#!/bin/sh
# Script that prevents the annoying shutdown check
# Until they add --disable-shutdown-check back or an equivalent, this is necessary

rm -rf /home/$USER/.config/obs-studio/.sentinel
obs --startreplaybuffer 
