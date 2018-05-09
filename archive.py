# this program opens the old websites dated back with time
import webbrowser
import json
from urllib.request import urlopen

print(" lets find a old website: ")
site = input("type a website url: ")
era = input ("Type a year, month, and day, like 20150613:")

url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)

try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("it should appear in your browswer now")
    webbrowser.open(old_site)
except:
    print("sorry no luck finding site", site)
