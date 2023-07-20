def pattern_1(num): 
      
    # outer loop handles the number of rows
    # inner loop handles the number of columns 
    # n is the number of rows. 
    for i in range(0, num): 
      # value of j depends on i 
        for j in range(0, i+1): 
          
            # printing hashes
            print("#",end=" ") 
       
        # ending line after each row 
        print("\r")  
num = int(input("Enter the number of rows in pattern: "))
pattern_1(num)