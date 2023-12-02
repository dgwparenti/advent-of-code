# read in file
with open('directions.txt') as f:
    directions = f.read()

# in a for loop
floor = 0
for i, direction in enumerate(directions):
    if floor >-1:
        if direction == '(':
                floor=floor+1
        else:
            floor=floor-1
    else:
         print('<0',i,floor)
         break