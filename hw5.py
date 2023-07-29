#hw5

from vpython import*
G=6.673E-11
mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10} #10 times larger for better view
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi/180.0

def G_force(m1,m2,pos1,pos2):
    return -G*m1*m2/mag2(pos1-pos2)*norm(pos1-pos2)
class as_obj(sphere):
    def kinetic_energy(self):
        return 0.5 * self.m * mag2(self.v)
    def potential_energy(self):
        return - G * mass['earth'] * self.m / mag(self.pos)
    

scene = canvas(width=800, height=800, background=vector(0.2,0.5,0.8))
#scene.forward = vector(0, -1, 0)
scene.lights = []
sun = sphere(pos=vector(0,0,0), radius =radius['sun'], color = color.orange, emissive=True,m = mass['sun'])
sun.v = vector (0,0,0)
sun.visible=True
local_light(pos=vector(0,0,0))

earth = as_obj(pos = vector(earth_orbit['r'],0,0), radius =radius['earth'] , m = mass['earth'], texture={'file':textures.earth}, make_trail = True)
earth.v = vector(0, 0, - earth_orbit['v'])
moon = as_obj(pos = vector(moon_orbit['r']*cos(theta)+earth_orbit['r'],moon_orbit['r']*sin(theta),0), radius =radius['moon'], m = mass['moon'], make_trail = False)
moon.v = vector(0, 0, - moon_orbit['v']- earth_orbit['v'])

a1=arrow(shaftwidth=0.8)
a1.pos=earth.pos


#pos_CM=earth.pos*earth.m + moon.pos*moon.m == vector(0,0,0)
#earth.v*earth.m + moon.v*moon.m == vector(0,0,0)

scene.center = earth.pos
v_CM=(earth.v*earth.m+moon.v*moon.m)/(earth.m+moon.m)
earth.v+=-v_CM
moon.v+=-v_CM
sun.v+=-v_CM

n = 0
last_times = 0
now_times = 0
direction_aux_switch = -1
a = 1

dt=60*60*6
while True:
    rate(1000)
    n += 1
    earth_force = G_force ( earth.m , moon.m , earth.pos , moon.pos ) + G_force(earth.m,sun.m,earth.pos,sun.pos)
    moon_force = G_force ( moon.m , earth.m , moon.pos , earth.pos ) + G_force(moon.m,sun.m,moon.pos,sun.pos)
    sun_force = G_force ( sun.m , moon.m , sun.pos , moon.pos ) + G_force(sun.m,earth.m,sun.pos,earth.pos)

    moon.a = moon_force/moon.m
    moon.v = moon.v + moon.a * dt
    moon.pos = moon.pos + moon.v * dt

    earth.a = earth_force/earth.m
    earth.v = earth.v + earth.a * dt
    earth.pos = earth.pos + earth.v * dt
    
    a1.pos = earth.pos
    a1.axis = norm(vec((moon.pos.y-earth.pos.y)*(moon.v.z-earth.v.z)-(moon.pos.z-earth.pos.z)*(moon.v.y-earth.v.y), (moon.pos.z-earth.pos.z)*(moon.v.x-earth.v.x)-(moon.pos.x-earth.pos.x)*(moon.v.z-earth.v.z), (moon.pos.x-earth.pos.x)*(moon.v.y-earth.v.y)-(moon.pos.y-earth.pos.y)*(moon.v.x-earth.v.x)))*10**8*1.5
    scene.center= earth.pos

    sun.a=sun_force/sun.m
    sun.v=sun.v+sun.a*dt
    sun.pos=sun.pos+sun.v*dt

     
    if ((moon.pos.y-earth.pos.y)*(moon.v.z-earth.v.z)-(moon.pos.z-earth.pos.z)*(moon.v.y-earth.v.y))*direction_aux_switch > 0:
        direction_aux_switch = direction_aux_switch *(-1)
        last_times = now_times
        now_times = n
    if last_times > 0 and a>0 :
        a = a-1
        print ("The period", now_times-last_times)
        


    #sun.a = (G_force_se(sun.m, sun.pos)+G_force_se(sun.m, sun.pos)) / sun.m
    #sun.v = sun.v + sun.a * dt
    #sun.pos = sun.pos + sun.v * dt
    

