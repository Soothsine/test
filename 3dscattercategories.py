# -*- coding: utf-8 -*-


from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

x_ticks_labels = ['Flow optimization','Demand prediction','Transport simulation','Efficency','Segmentation']
y_ticks_labels = ['Order data','Fault codes','Temperature','Sales','Warranty']
z_ticks_labels = ['RF regression','Log regression','RNN','RPA','SVM']

x = np.arange(len(x_ticks_labels))
y = np.arange(len(y_ticks_labels))
z = np.arange(len(z_ticks_labels))
 
df=pd.DataFrame({'X': np.array([0,1,2,3,4]), 'Y': np.array([0,1,2,3,4]), 'Z': np.array([0,1,2,3,4]) }) 

fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
ax.scatter(df['X'], df['Y'], df['Z'], c='skyblue', s=200) 

ax.view_init(30, 185) 

ax.set_xticks(x)
ax.set_xticklabels(x_ticks_labels, rotation='vertical', fontsize=12)
ax.set_yticks(y)
ax.set_yticklabels(y_ticks_labels, rotation='vertical', fontsize=12)
ax.set_zticks(z)
ax.set_zticklabels(z_ticks_labels, rotation='horizontal', fontsize=12)

plt.show() 
