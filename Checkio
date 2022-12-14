#hose password
def checkio(password:str)->bool:
    password=a
    if len(a)>=10 and a.isascii():
    status1,status2,status3=False,False,False
        for i in a:
            if i.isdigit():
                status1=True
                break;
        for i in a:
            if i.isupper():
                status2=True
                break;
        for i in a:
            if i.islowwer():
                status3=True
                break;
        if status1 and status2 and status3:
            return True
        else:
            return False
    else:
        return False

print(checkio('A12313pokl'))


#uloha naprogramovat krajsie (vylepsit otrasny dudikov kod)
#map function, lambda function? - anonymna funkcia - ako ju zavolat - zavola sa len kde sa napise
--------------------------------------------------------------------------------------------------------
#bird language
def translate(birdlanguage:str)->str:
    a=birdlanguage
    count=0
    final=''
    vow='aeiouy'
    con='qwrtpsdfghjklzxcvbnm'
    while count<len(a):
        #print(a[i])
        if a[count] in vow or a[count] in vow.upper():
            final+=a[count]
            count+=3
        elif a[count] in con or a[count] in con.lower():
            final+=a[count]
            count+=2
        else:
            final+=a[count]
            count+=1
    return final

print(translate('hieeelalaooo'))
print(translate('hoooowe yyyooouuu duoooiiine'))
---------------------------------------------------------------------------------------------------------------
#alternation
import random
def alternation(length=5)->str: #defaultna hodnota length=5
    final=''
    vow='aeiouy'
    con='qwrtpsdfghjklzxcvbnm'
    for i in range(length):
        #final+=random.choice(con)
        index=random.randrange(0,len(con))
        final+=con[index]
        final+=random.choice(vow)
    return final.calitalize()

print(alternation())
