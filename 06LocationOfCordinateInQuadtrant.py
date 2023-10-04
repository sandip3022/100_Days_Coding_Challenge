"""
Day 6: Determine location of point in quadrant system

like 
x +ve, y +ve => 1st Quadrant
x -ve, y +ve => 2nd Quadrant
x -ve, y -ve => 3rd Quadrant
x +ve, y -ve => 4th Quadrant
"""
X_Co = int(input("Enter X Co-ordinate-:"))
Y_Co = int(input("Enter Y Co-ordinate-:"))
if (X_Co>0 and Y_Co>0):
 print("Entered point lies in First Quadrant")
elif (X_Co<0 and Y_Co>0):
 print("Entered point lies in Second Quadrant")
elif (X_Co<0 and Y_Co<0):
 print("Entered point lies in Third Quadrant")
elif (X_Co>0 and Y_Co<0):
 print("Entered point lies in Fourth Quadrant")
else:
 print("Entered point lies at origin")