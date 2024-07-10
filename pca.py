# -*- coding:utf-8 -*-
#导包
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取文件
data=pd.read_csv('free-energy-landscape.txt',sep='\t',header=None)

fesvalue=np.array(data[2])
# 因为默认为32*32=1024,所以把其整为32*32格点，横纵坐标可抛弃，因为都是依次的，而且意义不大。
plotvalue=np.reshape(fesvalue,(32,-1))

# 绘图
plt.figure(figsize=(8,8))
plt.imshow(plotvalue,cmap='jet',interpolation='bilinear')
plt.xticks([],[])
plt.yticks([],[])
plt.xlabel('PC1',fontsize=16)
plt.ylabel('PC2',fontsize=16)
#plt.show()
plt.savefig('fes.png',dpi=600)
