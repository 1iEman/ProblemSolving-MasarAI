"""
ALGORITHM:
1. Promote user to enter the black and white balls

2. Special Case:
      - if white ball is 0 then print 0
      
3. Generate list contain numbers from 1 to 100

4. Use For loop through numbers list:
   - Check if number is odd then Subtract odd number from white balls and check result if greater than 0 --> It means there is enough white balls to build new level, 
     update white balls with the Subtraction result and add that level has been build for triangle (counter+1)
     
   - Then take next number (which will be ocourse even number) and Subtract even number from black balls then check result if greater than 0 --> --> It means there is enough black balls to build new level
     update black balls with the Subtraction result and add new level has been build for triangle (counter+1)
     
5. Print the number of levels' triangle (counter)
"""

"""
Pesudo-code: 

START

1. Ask the user to enter number of white balls and black balls

2. If white balls are 0
      Print 0
      Stop

3. Set counter = 0
4. Make a list of numbers from 1 to 100

5. Go through each number in the list:
      - If the number is odd:
            - If we have enough white balls:
                  Subtract that number from white balls
                  Increase counter by 1

                  - If next number exists (even number) and we have enough black balls:
                        Subtract next number from black balls
                        Increase counter by 1
                  - Else:
                        Stop the loop
            - Else:
                  Stop the loop

6. Print the total counter (levels built)

END

"""
# Eample Input 1 2 -->> white = 1 , black = 2
white , black = map(int , input("Enter the white balles then the black ones: ").split())
 
# Special cases
if (white == 0 ):
    print("0")
    exit()

counter = 0
numbers = list(range(1,101))
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        if white - numbers[i] >= 0:
            white = white - numbers[i]
            counter+=1
            if i != (len(numbers)-1):
                if (black - numbers[i+1] >= 0):
                   black = black - numbers[i+1]
                   counter+=1
                else:
                    break
        else:
            break
        
print(counter)
