介绍：
  Merkle Tree 本身也算是一个哈希列表，只不过是在这个基础上又引入了树形结构，从而获得了更高的灵活性。

  在最底层，和哈希列表一样，我们把数据分成小的数据块，有相应的哈希和它对应。但是往上走，并不是直接去运算根哈希，而是把相邻的两个哈希合并成一个字符串，然后运算这个字符串的哈希，这样每两个哈希就组队打包，得到了一个高一层的”子哈希“。如果最底层的哈希总数是单数，那到最后必然出现一个单个哈希，这种情况就直接对它进行哈希运算，所以也能得到它的子哈希。于是往上推，依然是一样的方式，可以得到数目更少的新一级哈希，最终必然形成一棵倒挂的树，到了树根的这个位置，这一代就剩下一个根哈希了，我们把它叫做 Merkle Root 。如下图所示
![Image text](https://github.com/getpdp/Homework/blob/main/Merkle%20Tree/figures/0.png)
我们可以依据此结构可以快速检索一个数据Element是否在数据集dataset内。同时Merkel Tree可以实现插入，删除等更新操作。在P2P网络和数字签名中都有应用。
以下为实现一个简单的Merkel Tree的检索工作。
在生成数据集的时候，假设其中一个数据为字符串‘abcdefg’,余下的均为指定长度的随机字符串。随后检索该字符串是否在Merkel Tree内：
![Image text](https://github.com/getpdp/Homework/blob/main/Merkle%20Tree/figures/1.png)
![Image text](https://github.com/getpdp/Homework/blob/main/Merkle%20Tree/figures/2.png)
![Image text](https://github.com/getpdp/Homework/blob/main/Merkle%20Tree/figures/3.png)
我们可以发现该字符串能在Merkel Tree上检索到。
同理，如果随机生成100000个数据，而不知道其中任意一个数据时，检索字符串‘abcdefg’是否在Merkel Tree内：
![Image text](https://github.com/getpdp/Homework/blob/main/Merkle%20Tree/figures/4.png)
![Image text](https://github.com/getpdp/Homework/blob/main/Merkle%20Tree/figures/5.png)
经观察我们发现随机生成的字符串没有‘abcdefg’，Merkel Tree的简单实现完成
