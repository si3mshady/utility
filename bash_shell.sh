#!/bin/bash

echo -n "Enter a process name to evaluate "

read response

echo "You entered" $response

process=$(pidof $response)

        for i in $process;

do

var=$(ps aux $i | awk '{print $3}' | egrep "\d" )

echo "The CPU % usage for $i is $var"

if (( $(bc <<< "$var <  80") ))
        then
 echo "Would you like to kill $i (y/n)"
 read resp

fi

if [ "$resp" == "y" ] || [ "$resp" == "Y" ];

then

kill -15 $i

echo "$i has been terminated with sigkill 15"

fi


done;
