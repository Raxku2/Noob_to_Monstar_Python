f=open("a.txt","w"); f.write("Hello"); f.close()
f=open("a.txt"); print(f.read()); f.close()
f=open("a.txt","a"); f.write("World"); f.close()
f=open("a.txt","w"); f.writelines(["one\n","two\n"]); f.close()
f=open("a.txt"); 
for line in f: print(line.strip()); f.close()
f=open("a.txt"); print(len(f.read().split())); f.close()
open("b.txt","w").write(open("a.txt").read())
f=open("num.txt","w"); [f.write(str(i)+"\n") for i in range(1,11)]; f.close()
nums=map(int,open("num.txt").read().split()); print(sum(nums))
# write replaces, append adds
