# bubble sort
q =[102,99,12,15,6,7]
print(q[1])
print(len(q))
try:
    while q!= sorted(q):
        for i in range(len(q)-1):
            if q[i+1] < q[i]:
                x = q[i]
                y = q[i+1]
                q[i] = y
                q[i+1] = x
                print(q)
           
except:
    print("error") 
