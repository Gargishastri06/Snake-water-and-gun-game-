# snake,water,gun game
'''
s= snake=1
g=gun =0
w=water=-1
'''


print('           WELCOME TO THE GAME               ')
print('*********************************************************')
print('RULE: If you want to choose snake enter = s \n      If you want to choose gun enter = g \n      If you want to choose water enter = w ')
print('*********************************************************')
import random
computer = random.randint(-1,1)
player=input('enter your choice : ')
dic2={1:'snack',-1:'water',0:'gun'}
compchoose=dic2[computer]
print(f"computer choose :{compchoose}")
dic1={'s':'snack','g':'gun','w':'water'}
choose=dic1[player]
print(f"you choose : {choose}  ")
print('')
dic={'s':1,'w':-1,'g':0}
you=dic[player]
if computer==you:
    print('---This is draw---')
else:
    if computer==-1 and you==1:
        print('---You win---')
    elif computer==-1 and you==0:
        print('---You fail---')
    elif computer==1 and you==-1:
        print('---You win----')
    elif computer==1 and you==0:
        print('---You fail---')
    elif computer==0 and you==1:
        print('---You win---')
    elif computer==0 and you==-1:
        print('---You fail---')
    else:
        print('Something went wrong')

print('                                                         ')
print('*********************************************************')

print('           GAME END            ')

print('*********************************************************')