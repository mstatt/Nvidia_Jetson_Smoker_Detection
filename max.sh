#!/bin/sh
# Script to kick off Max performance on Nano

sudo jetson_clocks
sudo sh -c 'echo 128 > /sys/devices/pwm-fan/target_pwm'
jtop