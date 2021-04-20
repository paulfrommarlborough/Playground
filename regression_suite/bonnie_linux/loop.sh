#!/bin/sh
i="RUN"
while [ i != "EXIT" ]
do
 ./Bonnie64 -s 50
 rm -rf ./Bonnie.*
done
done

