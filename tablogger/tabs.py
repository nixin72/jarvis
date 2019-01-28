import json

f= open('~/.mozilla/firefox/RANDOM.default/sessionstore-backups/recovery.js' )

jdata = json.loads(f.read())

f.close()
