from vpython import *

#Items

mercurio = sphere(pos=vector(100,0,0), radius=10, color = color.orange, make_trail = True)
venus = sphere(pos=vector(150,0,0), radius=20, color = color.red, make_trail = True)
terra = sphere(pos=vector(200,0,0), radius=25, color = color.blue, make_trail = True)
sol = sphere(pos=vector(0,0,0), radius=40, color = color.yellow, make_trail = True)


#Condições

r1 = 100          #Raio
t1 = 1            #Tempo
w1 = (2*pi)/t1    #Velocidade Angular

r2= 150           #Raio
t2 = 2            #Tempo
w2 = (2*pi)/t2    #Velocidade Angular

r3= 200           #Raio
t3 = 3            #Tempo
w3 = (2*pi)/t3    #Velocidade Angular

dt = 0.001

#Equações

while True:
    rate(180)
    t1 += dt
    p1 = vector(r1*cos(w1*t1), r1*sin(w1*t1), 0)
    mercurio.pos = p1
    
    t2 += dt
    p2 = vector(r2*cos(w2*t2), r2*sin(w2*t2), 0)
    venus.pos = p2
    
    t3 += dt
    p3 = vector(r3*cos(w3*t3), r3*sin(w3*t3), 0)
    terra.pos = p3
