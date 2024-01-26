def merge(arr,l,m,r):
    for i in range (m+1,r):
        j = i-1
        key = arr[i]
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = key
            j-=1

def merge_sort(arr,l,r):
    if l < r:
        m = l + (r - l)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)

arr = [5,4,6,9,2,7,1]
r = len(arr)
print(r)
merge_sort(arr,0,r)
print(arr)