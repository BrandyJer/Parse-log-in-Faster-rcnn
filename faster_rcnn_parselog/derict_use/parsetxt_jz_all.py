# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 15:41:02 2017

@author: Administrator
"""

###利用parse_log.sh生成的数值列表.txt文件生成loss曲线

import matplotlib.pyplot as plt
#import numpy as np 

Iters = []
TrainingLoss1 = []
TrainingLoss2 = []
TrainingLoss3 = []

averge_loss1 = []
averge_loss2 = []
averge_loss3 = []

averge_Iters = []
lossvalue1 = 0
lossvalue2 = 0
lossvalue3 = 0

i = 0
#indexname = ('Iters', 'TrainingLoss')
with open(r'F:\AGraduateLab\AJZlearning\AAI\end2end_ZF_1type_iter6.txt', 'r') as f:
    lineper = f.readline()
    lineper = f.readline()
    while lineper:
        values = lineper.split()
        Iters.append(float(values[0]))
        TrainingLoss1.append(float(values[2]))
        lineper = f.readline()
        
with open(r'F:\AGraduateLab\AJZlearning\AAI\2types_wangmeihan_ZF_iter6.txt', 'r') as f:
    lineper = f.readline()
    lineper = f.readline()
    while lineper:
        values = lineper.split()
#        Iters.append(float(values[0]))
        TrainingLoss2.append(float(values[2]))
        lineper = f.readline()
        
with open(r'F:\AGraduateLab\AJZlearning\AAI\VGG16_1typetrain.txt', 'r') as f:
    lineper = f.readline()
    lineper = f.readline()
    while lineper:
        values = lineper.split()
#        Iters.append(float(values[0]))
        TrainingLoss3.append(float(values[2]))
        lineper = f.readline()
        
for Iter in Iters:
    lossvalue1 = lossvalue1+TrainingLoss1[i]
    lossvalue2 = lossvalue2+TrainingLoss2[i]
    lossvalue3 = lossvalue3+TrainingLoss3[i]
    i = i+1
    if i%20 == 0:
        lossvalue1 = lossvalue1/20.0
        lossvalue2 = lossvalue2/20.0
        lossvalue3 = lossvalue3/20.0
        
        averge_loss1.append(lossvalue1)
        averge_loss2.append(lossvalue2)
        averge_loss3.append(lossvalue3)
        
        averge_Iters.append(Iters[i-1])
        lossvalue1 = 0
        lossvalue2 = 0
        lossvalue3 = 0
    
    
#plt.title('Iters VS TrainingLoss')
plt.xlabel('Train loss')
plt.ylabel('Iters')
plt.plot(averge_Iters, averge_loss1, "r", label = '1type_ZF')
plt.plot(averge_Iters, averge_loss2, "g", label = '2types_ZF')
plt.plot(averge_Iters, averge_loss3, "b", label = '1type_VGG16')
#plt.plot([0, len(averge_loss)], averge_loss, label = 'end2end_VGG16')
plt.legend(loc = 'upper right')
plt.show()