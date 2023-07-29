#hw4_must
#https://youtu.be/6ixPAwBiMvA
from vpython import*
g =9.8
size,m = 0.02, 0.5
L,k = 0.5, 15000
v = [0,0,0,0,0]
N,NN =2,5
springForce= [0,0,0,0,0]
scene = canvas(width = 500, height = 500, center = vec(0,-0.2,0), background= vec(0.5,0.5,1))
ceiling = box(length= 0.8, height= 0.005, width= 0.8,color= color.blue)

def af_col_v(m1, m2, v1, v2, x1, x2): # function after collision velocity
    v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime)

balls = []
for i in range(NN):
    ball = sphere(pos = vec(i*size*2-0.1,-L-m*g/k,0), radius = size)
    ball.v = vec(v[i], 0, 0)
    ball.m = m
    balls.append(ball)

for i in range(N):
    balls[i].v = vec(-0.6, 0, 0)


springs =[]
for i in range(NN):
    spring = cylinder(pos = vec(i*size*2-0.1, 0, 0),radius = 0.005)
    spring.axis = balls[i].pos - spring.pos
    springs.append(spring)

dt = 0.001
t = 0
while True:
    rate(1000)
    t += dt

    for i in range(NN):
        
        springs[i].axis = balls[i].pos - springs[i].pos
        springForce[i] = -k * (mag(springs[i].axis) -L)*springs[i].axis.norm()
        balls[i].a = vec(0,-g,0) + springForce[i]/m

        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v *dt
    
    for i in range(NN-1):
        if (mag(balls[i].pos - balls[i+1].pos) <= size+size and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0) :
            (balls[i].v, balls[i+1].v) = af_col_v (balls[i].m, balls[i+1].m, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)

 


    
