#Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import time


def func_fx(x):
    fx = (4*x**3) +(x**2) -(7*x)+14
    #fx = 0.65-(0.75/(1+x)**2)-(0.65*x*(np.arctan(np.float64(1/np.float64(x)))))
    #fx=np.sin(x)
    #fx = -((1/((x-1) ** 2))*(np.log(x) - (2*(x - 1)/(x + 1))))
    #fx = np.exp(-x) - np.cos(x)
    return fx


def check_pos(x1,x2):
    if x2<x1:
        label='right'
    else:
        label='left'
    return label

def update_interior(xl, xu,iteration, L0):
    d=(((np.sqrt(5)-1)/2)**iteration)*(L0)
    x1=xl+d
    x2=xu-d
    return x1,x2


#FINDING MAXIMUM OF THE FUNCTION using Golden Section Method
def find_max(xl,xu,x1,x2,label,iteration, L0):
    fx1=func_fx(x1)
    fx2=func_fx(x2)
    if fx2>fx1 and label=='right':
        xl=xl
        xu=x1
        new_x=update_interior(xl,xu,iteration, L0)
        x1=new_x[0]
        x2=new_x[1]
    else:
        xl=x2
        xu=xu
        new_x=update_interior(xl,xu,iteration, L0)
        x1=new_x[0]
        x2=new_x[1]
    return xl,xu


#FINDING MINIMUM OF THE FUNCTION using Golden Section Method
def find_min(xl,xu,x1,x2,label,iteration,L0):
    fx1=func_fx(x1)
    fx2=func_fx(x2)
    if fx2>fx1 and label=='right':
        xl=x2
        xu=xu
        new_x=update_interior(xl,xu,iteration,L0)
        x1=new_x[0]
        x2=new_x[1]
    else:
        xl=xl
        xu=x1
        new_x=update_interior(xl,xu, iteration,L0)
        x1=new_x[0]
        x2=new_x[1]
    return xl,xu


#PLOTTING FUNCTION
def plot_graph(xl,xu,x1,x2):
    x=np.linspace(0,6,100)
    y=func_fx(x)
    plt.plot(x,y)
    plt.plot([0,6],[0,0],'k')
    
    #plot x1 point
    plt.plot(x1,func_fx(x1),'ro',label='x1')
    plt.plot([x1,x1],[0,func_fx(x1)],'k')
    
    #plot x2 point
    plt.plot(x2,func_fx(x2),'bo',label='x2')
    plt.plot([x2,x2],[0,func_fx(x2)],'k')
    
    #plot xl line
    plt.plot([xl,xl],[0,func_fx(xl)])
    plt.annotate('xl',xy=(xl-0.01,-0.2))
        
    #plot xu line
    plt.plot([xu,xu],[0,func_fx(xu)])
    plt.annotate('xu',xy=(xu-0.01,-0.2))
        
    #plot x1 line
    plt.plot([x1,x1],[0,func_fx(x1)],'k')
    plt.annotate('x1',xy=(x1-0.01,-0.2))
        
    #plot x2 line
    plt.plot([x2,x2],[0,func_fx(x2)],'k')
    plt.annotate('x2',xy=(x2-0.01,-0.2))
    
    #y-axis limit
    plt.ylim([-100,100])
    plt.show()
    
    
def golden_search(xl,xu,mode,et):
    it=0
    e=1
    L0 = abs(xu-xl)
    while e>=et:
        new_x=update_interior(xl,xu, it+1, L0)
        x1=new_x[0]
        x2=new_x[1]
        label=check_pos(x1,x2)
        plot_graph(xl,xu,x1,x2) #PLOTTING
        plt.show()
        
        #SELECTING AND UPDATING BOUNDARY-INTERIOR POINTS
        if mode=='max':
            new_boundary=find_max(xl,xu,x1,x2,label,it+1, L0)
        elif mode=='min':
            new_boundary=find_min(xl,xu,x1,x2,label, it+1, L0)
        else:
            print('Please define min/max mode')
            break #exit if mode not min or max
        xl=new_boundary[0]
        xu=new_boundary[1]
        it+=1
        print ('Iteration: ',it)
        e=(abs(xu-xl)) #Error
        print(f'Interval is: [{xl}, {xu}]')
        print('Error:',e)
        time.sleep(1)
    print(f'Final interval is: [{xl}, {xu}]')
    print(f'x_opt = {float(xl+xu)/2} and function value at x_opt = {func_fx(float(xl+xu)/2)}')

 
#EXECUTING GOLDEN SEARCH FUNCTION FOR THE FUNCTION 4x^3+x^2-7x+14 in RANGE 0 to 1
# print("FINDING MINIMA OF THE FUNCTION IN THE GIVEN RANGE")
func_range = [0,1]
golden_search(func_range[0],func_range[1],'min',0.15)