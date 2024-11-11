#!/bin/bash

fizzbuzz()
{
    multiplo_3=$1
    multiplo_5=$2
    i=1

    while [ $i -le 100 ]
    do
        if (( i % multiplo_3 == 0 )) && (( i % multiplo_5 == 0 ))
        then
            echo "fizzbuzz"
        elif (( i % multiplo_3 == 0 ))
        then
            echo "fizz"
        elif (( i % multiplo_5 == 0 ))
        then
            echo "buzz"
        else
            echo $i
        fi
        ((i++))
    done    
}

main()
{
    fizzbuzz 3 5 
}

main
