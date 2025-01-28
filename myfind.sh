#!/bin/bash
find ./files1 ./files2 -maxdepth 1 -type f \( -name "lorem2.dat" -o -name "lorem3.dat" \)
