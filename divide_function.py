def div(a,b):
    try:
    # performing a division        
         sol=a/b
         print("the divison of {0} and {1} = {2}".format(a,b,sol))
    # catching error because you cannot divide by zero     
    except ZeroDivisionError:
        print("You can't divide by 0, mate, sorry.")


    

  
 
