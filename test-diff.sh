#!/bin/bash
branches=(jesse)
for branch in ${branches[@]}
do 
  for py_file in $(git diff --name-only $branch dev | grep .py)
  do
    python $py_file
  done
done
