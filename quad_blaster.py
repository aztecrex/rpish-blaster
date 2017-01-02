from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
from line import plot_line
from draw import Sprite

sense = SenseHat()


x = 3
y = 3
firing = False

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - 1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
       y = clamp(y + 1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)

def pushed_middle(event):
    global firing
    if event.action != ACTION_RELEASED:
      firing = True
       

def refresh():
      draw()

def pos(t, index):
    return (0,0)

def draw():
      global x, y, firing
      if not firing:
          crosshair.put((x, y))
      else:
          for i in range(0, 10):
              for j in range(0,4):
                  bullets[j].put(pos(i,j))

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_any = refresh

crosshair = Sprite([(-1,0),(1,0),(0,-1),(0,1)], 0, 0, 255)
bullets = [Sprite([(0,0)], 255, 0, 0) for i in range(0,4)]

def main():
    sense.clear()
    draw()
    pause()

if __name__ == "__main__": main()


