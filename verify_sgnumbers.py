def isPhoneNumber(text):
   if len(text) != 9:
         return False

   for i in range(0, 4):
        if not text[i].isdecimal():
            return False

   if text[4] != '-':
    return False

   for i in range(5, 9):
    if not text[i].isdecimal():
        return False
   
   return True


print('Is 7856-1234 a phone number?')
print(isPhoneNumber('7856-1234'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
print('Is 13454065 moshi a phone number?')
print(isPhoneNumber('13454065'))



     
