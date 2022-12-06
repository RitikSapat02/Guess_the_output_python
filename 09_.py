'''
def sum(num1,num2):
    def another_fun(num1,num2):
        return num1+num2
print(sum(10,20))             #none

'''


'''
def sum(num1,num2):
    def another_fun(num1,num2):
        return num1+num2
    return another_fun            #refrence_address to function will return
print(sum(10,20))
'''


'''
def sum(num1,num2):
    def another_fun(num1,num2):
        return num1+num2
    return another_fun(10,20)
print(sum(10,20))
'''


def sum(num1,num2):
    def another_fun(num1,num2):
        return num1+num2
    return another_fun             #address of another_fun

total = sum(10,20)                 #assigning refrence to function so now total refers to the same function as of another_fun

print(total(10,20))