a=input("nhập dãy số các nhau bằng dấu phẩy:")
s=[x for x in a.split(",")if int(x)%2!=0]
print(",".join(s))