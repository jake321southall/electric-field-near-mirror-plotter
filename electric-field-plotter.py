# -*- coding: utf-8 -*-
"""
This program will calculate the E-field expectation value of a 
coherent state at time t=0 in presense of a square potential that 
is only non-zero in the domain -0.5<x<0.5. The height of this 
potential can be adjusted below. This corresponds to equation (77)
in extension18 with Omega(x) described as above, theta=0,
amplitude of eaach wave set to 1 and k_0 set to 1.
"""


# importing the required modules
import matplotlib.pyplot as plt 
import numpy as np

#Calculating Omega(x) integrals
def int_omega_plus(x,t,height):
    if x > 0.5:
        int_omega_plus = 0
    elif x > -0.5:
        if x + t > 0.5:
            int_omega_plus = (height)*(0.5-x)
        else:
            int_omega_plus = (height)*(t)
    else:
        if x + t < -0.5:
            int_omega_plus = 0
        elif x + t < 0.5:
            int_omega_plus = (height)*(x + t + 0.5)
        else:
            int_omega_plus = height
    return int_omega_plus

def int_omega_minus(x,t,height):
    if x < -0.5:
        int_omega_minus = 0
    elif x < 0.5:
        if x - t < -0.5:
            int_omega_minus = (height)*(x+0.5)
        else:
            int_omega_minus = (height)*(t)
    else:
        if x - t > 0.5:
            int_omega_minus = 0
        elif x - t > -0.5:
            int_omega_minus = (height)*(0.5-(x-t))
        else:
            int_omega_minus = height
    return int_omega_minus

#setting our initial time t=0
t = 0

#setting the height of our potential, pi/2\pm n*pi corresponds to 
#full reflection.
#for this potential, the height is equal to it's area under the 
#curve, i.e. area= width x height and we have width=1 here.
#This parameter can be adjusted to see different reflective and
#transmissve rates.
height =(np.pi/2)

#creating our while loop, during each iteration it will print
#the <E(x,t)> values to the console, increase t, then wait 
#for the users command to continue with the new t value
#To exit the loop will require the users input in the console,
#i.e. crtl + c
while t > -1:
    #creating our x-axis array
    x = np.arange(-15*np.pi,15*np.pi,0.1)
    
    #creating our empty omega minus and plus integrals
    int_omega_plus_arr = []
    int_omega_minus_arr = []
    
    #appending our omega integral values for each x to our arrays
    for x in x:
        int_omega_plus_arr.append(int_omega_plus(x,t, height))
        int_omega_minus_arr.append(int_omega_minus(x,t, height))
        
    #Taking the cos and sin of each value in the arrays
    int_omega_minus_cos = np.cos(int_omega_minus_arr) 
    int_omega_plus_sin = np.sin(int_omega_plus_arr) 
    
    x = np.arange(-15*np.pi,15*np.pi,0.1)
    #creating our right moving wave terms
    y = np.cos(x-t)*int_omega_minus_cos
    #creating our left moving wave terms
    z = np.cos(-x-t)*int_omega_plus_sin
    #adding the two together 
    w = y + z
    
    # Add title and axis names
    plt.title('E field of coherent state near a mirror')
    plt.xlabel('x')
    plt.ylabel('E field / Amp')

    
    #creating our plots
    
    #plot of right moving wave
    #plt.plot(x,y)
    
    #plot of left moving wave
    #plt.plot(x,z)
    
    #plot of the sum.
    plt.plot(x,w)
    plt.ylim([-2, 2])
    plt.show()
    #increasing t, can adjust this for smoother animations.
    t += (np.pi/10)
    #command to allow user to continue when enter is pressed
    #hold down enter to see 'animation'
    wait = input("PRESS ENTER TO CONTINUE.")

    