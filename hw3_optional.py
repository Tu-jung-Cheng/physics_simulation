#hw3

from vpython import*
g = 9.8
size= [0.06, 0.04]
m = [0.2, 0.12]
L, k = 0.5, 15
springForce = 0

scene = canvas(width = 500, height = 500, center = vec(0,0,0), background = vec(0.5,0.5,1))
#ceiling = box(length = 0.8, height = 0, width = 0.8, color = color.blue)
balls = []

for i in range(2):
    ball = sphere (pos = vec((i-0.5)*1.1*L, size[i],0), radius = size[i],color= color.red)
    ball.m = m[i]
    ball.v = vec(0, 0, 0)
    balls.append(ball)

spring = helix(pos = vec((-0.5)*1.1*L, size[0],0),radius=0.02, thickness =0.01)
spring.axis = balls[1].pos-spring.pos

vp = balls[0].v.x
t = 0
t0 = 0
dt = 0.001
q=0
while True:
    rate(1000)
    t += dt
    spring.axis = balls[1].pos -balls[0].pos
    springForce = -k*(mag(spring.axis) - L)*spring.axis.norm()
    for i in range(2):
        balls[1].a=springForce/balls[1].m   
        balls[0].a=-springForce/balls[0].m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt

   
    vc = balls[0].v.x
    if(vp > 0 and vc < 0):
        i += 1
        print ('period is',t-t0,'second')
        t0 = t
    vp = vc
    
