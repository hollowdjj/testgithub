# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:43:24 2021

@author: Administrator
"""
import numpy as np
#import matplotlib.pyplot as plt

#def draw(theta ,totalL,N):
#    L=totalL/N
#    xva = np.zeros(N+1)  
#    yva = np.zeros(N+1)
#    xtemp=0
#    ytemp=0
#    for i in range(N):
#        xtemp=xtemp+L*np.cos(theta[i]*3.1415926/180)
#        xva[i+1]=xtemp
#    for i in range(N):
#        ytemp=ytemp+L*np.sin(theta[i]*3.1415926/180)
#        yva[i+1]=ytemp
#
#    fig = plt.figure()
#    ph = fig.add_subplot(1,1,1)
#    ph.plot(xva,yva,'y-')

def Energy_in(x,L):
    EN=0
    for i in range(len(x)):
        temp=0
        for j in range(0,i):
            temp=temp+np.sin(x[j]*3.1415926/180)*L
        EN=EN+temp
    return EN