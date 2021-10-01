#!/usr/bin/env bash
declare -a dict=('Horse' 'Shoe' 'Cat' 'Puppy' 'Camera' 'Radio' 'Song')
for file in "$@"
do
    if [ ! -f $file ]; then
        echo "${file} does not exist!"
    else
        mv $var ${dict[$RANDOM % ${#dict[@]}]}
    fi
done
