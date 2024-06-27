# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)
print(sorted(lst))