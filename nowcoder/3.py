def pow(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res
n = input()[2:]
d = {'0':0,'1':1,'2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
res = 0
i = 1
l = len(n)
while i <= l:
    res += d[n[l-i]]*pow(16,i-1)
    i+=1
print(int(res))