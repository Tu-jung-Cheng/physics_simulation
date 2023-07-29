#https://youtu.be/NUCMgzIGp64
import numpy as np
from vpython import *
A, N, omega = 0.10, 50, 0
size, m, k, d = 0.06, 0.1, 10.0, 0.4
scene = canvas(title='Spring Wave', width=800, height=300, background=vec(0.5,0.5,1), center = vec((N-1)*d/2, 0, 0))
"""
balls = [sphere(radius=size, color=color.red, pos=vector(i*d, 0, 0), v=vector(0,0,0)) for i in range(N)] #3
springs = [helix(radius = size/2.0, thickness = d/15.0, pos=vector(i*d, 0, 0), axis=vector(d,0,0)) for i in range(N-1)] #3
"""
#c = curve([vector(i*d, 1.0, 0) for i in range(N)], color=color.black) #1
#ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d, np.arange(N)*d, np.zeros(N), np.ones(N)*d #5
oscillation2 = graph(width = 400, align = 'left', xtitle='wavevector',ytitle='omega',background=vec(0.5,0.5,1))
p=gcurve(color=color.cyan,graph = oscillation2)


n = 1
t, dt = 0, 0.0003
T = 0
ball_pos0,ball_pos1,omega=5,3,0
if n <= N/2:
    Unit_K = 2 * pi/(N*d)
    Wavevector = n * Unit_K
    phase = Wavevector * arange(N) * d
    ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d
    while True:
        rate(10000)
        t += dt
        T+=dt
        ball_pos[0] = A * sin(omega * t ) #4
        ## spring_len[:-1] =
        ## ball_v[1:] += #6
        spring_len[0:-1]=ball_pos[1:]-ball_pos[0:-1]
        spring_len[-1]=N*d+ball_pos[0]-ball_pos[-1]
        ball_v[1:]+=k*((spring_len[1:]-d)-(spring_len[0:-1]-d))/m*dt
        ball_pos0=ball_pos1
        ball_pos1=ball_pos[1]
        
        ball_pos += ball_v*dt
        """
        for i in range(N):
            balls[i].pos.x = ball_pos[i] #3
        for i in range(N-1): #3
            springs[i].pos = balls[i].pos #3
            springs[i].axis = balls[i+1].pos - balls[i].pos #3
        
        #2
        ball_disp = ball_pos - ball_orig
        
        for i in range(N):
            c.modify(i, y = ball_disp[i]*4+1)
"""
        if ball_pos0<ball_pos1 and ball_pos[1]<ball_pos1:
            print(T)
            omega=2*pi/T
            p.plot(pos=(Wavevector,omega))
            T=0
            n+=1
            Unit_K = 2 * pi/(N*d)
            Wavevector = n * Unit_K
            phase = Wavevector * arange(N) * d
            ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d
            ball_pos0,ball_pos1,omega=5,3,0
       

