#a = [[1.0,1.0,2.0,-4],[2.0,-1.0,3.0,1],[3.0,1.0,-1.0,2],[1,-1,-1,1]]
#b = [0.0,5.0,5.0,0]

a = [[2.0,-3.0,1.0],[1.0,-1.0,-2.0],[3.0,1.0,-1.0]]
b = [7.0,-2.0,0.0]

a_len = len(a)
print ("lenght", a_len)

for k in range(a_len-1):
    print ("k=",k)
    for i in range(k+1,a_len):
        print ("i",i)
        x = a[i][k]/a[k][k]
        print ("x",x)
        for j in range(a_len):
            a[i][j]=a[i][j]-a[k][j]*x
        b[i] = b[i] - b[k]*x
        
            
print (a)
print (b)

# Back Substitution

for i in range(a_len-1,-1,-1):
    # range(2,-1,-1) will give 2,1,0
    print ("i",i)
    x = b[i]
    if i < a_len-1:
        for j in range(i+1,a_len):
            print ("j",j)
            x = x - a[i][j]*b[j]
    b[i] = x / a[i][i]
    

print ("Solution=",b)
