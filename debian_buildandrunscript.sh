#!/bin/bash

make clean html
#make latexpdf
cd _build/html/
python3 -m http.server
