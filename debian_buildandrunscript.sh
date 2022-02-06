#!/bin/bash

make clean html
cd _build/html/
python3 -m http.server
