#gives runner up score


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    arr=set(arr)
    arr=list(arr)
    arr=sorted(arr)
    arr=arr[::-1]
    if(len(arr)==1):
        print(0)
    else:
        print(arr[1])
