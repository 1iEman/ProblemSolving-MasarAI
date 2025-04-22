
# Problem of dice
listt = [ 1 , 1 , 3 ,4 ,5 ,6]
for element in listt:
    if element > 6 :
        exit("Error" )

dictResult = {1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0}
for element in listt:
    dictResult[element] +=1
        
print(dictResult)
