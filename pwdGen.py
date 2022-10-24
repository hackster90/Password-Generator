#Password Generator

import random

# Here n Is The Length Of The Password
def Generate(n):
    pwdStr = ''
    for i in range(0,n):
        uni = random.randint(33,127)
        pwdStr+=chr(uni)
    return  pwdStr


#Test cases

#Test1
#Generate(10)
# kP*avO)mN4

#Test2
#Generate(20)
# *\GG7F{nr%.MIV5A2Hi7

#Test3
#Generate(30)
# $2bo1~E]Wj\y,vN;cD8|9+M`#rD<\i

#Test4
#Generate(40)
# DDl7j:dCZ)rUvX$o{PtP?D@*70*B^XJ7m}wGof[

#Test5
#Generate(50)
# Imf@.&T!QCxU6/ua/08y0\DsJm(lwE]e]Fm&GFLje"vy%YeU,]

