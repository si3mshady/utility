#!/bin/bash

function check {
count=$(awk '/[Ee]rror/ { count++ } END { print count }' /var/log/system.log)
ut=$(uptime | awk '{print $10,$11,$12}')
time=$(date +%a\ %B\ %d\ %H:%M)
echo  "\"Error\" has been detected $count times as of"  $time
echo  "Uptime as of $time -> $ut" 
}
check > latest_system_check


