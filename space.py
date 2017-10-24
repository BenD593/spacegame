#imports#
from PIL import Image
import tkinter
#images#
#Read image
im = Image.open( '1.png' )
#Display image
im.show()
#creat windows#
right = tkinter.Tk()
left = tkinter.Tk()
thurst = tkinter.Tk()
air = tkinter.Tk()
live = tkinter.Tk()
#left#
a = tkinter.Label(left ,text="Atlantis Left Panel")
b = tkinter.Button(left ,text="Alpha Air Lock")
c = tkinter.Button(left ,text="Bravo Air Lock")
#right#
a1 = tkinter.Label(right ,text="Atlantis Right Panel")
b1 = tkinter.Label(right ,text="Altitude:65ft")
c1 = tkinter.Label(right ,text="Bearing:0")
l1 = tkinter.Label(right ,text="Pitch:0")
m1 = tkinter.Label(right ,text="Yaw:0")
n1 = tkinter.Label(right ,text="Roll:0")
d1 = tkinter.Label(right ,text="          ")
e1 = tkinter.Label(right ,text="Coms")
f1 = tkinter.Label(right ,text="Status:Connected")
g1 = tkinter.Label(right ,text="Channel:76")
h1 = tkinter.Label(right ,text="Volume:50%")
i1 = tkinter.Button(right ,text="Press to speak")
j1 = tkinter.Button(right ,text="Change Channel")
k1 = tkinter.Button(right ,text="Mute")
#Thurst#
a2 = tkinter.Label(thurst ,text="Thurst")
b2 = tkinter.Label(thurst ,text="Thrust:0%")
c2 = tkinter.Button(thurst  ,text="Thurst up 10%")
d2 = tkinter.Button(thurst  ,text="Thurst down 10%")
e2 = tkinter.Button(thurst  ,text="Thurst off(0%)")
f2 = tkinter.Button(thurst  ,text="Thurst on(100%)")
#air#
a3 = tkinter.Label(air ,text="Oxygen")
b3 = tkinter.Label(air ,text="Oxygen left:100%")
c3 = tkinter.Label(air ,text="Oxygen in air:100%")
d3 = tkinter.Button(air ,text="Switch To Backup Oxygen")
e3 = tkinter.Button(air ,text="Enable Emergancy Oxygen masks")
#live#
a4 = tkinter.Label(live ,text="Live info")
b4 = tkinter.Label(live ,text="No info")
#left pack#
a.pack()
b.pack()
c.pack()
#right pack#
a1.pack()
b1.pack()
c1.pack()
l1.pack()
m1.pack()
n1.pack()
d1.pack()
e1.pack()
f1.pack()
g1.pack()
h1.pack()
i1.pack()
j1.pack()
k1.pack()
#Thurst pack#
a2.pack()
b2.pack()
c2.pack()
d2.pack()
e2.pack()
f2.pack()
#air pack#
a3.pack()
b3.pack()
c3.pack()
d3.pack()
e3.pack()
#live#
a4.pack()
b4.pack()
#start windows#
right.mainloop
left.mainloop
thurst.mainloop
air.mainloop
live.mainloop
