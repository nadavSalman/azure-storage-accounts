#!/bin/bash

# -------------------------------------------------------------------------------------------
# |   This script will create, upload, and copy 100 blobs from Storage account A to B.      |
# |   intended to run on the deployment Server.                                             |
# -------------------------------------------------------------------------------------------

if [ -z "$(ls -A ./files)" ]; then
    echo "Folder is empty, creating 100 files (blobs)."
    for i in {1..100}; do touch "./files/file${i}.tgz"; done
else
    echo "Folder is not empty."
fi

python3 main.py

