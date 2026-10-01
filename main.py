import time
x=[]
length = int(input("how long array"))
for abc in range(length):
  c= int(input("enter integer"))
  x.append(c)
start= time.time()
for e in range(len(x)):

  for i in range(len(x)-1):
    u=x[i]
    f=x[i+1]
    if  x[i]>x[i+1]:
      x[i]=f
      x[i+1]=u
end= time.time()

print(f"{end - start:.10f}, seconds")
print(x)
