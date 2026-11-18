"""Author-year keys for the included studies (from review/data/study_citations.csv)."""
import csv, os
_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CIT = {r["idx"]: r for r in csv.DictReader(open(os.path.join(_ROOT, "review/data/study_citations.csv"), encoding="utf-8"))}

def key(i):
    return CIT[str(i)]["key"]

def short(i):
    """Key without parentheses, e.g. 'Chatterjee 2020'."""
    return key(i).replace(" (", " ").replace(")", "")
