#!/bin/bash

set -e

build_copy_rm() {
  name=$1
  dockerfile=$2
  src=$3
  dst=$4

  echo $name, $dockerfile, $src, $dst, $OPTS

  docker build -t $name -f $dockerfile $OPTS ../
  id=$(docker create $name)
  docker cp $id:$src $dst
  docker rm -v $id
}

OPTS=$@

build_copy_rm monkey_chaos Dockerfile.chaos /monkey/chaos_monkey/dist ../
build_copy_rm monkey_chaos32 Dockerfile.chaos32 /monkey/chaos_monkey/dist ../
docker build -t monkey_island -f Dockerfile.island ../
