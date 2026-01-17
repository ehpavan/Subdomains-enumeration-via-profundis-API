#!/usr/bin/env python3
import argparse
import requests
import json
import os
import re
import sys
import time
import random

DOMAIN_RE = re.compile(r'^[\.a-z\-\d]+\.[a-z]+$')

def get_api_key(cli_key):
    if cli_key:
        return cli_key.strip()
    key = os.getenv("PROFUNDIS_API_KEY", "").strip()
    if key:
        return key
    print("[!] PROFUNDIS API key not provided. Use -k KEY or set PROFUNDIS_API_KEY.")
    sys.exit(1)

def validate_domain(domain: str) -> str:
    domain = domain.lower().strip()
    if not DOMAIN_RE.fullmatch(domain):
        print(f"[!] Domain validation failed: {domain}")
        return None
    return domain

def fetch_subdomains(key, domain):
    url = "https://api.profundis.io/api/v2/common/data/subdomains"
    headers = {
        "X-API-KEY": key,
        "Accept": "text/event-stream",
        "Content-Type": "application/json"
    }
    data = {"domain": domain}

    print(f"[*] Fetching subdomains for {domain}...")

    try:
        with requests.post(url, headers=headers, data=json.dumps(data), stream=True, timeout=30) as r:
            if r.status_code != 200:
                print(f"[!] Error {r.status_code}: {r.text}")
                return

            for line in r.iter_lines():
                if line:
                    # Print raw line decoded; user will process later as needed
                    print(line.decode(errors="ignore"))
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Request failed for {domain}: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", action="append", help="Domain to scan (can be used multiple times)")
    parser.add_argument("-f", "--file", help="Path to a file with one domain per line")
    parser.add_argument("-k", "--key", help="Profundis API key (overrides PROFUNDIS_API_KEY env var)")
    args = parser.parse_args()

    domains = []

    if args.domain:
        domains.extend(args.domain)

    if args.file:
        if not os.path.exists(args.file):
            print(f"[!] File not found: {args.file}")
            sys.exit(1)
        with open(args.file, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    domains.append(line)

    if not domains:
        print("[!] No domains provided. Use -d or -f.")
        sys.exit(1)

    key = get_api_key(args.key)

    for i, domain in enumerate(domains, start=1):
        valid_domain = validate_domain(domain)
        if valid_domain:
            fetch_subdomains(key, valid_domain)
            if i < len(domains):
                wait_time = random.uniform(2, 3)
                time.sleep(wait_time)
        else:
            print(f"[!] Skipping invalid domain: {domain}")

if __name__ == "__main__":
    main()
