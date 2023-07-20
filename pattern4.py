def pattern_4(num): 
      
    # initialising starting number  
    number = 1
    # outer loop always handles the number of rows 
    # let us use the inner loop to control the number 
   
    for i in range(0, num): 
      
        # commenting the reinitialization part ensure that numbers are printed continuously
        # ensure the column starts from 0
        number = 0
      
        # inner loop to handle number of columns 
        for j in range(0, i+1): 
          
                # printing number 
            print(number, end=" ") 
          
            # increment number column wise 
            number = number + 1
        # ending line after each row 
        print("\r") 
  

num = int(input("Enter the number of rows in pattern: "))
pattern_4(num)