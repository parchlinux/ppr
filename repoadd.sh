#!/bin/bash

#set -x

if [ "$1" == "" ];then
  echo "repoadd.sh <repo_name>"
  exit 1
fi

cd x86_64
repo-add $1.db.tar.gz *pkg.tar.zst

mv $1.files.tar.gz $1.files
mv $1.db.tar.gz $1.db
