arr1 = [1,2,3,4,5]
arr2 = arr1

arr1.append(6)

print(arr1)
print(arr2)

#to print the initial values of arr1 in arr2 we use copy() method

arr2 = arr1.copy()
arr1.append(7)
print(arr1)
print(arr2)