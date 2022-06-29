#remove last line from a text line in python
fd=open("pv.yaml","r")
d=fd.read()
fd.close()

m=d.split("\n")
s="\n".join(m[:-1])
fd=open("pv.yaml","w+")

for i in range(len(s)):
    fd.write(s[i])
fd.close()