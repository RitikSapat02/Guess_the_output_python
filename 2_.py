'''def sum(num1,num2):
    def another_fun(num1,num2):
        return num1+num2

print(sum(10,20))        #none
'''

'''
def sum(num1,num2):
    def another_fun(num1,num2):
        return num1+num2
    return another_fun

print(sum(10,20))      # address_fun = refrence of the function stored
'''

'''
def sum(num1,num2):
    def another_fun(num1,num2):
        return num1+num2
    return another_fun(num1,num2)

print(sum(10,20))     #30
'''

def sum(num1,num2):
    def another_fun(num1,num2):
        return num1+num2
    return another_fun

total = sum(10,20)           #total = another_fun = now both referring to function
print(total(10,20))       #30


