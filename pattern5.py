def pattern_5(num): 
    # initializing value of A as 65
    # ASCII value  equivalent
    number = 65
  
    # outer loop always handles the number of rows 
    for i in range(0, num): 
      
        # inner loop handles the number of columns 
        for j in range(0, i+1): 
          
            # finding the ascii equivalent of the number 
            char = chr(number) 
          
            # printing char value  
            print(char, end=" ") 
      
        # incrementing number 
        number = number + 1
      
        # ending line after each row 
        print("\r") 
  
num = int(input("Enter the number of rows in pattern: "))
pattern_5(num)