# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        pos = line.find(':')
        num = float(line[pos+2:])
        average = average + num
    count = count + 1
print("Average spam confidence:", average / count)