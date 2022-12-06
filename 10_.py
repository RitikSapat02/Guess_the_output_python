def highest_even(li):
    even = []
    for x in li:
        if(x%2==0):
            even.append(x)
        return max(even)
print(highest_even([2,3,4,5,6,7,8,91,10]))