"""Download the WDI indicators listed in spec.md into one tidy CSV (analysis/data/wdi_panel.csv).

Uses the public World Bank API, no key needed. Raw JSON is cached in the directory given as argv[1].
"""
import concurrent.futures as cf
import json
import os
import sys
import time

import pandas as pd
import requests

CACHE = sys.argv[1]
os.makedirs(CACHE, exist_ok=True)
OUT = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUT, exist_ok=True)
IND = {"mobile": "IT.CEL.SETS.P2", "internet": "IT.NET.USER.ZS", "broadband": "IT.NET.BBND.P2", "gdppc": "NY.GDP.PCAP.KD",
       "lifeexp": "SP.DYN.LE00.IN", "u5mort": "SH.DYN.MORT", "unemp": "SL.UEM.TOTL.ZS", "agshare": "NV.AGR.TOTL.ZS",
       "co2pc": "EN.ATM.CO2E.PC", "elecuse": "EG.USE.ELEC.KH.PC", "secenr": "SE.SEC.ENRR", "trade": "NE.TRD.GNFS.ZS",
       "credit": "FS.AST.PRVT.GD.ZS", "elecaccess": "EG.ELC.ACCS.ZS", "pop": "SP.POP.TOTL"}

def get(url, params=None, tries=6):
    for i in range(tries):
        try:
            r = requests.get(url, params=params, timeout=280)
            if r.status_code == 200:
                return r.json()
        except requests.RequestException:
            pass
        time.sleep(5 * (i + 1))
    return None

def fetch(item):
    name, code = item
    path = os.path.join(CACHE, f"{code}.json")
    if os.path.exists(path):
        return name, json.load(open(path))
    d = get(f"https://api.worldbank.org/v2/country/all/indicator/{code}", {"format": "json", "per_page": 20000, "date": "1995:2023"})
    if d and len(d) > 1:
        json.dump(d, open(path, "w"))
        return name, d
    return name, None

with cf.ThreadPoolExecutor(2) as ex:
    res = dict(ex.map(fetch, IND.items()))
meta = get("https://api.worldbank.org/v2/country", {"format": "json", "per_page": 400})
ctry = pd.DataFrame([{"iso3": c["id"], "country": c["name"], "region": c["region"]["value"].strip(), "income": c["incomeLevel"]["value"]} for c in meta[1]])
ctry = ctry[ctry["region"] != "Aggregates"]
frames = []
for name, d in res.items():
    if d is None:
        print("MISSING", name)
        continue
    df = pd.DataFrame([{"iso3": x["countryiso3code"], "year": int(x["date"]), name: x["value"]} for x in d[1] if x["value"] is not None and x["countryiso3code"]])
    frames.append(df.set_index(["iso3", "year"]))
panel = pd.concat(frames, axis=1).reset_index()
panel = panel.merge(ctry, on="iso3", how="inner")
panel.to_csv(os.path.join(OUT, "wdi_panel.csv"), index=False)
print(panel.shape, panel["iso3"].nunique(), panel.groupby("income")["iso3"].nunique().to_dict())
