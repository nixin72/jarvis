"""
List all Firefox tabs with title and URL
Supported input: json or jsonlz4 recovery files
Default output: title (URL)
Output format can be specified as argument
"""

import sys
import pathlib
import lz4.block
import json
import re

path = "/c/Users/phdum/AppData/Roaming/Mozilla/Firefox/Profiles/7747s9bd.default/sessionstore-backups/recovery.jsonlz4"

with open(path, "r") as file:
    data = file.read()
    if data[:8] == b'mozLz40\0':
        data = lz4.block.decompress(data[8:])
    j = json.loads(data)
    for w in j['windows']:
        for t in w['tabs']:
            i = t['index'] - 1
            print(template % (
                t['entries'][i]['title'],
                t['entries'][i]['url']))