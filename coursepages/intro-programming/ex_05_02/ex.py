largest = None
smallest = None

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        ival = int(sval)
    except:
        print("Invalid input")
        continue
    if largest is None or ival > largest:
        largest = ival
    if smallest is None or ival < smallest:
        smallest = ival

print("Maximum is", largest)
print("Minimum is", smallest)