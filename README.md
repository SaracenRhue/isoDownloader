# iso downloader

This script downloads the latest ISOs of various systems.

## usage

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/SaracenRhue/isoDownloader/main/get_iso.sh)"
```

or

```bash
wget -c --retry-connrefused --tries=0 --timeout=5 https://raw.githubusercontent.com/SaracenRhue/isoDownloader/main/main.py
python3 main.py
rm -fr main.py
```

## requirements

* curl
* wget
* python3
* python3-requests
* python3-beautifulsoup4
* python3-pick
