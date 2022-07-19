# 运算函数
def Mod32(a,b):

    x = (a+b)%(2**32)
    ans = str(x)
    return ans



def MoveLeft(text, num):


    text = str(text)
    return (text[num:] + text[:num])



def Xor(x,y):

    result =''
    if len(x)!=len(y):
        
        return False
    for i in range(len(y)):
        if x[i]==y[i]:
            result += '0'
        else:
            result += '1'
    return result


def Or(a,b):

    result =''
    if len(a)!=len(b):
        print("Length does not equal")
        return False
    for i in range(len(a)):
        if (a[i]=='1')|(b[i]=='1'):
            result += '1'
        else:
            result += '0'

    return result




def And(a,b):

    result =''
    if len(a)!=len(b):
        print("Length does not equal")
        return False
    for i in range(len(a)):
        if (a[i]=='1')&(b[i]=='1'):
            result += '1'
        else:
            result += '0'
    return result




def Not(a):

    result = ''
    for ch in a:
        if ch == '1':
            result = result + '0'
        else:
            result = result + '1'
    return result



def Substitute(x, mode):

    if mode == 0:
        ans = Xor(Xor(x,MoveLeft(x,9)),MoveLeft(x,17))
    else:
        ans = Xor(Xor(x,MoveLeft(x,15)),MoveLeft(x,23))
    return ans


def MessageFilling(M):
    '''假设消息m的长度l为此特串。首先将比特"1” 添加到消息的末尾,再添加k个"0”,k是满

足1+l+k=448mod512的最小的非负整数。然后再添加一个64位比特串,该比特串是长度的二进

制表示。填充后的消息m'的比特长度为512的倍数。'''
    
    bin_message = ' '.join(format(ord(c), 'b') for c in M)

    length = len(bin_message)

    bin_message = bin_message + '1'

    while len(bin_message)%512!=448:
        bin_message += '0'
    length_bin = bin(length)[2:]

    while len(length_bin)<64:
            length_bin = '0' + length_bin

    bin_message = bin_message + length_bin

    return bin_message


def Iteration(m):
    IV = {}
    IV[0] = '7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e'
    # IV[0]作为迭代的初始值
    length = len(m)
    n = length//512
    b = {}#作为填充后的消息分组
    for i in range(n):
        b[i] = m[512*i:512*(i+1)]
        w = Expansion(b[i])
        IV[i+1] = Compression(w,IV[i])

    return IV[n]





def BlockToHex(text):

    text = str(text)
    while len(text)<32:
        text = '0' + text
    text_16 = ''
    for i in range(8):
        tmp = hex(int(text[4*i:4*(i+1)],base = 2))[2:]
        text_16 = text_16 + tmp   
    return text_16

def BinToHex(text):
    text = str(text)
    while len(text)<32:
        text = '0' + text
    text_16 = ''
    for i in range(len(text)//4):
        tmp = hex(int(text[4*i:4*(i+1)],base = 2))[2:]
        text_16 = text_16 + tmp
    return text_16


def HexToBin(text):
    text_2 = ''
    text = str(text)
    for ch in text:
        tmp = bin(int(ch ,base = 16))[2:]
        for i in range(4):
            if len(tmp)%4!=0:
                tmp = '0' + tmp
        text_2 = text_2 + tmp   
    while len(text_2)<32:
        text_2 = '0' + text_2      
    return text_2

# 10进制转2进制
def OctToBin(text):
    text_10 = ''
    text = str(text)
    tmp = bin(int(text ,base = 10))[2:]
    text_10 = text_10 + tmp  
    while len(text_10)<32:
        text_10 = '0' + text_10      
    return text_10

def OctToHex(text):
    text_10 = ''
    text = str(text)
    tmp = hex(int(text ,base = 10))[2:]
    text_10 = text_10 + tmp     
    while len(text_10)<8:
        text_10 = '0' + text_10   
    return text_10



def Expansion(b):

    w = {}
    for i in range(16):
        w[i] = b[i*32:(i+1)*32]
    for j in range(16, 68):
        tmp = Xor(Xor(w[j-16],w[j-9]),MoveLeft(w[j-3],15))
        tmp = Substitute(tmp, 1) 
        w[j] = Xor(Xor(tmp, MoveLeft(w[j-13],7)), w[j-6])
    for j in range(64):
        w[j+68] = Xor(w[j],w[j+4])
    for i in w:
        text = w[i]
        while len(text)<32:
            text = '0' + text
        text_16 = ''
        for j in range(8):
            tmp = hex(int(text[4*j:4*(j+1)],base = 2))[2:]
            text_16 = text_16 + tmp   
        w[i] = BlockToHex(w[i])
    return w



def FF(x,y,z,k):
    if((k>=0)&(k<=15)):
        ans = Xor(Xor(x,y),z)
    else:
        ans = Or(Or(And(x,y),And(x,z)),And(y,z))
    return ans


def GG(x,y,z,k):
    if((k>=0)&(k<=15)):
        ans = Xor(Xor(x,y),z)
    else:
        ans = Or(And(x,y),And(Not(x),z))
    return ans



def Compression(w,IV):
    '''压缩函数，输出一个256bit的杂凑值'''
    A = IV[0:8]
    B = IV[8:16]
    C = IV[16:24]
    D = IV[24:32]
    E = IV[32:40]
    F = IV[40:48]
    G = IV[48:56]
    H = IV[56:64]

    SS1 = ''
    SS2 = ''
    TT1 = ''
    TT2 = ''
    
    for j in range(64):
        if int(j)<=15:
            T = '79cc4519' 
        else:
            T = '7a879d8a'
        SS1 = MoveLeft(OctToBin(Mod32(int(MoveLeft(HexToBin(A),12), 2) + int(HexToBin(E), 2) + int(MoveLeft(HexToBin(T),j%32), 2) ,0)), 7)
        SS2 = Xor(SS1, MoveLeft(HexToBin(A),12))
        TT1 = int(Mod32(int(FF(HexToBin(A),HexToBin(B),HexToBin(C),j),2) + int(HexToBin(D),2) + int(SS2,2) + int(HexToBin(w[j+68]),2),0),10)
        TT2 = int(Mod32(int(GG(HexToBin(E),HexToBin(F),HexToBin(G),j),2) + int(HexToBin(H),2) + int(SS1,2) + int(HexToBin(w[j]),2),0),10)
        D = C
        C = BlockToHex(MoveLeft(HexToBin(B),9))
        B = A
        A = OctToHex(TT1)
        H = G
        G = BlockToHex(MoveLeft(HexToBin(F),19))
        F = E
        E = BlockToHex(Substitute(OctToBin(TT2),0))

    r = A+B+C+D+E+F+G+H
    r = HexToBin(r)
    v = HexToBin(IV)
    return BinToHex(Xor(r,v))

def encrypt(Message):
    filled_m=MessageFilling(Message)
    w=Expansion(filled_m)
    b=Iteration(filled_m)
    return b




if __name__ == "__main__":
    M = 'sadofiqywoefyoertfdedrv' # 要加密的内容
    filled_m = MessageFilling(M)
    w = Expansion(filled_m)
    b = Iteration(filled_m)
    print(b)

