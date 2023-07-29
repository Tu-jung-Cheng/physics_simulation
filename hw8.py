#https://youtu.be/cQwsC8BW3oo
from vpython import *
from diatomic import *
N = 20 # 20 molecules
L = ((24.4E-3/(6E23))*N)**(1/3.0)/50 # 2L is the length of the cubic container box, the number is made up
m = 14E-3/6E23 # average mass of O and C
k, T = 1.38E-23, 298.0 # some constants to set up the initial speed
initial_v = (3*k*T/m)**0.5 # some constant
scene = canvas(width = 400, height =400, align = 'left', background = vec(1, 1, 1))
container = box(length = 2*L, height = 2*L, width = 2*L, opacity=0.4, color = color.yellow )
energies = graph(width = 600, align = 'left', ymin=0)
c_avg_com_K = gcurve(color = color.green)
c_avg_v_P = gcurve(color = color.red)
c_avg_v_K = gcurve(color = color.purple)
c_avg_r_K = gcurve(color = color.blue)
COs=[]
for i in range(N): # initialize the 20 CO molecules
    O_pos = vec(random()-0.5, random()-0.5, random()-0.5)*L # random() yields a random number between 0 and 1
    CO = CO_molecule(pos=O_pos, axis = vector(1.0*d, 0, 0)) # generate one CO molecule
    CO.C.v = vector(initial_v*random(), initial_v*random(), initial_v*random()) # set up the initial velocity of C randomly
    CO.O.v = vector(initial_v*random(), initial_v*random(), initial_v*random()) # set up the initial velocity of O randomly
    COs.append(CO) # store this molecule into list COs
#print(COs)
times = 0 # number of loops that has been run

dt = 5E-16
t = 0
n=0
com_K=0
v_K=0
v_P=0
r_K=0
while True:
    rate(3000)
    t+= dt
    n+=1
    for CO in COs:
        CO.time_lapse(dt)
    #collision with molecules
    for i in range(N-1): # the first N-1 molecules
        for j in range(i+1,N): # from i+1 to the last molecules, to avoid double checking
            if abs(mag(COs[i].C.pos-COs[j].C.pos))<=2*size:
                COs[i].C.v,COs[j].C.v=collision(COs[i].C,COs[j].C)
            if abs(mag(COs[i].O.pos-COs[j].O.pos))<=2*size:
                COs[i].O.v,COs[j].O.v=collision(COs[i].O,COs[j].O)
            if abs(mag(COs[i].O.pos-COs[j].C.pos))<=2*size:
                COs[i].C.v,COs[j].O.v=collision(COs[i].C,COs[j].O)
            
             ## change this to check and handle the collisions between the atoms of different molecules
    #collision with walls           
    for CO in COs:
        
        if CO.O.pos.x >= L-size:
            CO.O.v=-CO.O.v 
        if CO.O.pos.y >= L-size :
            CO.O.v=-CO.O.v
        if CO.O.pos.z >= L-size:
            CO.O.v=-CO.O.v
        if CO.O.pos.x <= -L+size:
            CO.O.v=-CO.O.v 
        if CO.O.pos.y <= -L+size :
            CO.O.v=-CO.O.v
        if CO.O.pos.z <= -L+size:
            CO.O.v=-CO.O.v
            
        if CO.C.pos.x >= L-size:
            CO.C.v=-CO.C.v 
        if CO.C.pos.y >= L-size :
            CO.C.v=-CO.C.v
        if CO.C.pos.z >= L-size:
            CO.C.v=-CO.C.v
        if CO.C.pos.x <= -L+size:
            CO.C.v=-CO.C.v 
        if CO.C.pos.y <= -L+size :
            CO.C.v=-CO.C.v
        if CO.C.pos.z <= -L+size:
            CO.C.v=-CO.C.v
        ## change this to check and handle the collision of the atoms of all molecules on all 6 walls
    for i in range(N):
        com_K+=COs[i].com_K()
        v_K+=COs[i].v_K()
        v_P+=COs[i].v_P()
        r_K+=COs[i].r_K()

    c_avg_com_K.plot(pos=(t,com_K/n))
    c_avg_v_K .plot(pos=(t,v_K/n))
    c_avg_v_P .plot(pos=(t,v_P/n))
    c_avg_r_K .plot(pos=(t,r_K/n))

    
        
## sum com_K, v_K, v_P, and r_K for all molecules, respectively, to get total_com_K, total_v_K, total_v_P, total_r_K at the
## current moment
## calculate avg_com_K to be the time average of total_com_K since the beginning of the simulation, and do the same
## for others.
## plot avg_com_K, avg_v_K, avg_v_P, and avg_r_K
