#calculte sqft of a room

print('Enter the diamension of the room in sqft.')
width = int(input('enter width of the room : '))
height = int(input('enter height of the room : '))


def calculate_area(w,h):
    room = w*h
    return room
finalResult = calculate_area(width,height)
print(f"Final sqft of the room is {finalResult}")