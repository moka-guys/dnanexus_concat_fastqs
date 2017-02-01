#!/bin/bash
#

# The following line causes bash to exit at any point if there is any error
# and to output each line as it is executed -- useful for debugging
set -e -x -o pipefail

dx-download-all-inputs

python concatenate.py

mkdir -p ~/out/combined_fastq
cat cat.sh
sh cat.sh

dx-upload-all-outputs