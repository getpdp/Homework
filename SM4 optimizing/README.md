介绍：
SM4是一种分组密码算法，其分组长度为128位（即16字节，4字），密钥长度也为128位（即16字节，4字）。其加解密过程采用了32轮迭代机制（与DES、AES类似），每一轮需要一个轮密钥.SM4的分组长度为4字，因此，其输入是4字的明文 X1,X2,X3,X4，经过加密后，得到的输出是4字的密文 Y1,Y2,Y3,Y4.这个加密过程分为两步，由32次轮迭代和1次反序变换组成。

对于4字明文P进行加密得到的密文为：
![Image text](https://github.com/getpdp/Homework/blob/main/SM4%20optimizing/figures/0.png)
![Image text](https://github.com/getpdp/Homework/blob/main/SM4%20optimizing/figures/1.png)
