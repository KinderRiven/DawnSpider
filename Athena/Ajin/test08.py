

list = ["123", "!23"]

print list[0]
print list[1]

pos = 0
len = 100

while True:
    print "=============="
    for i in range(0, 50, 1):
        if pos >= len:
            break
        print pos
        pos = pos + 1

    if pos >= len:
        break
