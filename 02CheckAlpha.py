#Day 2 Write a program to identify if the character is an alphabet or not.
ch = input("please enter character:")
if((ch>='a'and ch<='z') or (ch<='A' and ch>='Z')): 
    print("The given character", ch,"is alphabet")
else:
   print("The given character", ch,"is not alphabet")
   
