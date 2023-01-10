#!/bin/sh
# Script to kick off Max performance on Nano
boost clocks
sudo jetson_clocks
# Kisk of fan to 1/2 speed
sudo sh -c 'echo 128 > /sys/devices/pwm-fan/target_pwm'
# Uncomment below if you want to start the jtop system monitor
#jtop