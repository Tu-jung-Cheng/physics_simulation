from vpython import *
import numpy as np
from histogram import *
N = 200
m, size = 4E-3/6E23, 31E-12*10 # He atom are 10 times bigger for easiear collision but not too big for accuracy
L = ((24.4E-3/(6E23))*N)**(1/3.0)/2 + size # 2L is the cubic container's original length, width, and height
k, T = 1.38E-23, 298.0 # Boltzmann Constant and initial temperature
t, dt = 0, 3E-13
vrms = (2*k*1.5*T/m)**0.5 # the initial root mean square velocity
stage = 0 # stage number

momentum=0
v_W,move_L=0,0

p,dp=0,0

atoms = [] # list to store atoms
# histogram setting
deltav = 50. # slotwidth for v histogram
vdist = graph(x=800, y=0, ymax = N*deltav/1000.,width=500, height=300, xtitle='v', ytitle='dN', align = 'left')
theory_low_T = gcurve(color=color.cyan) # for plot of the curve for the atom speed distribution
dv = 10.
for v in arange(0.,4201.+dv,dv): # theoretical speed distribution
    theory_low_T.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(2.*pi*k*T))**1.5)*exp((-0.5*m*v**2)/(k*T))*(v**2)*dv))
observation = ghistogram(graph = vdist, bins=arange(0.,4200.,deltav), color=color.red) # for the simulation speed distribution
#initialization
scene = canvas(width=500, height=500, background=vector(0.2,0.2,0), align = 'left')
container = box(length = 2*L, height = 2*L, width = 2*L, opacity=0.2, color = color.yellow )
p_a, v_a,k_a = np.zeros((N,3)), np.zeros((N,3)), np.zeros((N,3)) # particle position array and particle velocity array, N particles and 3 for x, y, z

for i in range(N):
    p_a[i] = [2 * L*random() - L, 2 * L*random() - L, 2 * L*random() - L] # particle is initially random positioned in container
    if i== N-1: # the last atom is with yellow color and leaves a trail
        atom = sphere(pos=vector(p_a[i, 0], p_a[i, 1], p_a[i, 2]), radius = size, color=color.yellow, make_trail = True, retain = 50)
    else: # other atoms are with random color and leaves no trail
        atom = sphere(pos=vector(p_a[i, 0], p_a[i, 1], p_a[i, 2]), radius = size, color=vector(random(), random(), random()))
    ra = pi*random()
    rb = 2*pi*random()
    v_a[i] = [vrms*sin(ra)*cos(rb), vrms*sin(ra)*sin(rb), vrms*cos(ra)] # particle initially same speed but random direction
    atoms.append(atom)
def vcollision(a1p, a2p, a1v,a2v): # the function for handling velocity after collisions between two atoms
    v1prime = a1v - (a1p - a2p) * sum((a1v-a2v)*(a1p-a2p)) / sum((a1p-a2p)**2)
    v2prime = a2v - (a2p - a1p) * sum((a2v-a1v)*(a2p-a1p)) / sum((a2p-a1p)**2)
    return v1prime, v2prime

def keyinput(evt):
    global stage
    s=evt.key 
    if s =="n":
        stage+=1
        
    
scene.bind('keydown', keyinput)
print ('------------------------------stage 0------------------------------')

aux = True
time = 0
z=0
while True:
    t += dt
    time+=dt  
    rate(10000)
    p_a += v_a*dt # calculate new positions for all atoms
    
    for i in range(N):
        atoms[i].pos = vector(p_a[i, 0], p_a[i, 1], p_a[i, 2]) # to display atoms at new positions
    if stage != 1 :
        observation.plot(data = np.sqrt(np.sum(np.square(v_a),-1))) ## freeze histogram for stage != 1
    """
    if stage ==1:
        L0 = L0-v_W*dt
        if stage <= L/2:
            stage +=1
    """
    
    ### find collisions between pairs of atoms, and handle their collisions
    r_array = p_a-p_a[:,np.newaxis] # array for vector from one atom to another atom for all pairs of atoms
    rmag = np.sqrt(np.sum(np.square(r_array),-1)) # distance array between atoms for all pairs of atoms
    hit = np.less_equal(rmag,2*size)-np.identity(N) # if smaller than 2*size meaning these two atoms might hit each other
    hitlist = np.sort(np.nonzero(hit.flat)[0]).tolist() # change hit to a list
    for ij in hitlist: # i,j encoded as i*Natoms+j
        i, j = divmod(ij,N) # atom pair, i-th and j-th atoms, hit each other
        hitlist.remove(j*N+i) # remove j,i pair from list to avoid handling the collision twice
        if sum((p_a[i]-p_a[j])*(v_a[i]-v_a[j])) < 0 : # only handling collision if two atoms are approaching each other
            v_a[i], v_a[j] = vcollision(p_a[i], p_a[j], v_a[i], v_a[j]) # handle collision
    #find collisions between the atoms and the walls, and handle their elastic collisions
    if stage !=1:
        for i in range(N):
            if abs(p_a[i][0]) >= L - size and p_a[i][0]*v_a[i][0] > 0 :
                v_a[i][0] = - v_a[i][0]
                dp+=m*abs(2*v_a[i][0])
            if abs(p_a[i][1]) >= L - size and p_a[i][1]*v_a[i][1] > 0 :
                v_a[i][1] = - v_a[i][1]
                dp+=2*m*abs(v_a[i][1])
            if abs(p_a[i][2]) >= L - size and p_a[i][2]*v_a[i][2] > 0 :
                v_a[i][2] = - v_a[i][2]
                dp+=2*m*abs(v_a[i][2])

    if stage ==1:
        for i in range(N):
            if (p_a[i][0]) >= container.length/2 - size and p_a[i][0]*v_a[i][0] > 0 :
                v_a[i][0] = - v_a[i][0] -2*v_W
                dp+=m*abs(2*v_a[i][0])
            if (p_a[i][0]) <= -container.length/2 + size and p_a[i][0]*v_a[i][0] > 0 :
                v_a[i][0] = - v_a[i][0] +2*v_W
                dp+=m*abs(2*v_a[i][0])
                
            if abs(p_a[i][1]) >= L - size and p_a[i][1]*v_a[i][1] > 0 :
                v_a[i][1] = - v_a[i][1]
                dp+=2*m*abs(v_a[i][1])
            if abs(p_a[i][2]) >= L - size and p_a[i][2]*v_a[i][2] > 0 :
                v_a[i][2] = - v_a[i][2]
                dp+=2*m*abs(v_a[i][2])
    k_a=0.5*m*v_a*v_a       
    if time>=1000*dt:
        vol=container.length*container.width*container.height
        p=dp/(time*4*(move_L+L)*2*size)
        T=0
        z+=1
        for i in range(N):
            T+=k_a[i]/(N*k) 
        print ("#",z,'T = ',T,'volume = ',vol,' p = ',p)
        print ("PV",p*vol,'NkT = ',N*k*T,'p*(V**gamma), = ',p*(vol**5/3))
        time=0
        dp=0
        print(stage)
    if stage==1:
        if container.length>=L:
            print ('------------------------------stage 1------------------------------')
            v_W=L/(20000.0*dt)
            move_L+=-v_W*dt
            container.length+=2*move_L
            #print(True)
        else:
            stage+=1
    
    if stage==2 and aux:
        v_W=0
        theory_high_T=gcurve(color=color.cyan)
        dv=10.
        aux = False
        for v in arange(0.,4201.+dv,dv):
            theory_high_T.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(4.*pi*k*T))**1)*exp((-0.5*m*v**2)/(k*T))*v*dv))
        observation = ghistogram(graph = vdist, bins=arange(0.,4200.,deltav), color=color.blue)
            
        print ('------------------------------stage 2------------------------------')
        container.length  = 2*L
    

    if stage==3:
        #print ('------------------------------stage 3------------------------------')
        move_L=L
        container.length=2*move_L
        
    
