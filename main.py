# -*- coding: utf-8 -*-
import random

str1 = '1234567890'
str2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
str3 = str1 + str2

ls = list(str3)
random.shuffle(ls)

psw = ''.join([random.choice(ls) for x in range(4)])
psw2 = ''.join([random.choice(ls) for x in range(4)])
psw3 = ''.join([random.choice(ls) for x in range(4)])
psw4 = ''.join([random.choice(ls) for x in range(4)])
end = (psw + ' ' + psw2 + ' ' + psw3 + ' ' + psw4)
print(end)