import random
import time
#random movtiavtion words generator !
num = random.randint(1,10)
print(f'computer chose message number {num} !')

message = ''
if num == 1 :
  message = 'Youre beautiful just the way you are!'
elif num == 2:
  message = 'you matter to me!'
elif num == 3:
  message = 'im really glad youre here!'
elif num == 4:
  message = 'its okay if things dont go as planned, theres better to come!'
elif num ==5:
  message = 'you deserve so much happiness <3'
elif num == 6:
  message = 'today is a very good day, i can feel it!'
elif num == 7:
  message= 'i hope life is kind to you when you need it most!'
elif num == 8:
  message= 'you existing makes ordinary days feel special <3'
elif num == 9:
  message = 'i hope you get treated the way your favourite song makes you feel <3'
elif num == 10:
  message = 'i hope you realise just how much i , and many others love you.'
time.sleep(1)
print(f"message of the day: '{message}' .")
