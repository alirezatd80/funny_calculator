from functions import help_fun , input_user
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
                    pass
                case "-":
                    pass
                case "*":
                    pass
                case "/":
                    pass
                case "^":
                    pass
                case "%":
                    pass
                case "!":
                    pass
                case "#":
                    pass
                case _ :
                    pass
        
    

if __name__ == "__main__":
    main()