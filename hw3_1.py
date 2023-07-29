#hw3

from vpython import*
g = 9.8
size, m = [0.06, 0.04], [0.2, 0.12]
L, k = 0.5, 15

scene = canvas(width = 500, height = 500, center = vec(0,-0.2,0), background = vec(0.5,0.5,1))
#ceiling = box(length = 0.8, height = 0.005, width = 0.8, color = color.blue)
balls = []
for i in range(2):
    ball = sphere (pos = vec(i*1.1*L, size[i] ,0), radius = size[i],color= color.red)
    mall.m= m[i]
    ball.v = vec(0, 0, 0)
    balls.append(ball)
"""    

spring = helix(pos = vec(0, size, 0), radius=0.02, thickness =0.01)
spring.axis = balls[i].pos-spring.pos
"""
"""
dt = 0.001
while True:
    rate(1000)
    spring.axis = ball.pos - spring.pos

    springForce = -k*(mag(spring.axis) - L)*spring.axis.norm()
    ball.a = vector(0, -g, 0) + springForce/m

    ball.v += ball.a*dt
    ball.pos += ball.v*dt

""""
