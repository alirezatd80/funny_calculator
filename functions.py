import re
def sum(num1 , num2):
    return num1 +num2

def minus(num1 , num2):
    return num1 - num2 

def multi(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
    if num2 == 0 :
        raise ZeroDivisionError("can't divide with zero !!! ")
    return num1/num2

def mod(num1 , num2):
    if num2 == 0 :
        raise ZeroDivisionError("can't mod with zero !!! ")
    return num1%num2

def power(num1 , num2):
    if num1 == num2 == 0:
        raise Exception("can't num1 and num2 be zero together")
    return num1^num2

def fact(num):
    if num == 0 or num == 1 :
        return 1
    return num * fact(num-1)

def sqr(num):
    if num >= 0 :
        return num ^(0.5)
    else:
        return Exception("can't sqr for nagetive number !!! ")
    
def input_user(message):
    
    user_input = input(message)
    if not check_expression(user_input):
        raise ValueError('please enter correct input !!!')
    else:
        return spliter(user_input)
        
def spliter(user_input):
    nums = re.split(r'[\+\-\*\/\^\%\!\#]',user_input)
    operation_selection = user_input.replace(nums[0],'').replace(nums[1],'')
    return nums  , operation_selection 

def check_expression(expression):
    expression= expression.replace(' ' , '')
    townum_operation_list = ['+','-','*','/','^','%']
    onenum_operation_list = ['!','#']
    all_operation_list = townum_operation_list+onenum_operation_list
    check_expression_user = True
    count_operation = 0 
    for i in expression:
        if i in all_operation_list:
            count_operation +=1
    if count_operation != 1 :
        check_expression_user= False
    if expression == "" :
        check_expression_user = False
    nums , operation  = spliter(expression)
    if operation in townum_operation_list and (nums[0]== '' or nums[1] == ''):
        check_expression_user=False
    if operation in onenum_operation_list and (is_num(nums[0]) and is_num(nums[1])):
        check_expression_user = False
    
    
    return check_expression_user
    
def is_num(string):
    try :
        float(string)
        return True
    except ValueError:
        return False

def help_fun():
    print("a+b(sum) , a-b(minus) , a*b(multi) , a/b(divide) , \na%b(mod) ,a^b(power) , a!(fact) , a#(sqr)\nctrl+c or ctrl+z for exit")
        
