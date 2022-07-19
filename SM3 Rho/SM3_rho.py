
import SM3
import random

def GetRandMessage():
    '''随机生成字符串'''
    str_list=list("abcdefghijklmnopqrst")
    M=''
    length =random.randint(10,60)
    for i in range(length):
        M+=random.choice(str_list)
    return M

def Rho():
    '''生日攻击，寻找碰撞'''
    history = set()
    flag =1
    counter=0
    while(flag):
        if counter>=50000:
            print("cannot find")
            break
        M = GetRandMessage()
        c1 = SM3.encrypt(M)
        c2 = c1[0:16]
        if(c2 in history):
            flag = 0
            print("Find!")
            print(c2)
            break
        else:
            history.add(c2)
           
        print("No conflicts")
        counter+=1
if __name__ == "__main__":
    Rho()