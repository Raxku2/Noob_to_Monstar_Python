
f=open("test.txt","w")
f.write("Hello\n")
f.close()

f=open("test.txt","r")
print(f.read())
f.close()

f=open("test.txt","a")
f.write("World\n")
f.close()
