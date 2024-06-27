# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
def greatest_email(fh):
    max_email = None
    counts = dict()
    max_count = 0
    for line in fh:
        if not line.startswith("From "): continue
        words = line.split()
        email = words[1]
        if email in counts:
            counts[email] += 1
        else:
            counts[email] = 1
        if counts[email] > max_count:
            max_email = email
            max_count = counts[email]
    return str(max_email)+' '+str(max_count)
print(greatest_email(fh))
