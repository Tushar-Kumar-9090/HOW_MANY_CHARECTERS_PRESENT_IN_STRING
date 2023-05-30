
## WAP to print how many times each and every charecter is present in a given string??


s="tuushaar"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
for j in d:
    print(j,"=",d[j])
