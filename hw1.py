#hw1
# https://youtu.be/672Wa1JVP-A 
from vpython import*
g=9.8
size=0.25
height=15.0
t=0
l=0
displacementX=0
displacementY=0

scene=canvas(width=800,height=800,center=vec(0,height/2,0),background=vec(0.5,0.5,1))
floor=box(length=30,height=0.01,width=10,color=color.blue)
ball=sphere(radius=size,color=color.red,make_trail=True,trail_radius=0.05)
msg=text(text='oblique projection',pos=vec(-10,height/2*2.5,0))
a1=arrow(color=color.yellow,shaftwidth=0.05)


ball.pos=vec(-15,5,0)
ball.v=vec(6,8,0)
a1.pos=vec(-15,5,0)
a1.axis=vec(3,4,0)

dt=0.001
while ball.pos.y>=size:
    rate(1000)

    ball.pos+=ball.v*dt
    a1.pos+=ball.v*dt
    ball.v.y=ball.v.y-g*dt
    a1.axis=ball.v/4

    t+=dt
    l+=sqrt((ball.v.x*dt)**2+(ball.v.y*dt)**2)
    displacementX+=ball.v.x*dt
    displacementY+=ball.v.y*dt
    
#msg.visible=False
#msg=text(text=str(ball.v.y),pos=vec(-10,height/2*2.5,0))
print('displacement X = %.4f (m)' % displacementX)
print('displacement Y = %.4f (m)' % displacementY)
print('The flying time in the air = %.4f (s)' % t)
print('The length of the entire path = %.4f (m)' % l)


