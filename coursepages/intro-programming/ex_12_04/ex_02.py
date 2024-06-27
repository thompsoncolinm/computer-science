import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.lonsurfhcp.com/')

counts = dict()
for line in fhand:
    print(line.decode().strip())
