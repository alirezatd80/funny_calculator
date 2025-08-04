from functions import help_fun ,is_num, input_user , sum , minus , multi , divide , mod , power, fact , sqr
def main():
    print('Welcome to calculator :)')
    print('Create by Alireza Tashani')
    help_fun()
    
    while(True):
            try :
                nums , operation = input_user('input : ')
            except :
                print('pls enter correct value !!!')
            match(operation):
                case '+':
                    print(f'output => {int(nums[0])} + {int(nums[1])} = {sum(int(nums[0]) , int(nums[1]))}')
                case "-":
                    print(f'output => {int(nums[0])} - {int(nums[1])} = {minus(int(nums[0]),int(nums[1]))}')
                case "*":
                    print(f'output => {int(nums[0])} * {int(nums[1])} = {multi(int(nums[0]),int(nums[1]))}')
                case "/":
                    try:
                        print(f'output => {int(nums[0])} / {int(nums[1])}={divide(int(nums[0]),int(nums[1]))}')
                    except :
                        print("error num2 cant be zero")
                case "^":
                    try:
                        print(f'output => {int(nums[0])} * {int(nums[1])} = {power(int(nums[0]),int(nums[1]))}')
                    except:
                        print('nums cant be zero')
                case "%":
                    try:
                        print(f'output => {int(nums[0])} % {int(nums[1])} = {mod(int(nums[0]),int(nums[1]))}')
                    except :
                        print("error num2 cant be zero")
                case "!":
                    try:
                        if is_num(int(nums[0])):
                            print(f'output => {int(nums[0])}! = {fact(int(nums[0]))}')
                        else:
                            print(f'output => {int(nums[1])}! = {fact(int(nums[1]))}')
                    except:
                        print('cant be correct')
                    
                case "#":
                    try:
                        if is_num(int(nums[0])):
                            print(f'output => {int(nums[0])}# = {sqr(int(nums[0]))}')
                        else:
                            print(f'output => {int(nums[1])}# = {sqr(int(nums[1]))}')
                    except:
                        print("can't be nagative num")
                case _ :
                    print(f'output => sorry')
        
    

if __name__ == "__main__":
    main()