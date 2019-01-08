#!/bin/bash

modified=$(find ~/Documents  -type f -mtime -7)
backupDir=~/backup


for item in $modified

do

    cp $item  $backupDir

	fi

done



for file in $(ls $backupDir)

 do

 tar czf "backup.tgz" $backupDir\/$file

    done

for delete in $(ls $backupDir \| grep -v tgz)
 
 do
 	
        rm $backupDir\/$delete

 done