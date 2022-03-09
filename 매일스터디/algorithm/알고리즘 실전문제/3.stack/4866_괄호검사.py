def find(a):
    found = []
    for i in range(len(a)):
        if a[i] == "{" or a[i] =="}" or a[i] =="(" or a[i] ==")":
            found.append(a[i])
    return found

T = int(input())
for tc in range(1,T+1):
    string = str(input())
        
    print(find(string))