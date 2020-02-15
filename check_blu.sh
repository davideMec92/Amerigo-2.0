#!/bin/bash

sudo hcitool cc B4:86:55:59:A2:E9 2> /dev/null

while true
do
    bt=$(hcitool rssi B4:86:55:59:A2:E9 2> /dev/null)
    if [ "$bt" == "" ]; then
        sudo hcitool cc B4:86:55:59:A2:E9  2> /dev/null
        bt=$(hcitool rssi B4:86:55:59:A2:E9 2> /dev/null)
    fi

    echo "$bt"
done
