#hw3_must
#https://youtu.be/Bn9p0WLSu0Y

from vpython import *
g = 9.8
size, m = 0.05, 0.2
L, k = 0.5, [15, 12, 17]
v = [1, 2, 2.2]
d = [-0.06, 0, -0.1]
springForce = [0,0,0]
scene = canvas(width=400, height=400, center =vec(0.4, 0.2, 0), align = 'left', background=vec(0.5,0.5,1))
floor = box(pos = vec(0.4, 0, 0), length=0.8, height=0.005, width=0.8, color=color.blue)
wall = box(pos= vec(0, 0.05, 0), length = 0.01, height = 0.1, width =0.8)

oscillation = graph(width = 450, align = 'left')
kin = gcurve(graph = oscillation, color = color.blue, width = 3)
potential = gcurve(graph = oscillation, color = color.red, width = 3)

oscillation2 = graph(width = 450, align = 'right')
kin1 = gcurve(graph = oscillation2, color = color.blue, width = 3)
potential1 = gcurve(graph = oscillation2, color = color.red, width = 3)

balls = []
for i in range(3):
    ball = sphere(pos = vec(L+d[i], size, (i-1)*3*size), radius = size, color=color.red)
    ball.v = vec(v[i], 0, 0)
    balls.append(ball)
springs =[]
for i in range(3):
    spring = helix(pos = vec(0, size, (i-1)*3*size), radius=0.02, thickness =0.01)
    spring.axis = balls[i].pos-spring.pos
    spring.k = k[i]
    springs.append(spring)

k0 = 0
U = 0
k1= 0
U1=0
t = 0
##movement
dt = 0.001
n=0
while True:
    rate(1000)
    t+=dt
    n+=1
    for i in range(3):
        springs[i].axis = balls[i].pos - springs[i].pos

        springForce[i] = -springs[i].k*(mag(springs[i].axis) - L)*spring.axis.norm()
        balls[i].a =  springForce[i]/m

        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt


    k0 = 1/2*m*(mag(balls[0].v)**2+mag(balls[1].v)**2+mag(balls[2].v)**2)
    U = 1/2*(springs[0].k*(mag(springs[0].axis) - L)**2+springs[1].k*(mag(springs[1].axis) - L)**2
             +springs[2].k*(mag(springs[2].axis) - L)**2)
        
    k1 += k0
    U1 += U
    kin.plot(pos=(t,k0))
    potential.plot(pos=(t,U))

    kin1.plot(pos=(t,k1/n))
    potential1.plot(pos=(t,U1/n))
