import random as r
import string as s
while True:
    elem = s.ascii_letters + s.digits
    sz = int(input("Size of password"))
    passs = ""
    if sz == 0:
        break
    else:
        for i in range(sz):
            passs += r.choice(elem)
        print(passs)

print(elem)