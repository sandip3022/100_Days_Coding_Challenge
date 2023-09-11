'''
Day 1 Write a program to identify if the character is a vowel or consonant.
'''
def vowelorconsonant(x):
  if(x=='a' or x == 'e' or x == 'i' or x == 'o' or x=='u'):
    print("vowel")
  else:
      print("Consonant")
      
x = input().lower()
print(vowelorconsonant(x))
