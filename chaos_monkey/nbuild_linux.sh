#!/bin/bash

p=$(pwd)
mkdir bin
cd monkey_utils/sambacry_monkey_runner
bash build.sh
cp *.so $p/bin
cd $p
pyinstaller --clean monkey.spec
