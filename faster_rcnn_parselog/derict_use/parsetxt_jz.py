# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 15:41:02 2017

@author: Administrator
"""

###利用parse_log.sh生成的数值列表.txt文件生成loss曲线

import matplotlib.pyplot as plt
#import numpy as np 

Iters = []
TrainingLoss = []
averge_loss = []
averge_Iters = []
lossvalue = 0
i = 0
#indexname = ('Iters', 'TrainingLoss')
with open(r'F:\AGraduateLab\AJZlearning\AAI\end2end_ZF_1type_iter6.txt', 'r') as f:
    lineper = f.readline()
    lineper = f.readline()
    while lineper:
        values = lineper.split()
        Iters.append(float(values[0]))
        TrainingLoss.append(float(values[2]))
        lineper = f.readline()       
for Iter in Iters:
    lossvalue = lossvalue+TrainingLoss[i]
    i = i+1
    if i%20 == 0:
        lossvalue = lossvalue/20.0
        averge_loss.append(lossvalue)
        averge_Iters.append(Iters[i-1])
        lossvalue = 0
    
    
#plt.title('Iters VS TrainingLoss')
plt.xlabel('Train loss')
plt.ylabel('Iters')
plt.plot(averge_Iters, averge_loss, label = '1type_ZF')
#plt.plot([0, len(averge_loss)], averge_loss, label = 'end2end_VGG16')
plt.legend(loc = 'upper right')
plt.show()