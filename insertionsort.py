arr=[12,-1,34,2,5,6,2, 67, 23189823198321983219, 291389218398]
n = len(arr)
for i in range(1, n):
    key = arr[i]
    print("Key", key)
    j = i-1
    while j >=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -=1
        print(arr)
    arr[j+1] = key
    print(arr)
    print("-"*20)