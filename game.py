import turtle,random
h = int(input("how many player ? "))
speed = [1,3,5,9,7,2,4,6,8]
run = [10,12,13,41,50,16,50,20,30]
player = [] 
c=0
while h>=1:
    a = input('enter youe name and color (with space): ')
    player.append(a)
    h-=1
    c+=1
h+=c
color = []
name = []
while h>=1:
    co = str(player[h-1])
    f = co.find(" ")
    if f!=-1:
        pl = co[:f]
        co = co[f+1:]
        name.append(pl)
        color.append(co)
        h-=1
    else:
        print("you dont write a space .......!!")
        break
h+=c
tu = []
m = -300
for i in range(0,h):
    t = turtle.Turtle("turtle")
    tu.append(t)
for b in range(0,h):
    tu[b].color(color[b])
    tu[b].penup()
    tu[b].goto(0,0)
    tu[b].goto(-300,m)
    tu[b].pendown()
    m+=50
u = turtle.Turtle("classic")
u.penup()
u.goto(400,400)
u.right(90)
u.pendown()
u.speed(2)
u.forward(800)
p = 'n'
for o in range(0,30000):
    for w in range(0,h):
        g=random.choice(speed)
        y = random.choice(run)
        tu[w].speed(g)
        tu[w].forward(y)
        z = tu[w].pos()
        if z[0] >= 400:
            p = 'm'
            break
        else:
            continue
    if p == 'm':
        break
    else:
        continue

turtle.done()