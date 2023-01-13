#!/bin/bash 

wget -c --retry-connrefused --tries=0 --timeout=5 https://raw.githubusercontent.com/SaracenRhue/isoDownloader/main/main.py
python3 main.py