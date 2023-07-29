#hw2_must
#https://youtu.be/6GmMHXGEjGY 

from vpython import*
#initial condiction
g=9.8
size=0.25
height=15.0
theta=pi/4
C_drag=0.9
i=0
n=0
highestPoint = 0
t=0
displacementX=0
displacementY=0

scene1=canvas(center=vec(0,5,0),width=600,align = 'left',background=vec(0.5,0.5,1))
oscillation = graph(width = 450, align = 'right')
floor=box(length=30,height=0.01,width=4,color=color.blue)
ball=sphere(radius=size,color=color.red,make_trail=True,trail_radius=size/3)
msg=text(text='bouncing ball',pos=vec(-10,height,0))

ball.pos=vec(-15,size,0)
ball.v=vec(20*cos(theta),20*sin(theta),0)

#plot function
funct = gcurve(graph = oscillation, color = color.blue, width = 4)

dt=0.001
while i < 3:
    rate(1000)
    ball.v += vec(0,-g, 0)*dt - C_drag * ball.v*dt
    ball.pos += ball.v*dt
    t+=dt
    
    if ball.v.y < 0 and n < 1:
        highestPoint = ball.pos.y
        n=n+1
    
    if ball.pos.y <= size and ball.v.y < 0:
        ball.v.y = -ball.v.y
        i=i+1
      
    
    funct.plot(pos=(t,ball.v.mag))
    
    displacementX+=ball.v.x*dt
    displacementY+=ball.v.y*dt

print('displacement X = %.4f (m)' % displacementX)
print('displacement Y = %.4f (m)' % displacementY)
print('The flying time in the air = %.4f (s)' % t)
print('heighest point = %.4f (m)' % highestPoint)



