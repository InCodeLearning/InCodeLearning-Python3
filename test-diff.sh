#!/bin/bash
branches=(jesse Yong mingzhangyang)
for branch in ${branches[@]}
do
  git checkout $branch
  echo ">>>> testing branch $branch"
  for py_file in $(git diff --name-only $branch dev | grep '\.py$')
  do
    echo ">>>>>>>> testing $py_file"
    python $py_file | grep Traceback
    pep8 --first $py_file
  done
done

# compare each of the contributor's branch with dev 
# execute all the newly committed python codes
