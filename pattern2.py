def pattern_2(num): 
      
    # define the number of spaces 
    k = 2*num - 2
  
    # outer loop always handles the number of rows 
    # let us use the inner loop to control the number of spaces
    # we need the number of spaces as maximum initially and then decrement it after every iteration
    for i in range(0, num): 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 2
      
        # reinitializing the inner loop to keep a track of the number of columns
        # similar to pattern_1 function
        for j in range(0, i+1):  
            print("# ", end="") 
      
        # ending line after each row 
        print("\r") 
  

num = int(input("Enter the number of rows in pattern: "))
pattern_2(num)