#!/usr/bin/python3

import re, sys

sys.stderr.write("Reading CLDR from stdin (e.g. github.com/unicode-org/cldr/common/uca/allkeys_CLDR.txt\n")
uniq = {}
print("return {")
for line in sys.stdin.readlines():
  m = re.match("^([0-9A-F]+).*# (.*)$",line)

  if m:
    if m.group(2) in uniq:
      sys.stderr.write(f'WARNING: name {m.group(2)} used at {uniq[m.group(2)]} and also in {line}\n')
    else:
      uniq[m.group(2)]=m.group(1)
      print(f'    ["{m.group(2)}"]=0x{m.group(1)},')
print("}")

