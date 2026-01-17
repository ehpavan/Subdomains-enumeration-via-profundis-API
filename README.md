# Subdomains-enumeration-via-profundis-API
The tool was designed to enumarate subdomains via profundis API, the tool utilizes an API Key of profundis the tool reads the API key via Env variables or you can specify with -k or --key.

# Installation
1. git clone `https://github.com/ehpavan/Subdomains-enumeration-via-profundis-API.git`
2. install the requirements via
```
pip3 install -r requirements.txt
```
> note: it causes some conflicts so use with --break-system-packages
3. run the tool via
```
python3 profundis.py
```

# Usage
1. basic usage
```
python3 profundis.py -d <Domain> -k <Profundis-Key>
```
3. reads the API-KEY via env variables (no need of -k flag)
```
python3 profundis.py -d <Domain>
```
5. Saving output
```
python3 profundis.py -d <domain> -k <profundis-Key> -o <output-file>
```

