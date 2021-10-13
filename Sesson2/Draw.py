from turtle import *
speed(-1)
so_canh = int(input("Enter number of edges: "))
for i in range(so_canh):
    forward(100)
    left(360/int(so_canh))
mainloop()