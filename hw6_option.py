#hw6

from vpython import *
size, m = 0.02, 0.2 # ball size = 0.02 m, ball mass = 0.2kg
L, k, K = 0.2, 20,5.0 # spring original length = 0.2m, force constant = 20 N/m
amplitude = 0.03
b1 = 0.05 * m * sqrt(k/m)
b2 = 0.0025 * m * sqrt(k/m)
fa = 0.1
omega = sqrt(k+K/m)


scene = canvas(width=600, height=400, fov = 0.03, align = 'left', center=vec(0.3, 0, 0), background=vec(0.5,0.5,0))
wall_left = box(length=0.005, height=0.3, width=0.3, color=color.blue) # left wall
ball1 = sphere(radius = size, color=color.red) # ball
spring1 = helix(radius=0.015, thickness =0.01)

wall_right = box(pos=vec(3*L,0,0),length=0.005, height=0.3, width=0.3, color=color.blue) #  wall
ball2 = sphere(pos=vec(2*L,0,0),radius = size, color=color.red) # ball2
spring2 = helix(pos=vec(3*L,0,0),radius=0.015, thickness =0.01)

spring3 = helix(pos=vec(L,0,0),radius=0.01, thickness =0.01)

oscillation = graph(width = 400, align = 'left', xtitle='t',ytitle='x',background=vec(0.5,0.5,0))
x=gcurve(color=color.red,graph = oscillation)

ball1.pos = vector(L+amplitude, 0 , 0) # ball initial position
ball1.v = vector(0, 0, 0) # ball initial velocity
ball1.m = m
spring1.pos = vector(0, 0, 0)

ball2.pos = vector(2*L-amplitude, 0 , 0) # ball initial position
ball2.v = vector(0, 0, 0) # ball initial velocity
ball2.m = m
#spring2.pos = vector(0, 0, 0)
t, dt = 0, 0.001
T = 2*pi / omega
while True:
    rate(1000)
    
    spring1.axis = ball1.pos - spring1.pos # spring extended from spring endpoint A to ball
    spring2.axis = ball2.pos - spring2.pos
    spring3.axis = ball2.pos - ball1.pos
    
    spring_force1 = - k * (mag(spring1.axis) - L) * norm(spring1.axis) # spring force vector
    spring_force2 = - k * (mag(spring2.axis) - L) * norm(spring2.axis)
    f1 = -b1 * ball1.v+vec(fa*sin(omega*t),0,0)
    ball1.a = (spring_force1 +f1) / ball1.m # ball acceleration = spring force /m - damping
    ball1.v += ball1.a*dt
    ball1.pos += ball1.v*dt

    f2 = -b2 * ball2.v+vec(fa*sin(omega*t),0,0)
    ball2.a = (spring_force2 +f2) / ball2.m # ball acceleration = spring force /m - damping
    ball2.v += ball2.a*dt
    ball2.pos += ball2.v*dt
    t += dt
    x.plot(pos=(t,ball1.pos.x - L))
