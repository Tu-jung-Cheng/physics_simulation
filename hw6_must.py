#hw6_2

from vpython import *
size, m = 0.02, 0.2 # ball size = 0.02 m, ball mass = 0.2kg
L, k = 0.2, 20 # spring original length = 0.2m, force constant = 20 N/m
#amplitude = 0.03
b = 0.05 * m * sqrt(k/m)
fa = 0.1
omega = sqrt(k/m)
work= 0
omega = [0.1*i + 0.7*sqrt(k/m) for i in range(1, int(0.5*sqrt(k/m)/0.1))]

a0,a1,a = 0,0,0

"""
scene = canvas(width=600, height=400, fov = 0.03, align = 'left', center=vec(0.3, 0, 0), background=vec(0.5,0.5,0))
wall_left = box(length=0.005, height=0.3, width=0.3, color=color.blue) # left wall
ball = sphere(radius = size, color=color.red) # ball
spring = helix(radius=0.015, thickness =0.01)
oscillation1 = graph(width = 400, align = 'left', xtitle='t',ytitle='x',background=vec(0.5,0.5,0))
x=gcurve(color=color.red,graph = oscillation1)
"""

oscillation2 = graph(width = 400, align = 'left', xtitle='omega',ytitle='PT',background=vec(0.5,0.5,0))
p=gcurve(color=color.cyan,graph = oscillation2)

class obj: pass
wall_left,spring,ball = obj(),obj(),obj()

wall_left.pos = vec(0,0,0)
spring.pos = wall_left.pos

ball.pos = vector(L, 0 , 0) # ball initial position
ball.v = vector(0, 0, 0) # ball initial velocity
ball.m = m

for omega_d in omega:
    T = 2*pi / omega_d

    t, dt, n, work = 0, 0.001, 1.0, 0
    while t <= 300:
        ##rate(1000)
        spring.axis = ball.pos - spring.pos # spring extended from spring endpoint A to ball
        spring_force = - k * (mag(spring.axis) - L) * norm(spring.axis) # spring force vector
        force = vec(fa*sin(omega_d*t),0,0)
        ball.a = (spring_force +force - b*ball.v) / ball.m # ball acceleration = spring force /m - damping
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        t += dt
        #x.plot(pos=(t,ball.pos.x - L))
        work += dot(force,ball.v)*dt
        A = work/t
    p.plot(pos = (omega_d,A))
    """
        if t/T >n:
            p.plot(pos = (t,work/T))
            n+= 1
            work = 0
    """


# here i neglect the use of parameter 'n' that's because it can be omit without loss of correctness
# in this program no 'n' is used but it could be added later
# 'A' is the average power of the spring-ball system
# we reset it to '0' every time we reset t to '0' 每次都要歸零
# thus we can plot the average power with respect to omega_d by using the 'for' loop 用for迴圈 把每個omega_d都跑過一次
# then we plot it y-axis is A and x-axis is omega_d
        
         
            
         
         
                
        
        
        
            

        
