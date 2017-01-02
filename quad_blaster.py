from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
from line import plot_line
from draw import Sprite
from time import sleep

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

def pos(progress, index):
    cx,cy = corners[index]
    return (cx + progress * (x - cx), cy + progress * (y - cy))

def draw():
      global x, y, firing
      if not firing:
          crosshair.put((x, y))
      else:
          firing = False
          for i in range(0, 6):
              progress = (1 / 6) * i
              for j in [n for n in range(0,4) if corners[n] != (x,y)]:
                  bolts[j].put(pos(progress,j))
              crosshair.put((x, y))
              sleep(.03)
          bolts[0].put((x,y))
          sleep(.1)
          for bolt in bolts:
              bolt.erase()
          crosshair.put((x, y))

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle
sense.stick.direction_any = refresh

crosshair = Sprite([(-1,0),(1,0),(0,-1),(0,1)], 0, 0, 255)
bolts = [Sprite([(0,0)], 255, 0, 0) for i in range(0,4)]
corners = [(0,0),(0,7),(7,0),(7,7)]

def main():
    sense.clear()
    draw()
    pause()

if __name__ == "__main__": main()


