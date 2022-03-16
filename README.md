# Electric field near mirror plotter

## Description
The main purpose of this project is to plot the equation 

![first equation](https://latex.codecogs.com/gif.latex?y%28x%2Ct%29%3D%5Ccos%5Cleft%28%5Cint_0%5Et%5COmega%28x-ct%27%29%7B%5Crm%20d%7Dt%27%5Cright%29%5Ccos%28x_t%29&plus;%5Csin%5Cleft%28%5Cint_0%5Et%5COmega%28x&plus;ct%27%29%7B%5Crm%20d%7Dt%27%5Cright%29%5Ccos%5Cleft%28x_%7B-t%7D%5Cright%29) 

where *x* denotes the coordinate along the *x*-axis, *t* denotes time,

![second equation](https://latex.codecogs.com/gif.latex?%5COmega%28x%29%3D%20%5Cbegin%7Bcases%7D%20%5Cfrac%7B%5Cpi%7D%7B2%7D%20%26%20%7B%5Crm%20if%7D%20-%5Cfrac%7B1%7D%7B2%7D%5Cleq%20x%5Cleq%20%5Cfrac%7B1%7D%7B2%7D%2C%20%5C%5C%200%20%26%20%7B%5Crm%20otherwise%7D.%20%5Cend%7Bcases%7D)

and

![third equation](https://latex.codecogs.com/gif.latex?x_t%3Dx-ct%5C%2C%2C%5C%2C%5C%2Cx_%7B-t%7D%3Dx&plus;ct%5C%2C.)

The above equation represents the electric field expectation value of a coherent state in the presence of a mirror, in a fully quantum setting. We found that the results reproduce the classical dynamics of a sinusoidal wave in the presense of the mirror and this project gives a nice visual representataion of this behaviour.
To understand how this equation is derived, please see our [paper](https://www.tandfonline.com/doi/full/10.1080/09500340.2021.1936241); it requires a good understanding of quantum optics!

## Features
The program in E_exp_plotter_final.py initializes time at *t=0* and increases by a value after each plot that is specified by the user in the script. The value of Omega can also be changed in the script.

## How to use
Packages used are matplotlib.pyplot and numpy. I used spyder to run my python code.


