
from hashlib import sha256
import random
import string
import math
'''我们认定一个数据块的长度为16个字节,不足的用0填充'''
def GenRandDatas(num):
    datas=[]
    for j in range(num):
        d=''
        for i in range(random.randint(5,16)):
            d+=random.choice(string.digits+string.ascii_letters)
        while len(d)<16:
            d='0'+d
        datas.append(d)
    # datas[0]='abcdefg'#验证元素是否存在时用的
    return datas

def Hash(num):
    val=sha256(num.encode(encoding='utf-8')).hexdigest()
    return val
# 随机生成data
def TransformData(length):
    res = []
    for i in range(length):
        block = [random.choice(string.digits + string.ascii_letters) for i in range(10)]  # 一个消息块长为5
        res.append(''.join(block))
    return res

def Node(datas):
    nodes=[]
    for data in datas:
        node=sha256(data.encode(encoding='utf-8')).hexdigest()
        nodes.append(node)
    return nodes
# 生成MerkleTree
def GenMerkelTree(num):
    datas=GenRandDatas(num)
    nodes=Node(datas)#等价于叶结点
    depth = math.ceil(math.log2(len(nodes)) + 1)  # merkle tree深度
    if len(nodes)==1:return nodes
    temp=nodes
    tree=[]
    tree.append(nodes)
    while len(temp)>1:
        uppernodes=[]
        for i in range(0,len(temp),2):
            left=temp[i]
            if i+1==len(temp):right=left
            else:right=temp[i+1]
            uppernodes.append(Hash(left+right))
        temp=uppernodes
        tree.append(uppernodes)

    return tree




def proof(Query, Merkle, root):
    hash_val = (sha256(Query.encode(encoding='utf-8'))).hexdigest()
    if hash_val in Merkle[0]:
        val_index = Merkle[0].index(hash_val)  
    else:
        return "This message isn't in the dataset."
    depth = len(Merkle)  
    Route= []  
    for i in range(depth - 1):
        if val_index % 2 == 0:  # 左子结点
            if len(Merkle[i]) - 1 != val_index:  
                Route.append(['l', Merkle[i][val_index + 1]])
        else:  # 右子结点
            Route.append(['r', Merkle[i][val_index - 1]])
        val_index = int(val_index / 2)    
    for ele in Route:
        if ele[0] == 'l':
            hash_val = sha256(hash_val.encode(encoding='utf-8') + ele[1].encode(encoding='utf-8')).hexdigest()
        else:
            hash_val = sha256(ele[1].encode(encoding='utf-8') + hash_val.encode(encoding='utf-8')).hexdigest()
    if hash_val == root:
        return "is in the merkle tree."
    else:
        return " is in the dataset, but it isn't in the merkle tree."


if __name__ == "__main__":
    guess = 'abcdefg'          # 猜测guess在不在树内
    Merkle = GenMerkelTree(100000)
    root = Merkle[-1][0]
    print("The message:", "[",guess, "]",proof(guess, Merkle, root))