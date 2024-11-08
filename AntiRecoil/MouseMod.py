from pynput.mouse import Button, Controller

mouse = Controller()

count = 0
while (count < 3):     
    count = count + 1
    # Set pointer position
mouse.position = (960, 540)
print('MasterModz has moved mouse to {0}'.format(mouse.position))