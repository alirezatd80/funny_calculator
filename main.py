from functions import help_fun ,is_num, input_user , sum , minus , multi , divide , mod , power, fact , sqr
def main():
    print('Welcome to calculator :)')
    print('Create by Alireza Tashani')
    help_fun()
    
    while(True):
            try :
                nums , operation = input_user('input : ')
                match(operation):
                    case '+':
                        print(f'output => {float(nums[0])} + {float(nums[1])} = {sum(float(nums[0]) , float(nums[1]))}')
                    case "-":
                        print(f'output => {float(nums[0])} - {float(nums[1])} = {minus(float(nums[0]),float(nums[1]))}')
                    case "*":
                        print(f'output => {float(nums[0])} * {float(nums[1])} = {multi(float(nums[0]),float(nums[1]))}')
                    case "/":
                        try:
                            print(f'output => {float(nums[0])} / {float(nums[1])}={divide(float(nums[0]),float(nums[1]))}')
                        except :
                            print("error num2 cant be zero")
                    case "^":
                        try:
                            print(f'output => {float(nums[0])} * {float(nums[1])} = {power(float(nums[0]),float(nums[1]))}')
                        except:
                            print('nums cant be zero')
                    case "%":
                        try:
                            print(f'output => {float(nums[0])} % {float(nums[1])} = {mod(float(nums[0]),float(nums[1]))}')
                        except :
                            print("error num2 cant be zero")
                    case "!":
                        try:
                            if is_num((nums[0])):
                                print(f'output => {float(nums[0])}! = {fact(float(nums[0]))}')
                            else:
                                print(f'output => {float(nums[1])}! = {fact(float(nums[1]))}')
                        except:
                            print('cant be correct')

                    case "#":
                        
                        try:
                            if is_num(nums[0]):
                                print(f'output => {float(nums[0])}# = {sqr(float(nums[0]))}')
                            else:
                                print(f'output => {float(nums[1])}# = {sqr(float(nums[1]))}')
                        except e:
                            print(f"can't be nagative num {e}")
                    case _ :
                        print(f'output => sorry')
            except :
                print('pls enter correct value !!!')
            
        
    

if __name__ == "__main__":
    main()