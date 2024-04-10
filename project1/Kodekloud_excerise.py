#Pgm1:
#for letter in 'KodeKloud':
   # if letter == 'e':
    #    continue
    #print('Letter : ' + letter)
    
   
#Pgm2:
#sum = 0
#values = [2,9,1,7]
#for number in values:
 #   sum += number
#print(sum)
    
#pgm3:
#for x in [0, 1, 1, 3]:
 #   for y in [0, 2, 1, 2]:
  #          print('*')
            
#pgm 4:
#year = 1905
#year = year // 100
#if(year == 0) :
#print(year)
#else:
       # year += 1
        
#print(year)
 
 # pgm 5:palindorme
def ispalindrome(s) :
     return s == s[::-1]
s = "mom"
ans = ispalindrome(s)

if ans: 
    print ("yes")
else:
    print("No")


a = input("Enter a word: ")
b = ""
for i in a:
    b = i + b
if (a == b): 
    print ("yes")
else:
    print("No")
    

 
    
    