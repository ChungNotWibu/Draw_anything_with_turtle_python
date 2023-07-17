import turtle as pen


# ==========

size = float(
    input("Enter polygon side length plz: ")
)

side = float(
    input("Enter the number of sides plz: ")
)

color = input("Enter the color u want plz: ")

# ==========

pen.fillcolor(color)
pen.begin()

for i in range(side):
    pen.forwad(size)
    pen.right(360/side)

pen.end_fill()   
