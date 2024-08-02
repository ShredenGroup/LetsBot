s=input()
n=int(s)

def get_result():
    a=0
    while a<n:
        
        yield a
        a+=1
b=get_result()
for item in b:
    print(item)
