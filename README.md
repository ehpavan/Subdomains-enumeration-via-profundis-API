# Subdomains-enumeration-via-profundis-API
This tool is designed to enumerate subdomains using the Profundis API. It offers flexible input options and secure API key management.

## Key Features
* Domain Input: * Use `-d` to scan a single domain.
  * Use `-f` or `--file` to scan multiple domains from a list.
* Authentication:
  * The tool requires a **Profundis API Key**.
  * You can provide the key via environment variables or specify it directly using the `-k` or `--key` flag.
# Installation
1. Clone the repository via
```
git clone https://github.com/ehpavan/Subdomains-enumeration-via-profundis-API.git
```
3. install the requirements via
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
4. Providing Multiple domains via -f
```
python3 profundis.py -f domains.txt -k <Profundis-Key>
```
6. Saving output
```
python3 profundis.py -d <domain> -k <profundis-Key> -o <output-file>
```

