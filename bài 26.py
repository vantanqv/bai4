a = 0
while True:
    s = input("Nhập nhật ký giao dịch: ")
    if not s:
        break
    x = s.split(" ")
    daodich = x[0]
    sotien = int(x[1])
    if daodich=="D":
         a+=sotien
    elif daodich=="W":
        a-=sotien
    else:
        pass
print (a)