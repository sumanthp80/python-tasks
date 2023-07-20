def pattern_7(num): 
      
    # number of spaces is a function of the input num 
    k = 2*num - 2
  
    # outer loop always handle the number of rows 
    for i in range(0, num): 
      
        # inner loop used to handle the number of spaces 
        for j in range(0, k): 
            print(end=" ") 
      
        # the variable holding information about number of spaces
        # is decremented after every iteration 
        k = k - 1
      
        # inner loop reinitialized to handle the number of columns  
        for j in range(0, i+1): 
          
            # printing hash
            print("# ", end="") 
      
        # ending line after each row 
        print("\r") 
 
num = int(input("Enter the number of rows: "))
pattern_7(num)