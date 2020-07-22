#! /bin/bash

for var in 1 2 3 4 5
do
  echo var value :$var
done

#case 1
list="1 2 3 4 5"
for var in $list
do
    echo var value :$var
done

for var2 in "1 2 3 4 5"
do
    echo var2 value :$var2
done




