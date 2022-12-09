#unlike cpp and java python does not have block scope

from re import I


game_level = 3
enemies = ["skeleton","zombie"]
if(game_level == 3):
    new_enemy = enemies[0]

print(new_enemy)

if(True):
    a=100
    b=400
    c=200
    d=100

print(a,b,c,d)

i = 0
suma = 0
while(i<10):
   suma +=i
   i+=1

print(suma)