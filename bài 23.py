s=input("Nhập câu:")
a={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
     a["DIGITS"]+=1
    elif c.isalpha():
        a["LETTERS"]+=1
else:
    pass
print("số chữ cái là:", a["LETTERS"])
print("số chữa số là:", a["DIGITS"])