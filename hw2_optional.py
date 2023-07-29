#hw2_optional

from vpython import*
#initial condiction
g=9.8
size=0.25
C_drag=0.3
t=0
displacementY=0

scene1=canvas(center=vec(0,500,0),height=1000,width=600,align = 'left',background=vec(0.5,0.5,1))
oscillation = graph(width = 450, align = 'right')
floor=box(length=30,height=0.01,width=4,color=color.blue)
ball=sphere(radius=size,color=color.red,make_trail=True,trail_radius=size)


ball.pos=vec(0,1000,0)
ball.v=vec(0,0,0)

#plot function
funct = gcurve(graph = oscillation, color = color.blue, width = 4)

dt=0.001
while ball.pos.y > size:
    rate(10000)
    ball.v += vec(0,-g, 0)*dt - C_drag * ball.v*dt
    ball.pos += ball.v*dt
    t+=dt
      
    funct.plot(pos=(t,ball.v.mag))
    displacementY+=ball.v.y*dt

print('Final velocity = %.4f (m/s)' % ball.v.mag)
print('displacement Y = %.4f (m)' % displacementY)
print('The flying time in the air = %.4f (s)' % t)



