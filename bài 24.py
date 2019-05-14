n=input("nhập câu:")
dict={'chử hoa':0, 'chử thường':0}
for i in n:
    if i.isupper():
        dict['chử hoa']+=1
    elif i!=' ':
        dict['chử thường']+=1
print(dict)