#!/bin/bash

fizzbuzz()
{
    i=1

    while [ $i -le 100 ]
    do
        if [ $((i % 3)) -eq 0 ] && [ $((i % 5)) -eq 0 ]
        then
            echo "fizzbuzz"
        elif [ $((i % 3)) -eq 0 ]
        then
            echo "fizz"
        elif [ $((i % 5)) -eq 0 ]
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
    fizzbuzz
}

main