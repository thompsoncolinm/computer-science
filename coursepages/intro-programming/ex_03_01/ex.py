xh = input('Enter hours: ')
xr = input('Enter rate: ')
fh = float(xh)
fr = float(xr)
if fh > 40:
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print('Pay:', xp)