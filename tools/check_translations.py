#!/usr/bin/env python3
"""Consistency check of translations against EN (the reference language).

For every language folder and every file that exists in both EN and the
language, checks:
  - Strings/*.txt: no key (@name) missing or extra, no duplicates;
  - placeholders ({0}, {}, {{ ... }}) preserved, per string / per docs file;
  - backticks balanced (even count).
Files absent from a language are not errors (some languages are partial).
Only reports; never edits any text. Exit code 1 if any error is found.
With --baseline, problems already listed there are tolerated (pre-existing debt).
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

REF = "EN"
KEY_RE = re.compile(r"^@([^=\n]*?)[ \t]*=", re.M)  # keys may contain spaces ("@screen mode")
# {{ ... }} (possibly nested) or {digits} / {}
PH_RE = re.compile(r"\{\{.*?\}\}|\{\d*\}", re.S)


def placeholders(text):
    out = Counter()
    for m in PH_RE.finditer(text):
        tok = m.group(0)
        if tok.startswith("{{"):
            # keep only the directive name: its arguments may hold translated text
            inner = tok[2:-2].strip()
            tok = "{{" + (inner.split()[0] if inner else "") + "}}"
        out[tok] += 1
    return out


def parse_strings(text):
    """Return (list of keys, dict key -> body)."""
    ms = list(KEY_RE.finditer(text))
    keys, bodies = [], {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        keys.append(m.group(1))
        bodies.setdefault(m.group(1), text[m.end():end])
    return keys, bodies


def read(p):
    return p.read_text(encoding="utf-8-sig")


def compare(where, ref, tr, errors):
    a, b = placeholders(ref), placeholders(tr)
    if a != b:
        lost, extra = a - b, b - a
        msg = []
        if lost:
            msg.append("missing " + ", ".join(sorted(lost.elements())))
        if extra:
            msg.append("unexpected " + ", ".join(sorted(extra.elements())))
        errors.append(f"{where}: placeholder {'; '.join(msg)}")
    if tr.count("`") % 2:
        errors.append(f"{where}: unbalanced backticks")


def check(root, langs=None):
    root = Path(root)
    errors = []
    ref_dir = root / REF
    langs = langs or sorted(d.name for d in root.iterdir()
                            if d.is_dir() and d.name != REF and (d / "Strings").is_dir())
    for lang in langs:
        for rf in sorted(ref_dir.rglob("*")):
            if not rf.is_file() or rf.suffix not in (".txt", ".md"):
                continue
            rel = rf.relative_to(ref_dir)
            tf = root / lang / rel
            if not tf.is_file():
                continue
            where = f"{lang}/{rel.as_posix()}"
            rt, tt = read(rf), read(tf)
            if rf.suffix == ".txt":
                rk, rb = parse_strings(rt)
                tk, tb = parse_strings(tt)
                for k in sorted(set(rk) - set(tk)):
                    errors.append(f"{where}: missing key @{k}")
                for k in sorted(set(tk) - set(rk)):
                    errors.append(f"{where}: unexpected key @{k}")
                for k, n in Counter(tk).items():
                    if n > 1:
                        errors.append(f"{where}: duplicate key @{k}")
                for k in rb:
                    if k in tb:
                        compare(f"{where} @{k}", rb[k], tb[k], errors)
            else:
                compare(where, rt, tt, errors)
    return errors


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("root", nargs="?", default=Path(__file__).resolve().parent.parent)
    ap.add_argument("--lang", action="append", help="limit to a language folder (repeatable)")
    ap.add_argument("--baseline", type=Path,
                    help="file with known problems (one per line) that are tolerated")
    ap.add_argument("--write-baseline", action="store_true",
                    help="print current problems in baseline format and exit 0")
    args = ap.parse_args(argv)
    errors = check(args.root, args.lang)
    if args.write_baseline:
        print("\n".join(errors))
        return 0
    if args.baseline:
        known = set(args.baseline.read_text(encoding="utf-8").splitlines())
        errors = [e for e in errors if e not in known]
    for e in errors:
        print(e)
    print(f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
