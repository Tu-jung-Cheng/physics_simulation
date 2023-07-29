#hw5

from vpython import *
g, size, height = 9.8, 0.25, 15.0
class any_ball(sphere): # declare any_ball a class with properties (attributes and methods) inherited from sphere
    m = 1.0 # if objects generated by any_ball do not have their own attributes m and v, they will inherit class’s
    v = vector(0,0,0) # attributes here, i.e., m and v
    def kinetic_energy(self):
        return 0.5 * self.m * mag(self.v)**2
scene = canvas(width=800, height=800, center = vec(0,height/2,0), background=vec(0.5,0.5,0))
floor = box(length=30, height=0.01, width=10, color=color.blue)
ball = any_ball(radius = size, color=color.red) # generate ball as an object belonged to any_ball class, and passing arguments into

# any_ball’s initializing function __init__().

print(ball.m, ball.v, ball.kinetic_energy()) # print ball.m, ball.v, but since ball does not have attributes m and v yet. It uses any_ball

# class’s m and v.
# ball.kinetic_energy() calls the kinetic_energy method.

ball.pos, ball.v, ball.m = vector( 0, height, 0), vector(0, 0, 0), 3.0
dt = 0.001
while ball.pos.y >= size:
    rate(1000)
    ball.pos += ball.v*dt
    ball.v.y += - g*dt
print(ball.m, ball.v, ball.kinetic_energy())
