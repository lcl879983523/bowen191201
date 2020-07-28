a=[1,5,6,8,79,]
for i in range(len(a)):
      for k in range(len(a)-1-i):
          if a[k] < a[k+1]:
            a[k],a[k+1]=a[k+1],a[k]
print(a)