a=set(["john","mary","tina","fiona","claire","eva","ben","bill","bert"])
a1=set(["john","mary","fiona","claire","ben","bill"])
a2=set(["mary","fiona","claire","eva","ben"])

print("英文與數學及格%s"%(set(a2)&set(a1)))
print("數學不及格%s"%(set(a)-set(a2)))
print("英文及格且數學不及格%s"%(set(a1)&(set(a)-set(a2))))