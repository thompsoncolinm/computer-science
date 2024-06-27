# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname)
hour = dict()
for line in handle:
    if not line.startswith("From "): continue
    words = line.split()
    time = words[5]
    hour[time[:2]] = hour.get(time[:2], 0) + 1
for k, v in sorted(hour.items()):
    print(k, v)
