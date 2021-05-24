# Pong
# Game where you protect your side of the screen using a paddle to deflect
# a ball towards the other players side. Successfully getting the ball past
# the opposing player's paddle awards you a point, first to 11 points wins
# the game.
# Version 1 of Pong shows the ball moving and wrapping with the edges of the
# screen and no score is kept. The paddles are present but are immovable and
# do not affect the ball's trajectory

from uagame import Window
import pygame, time
from pygame.locals import *

# User-defined functions

def main():

   window = Window('Pong', 600, 500)
   window.set_auto_update(False)
   game = Game(window)
   game.play()
   window.close()
# User-defined classes

class Ball:
   # An object in this class represents a colored circle.

   def __init__(self, surface, center, radius, color, velocity, window):
      # Initialize a Circle.
      # - self is the Circle to initialize
      # - center is a list containing the x and y int
      # coords of the center of the Circle
      # - radius is the int pixel radius of the Circle
      # - color is the pygame.Color of the Circle
      # - window is the uagame window object
      self.surface = surface
      self.center = center
      self.radius = radius
      self.color = color
      self.velocity = velocity
      self.window = window
      pygame.key.set_repeat(20,20)
      
   
   def draw(self):
      # Draw the Circle.
      # - self is the Circle to draw
      
      pygame.draw.circle(self.window.get_surface(), self.color, self.center, self.radius)
   
   def move(self):
      # Move the circle.
      # - self is the Circle to move
      
      screen_size = self.surface.get_size()
      for index in range(0, 2):
         self.center[index] += self.velocity[index]
         if (self.center[index] >= screen_size[index] - self.radius or self.center[index] <= self.radius):
            self.velocity[index] = -self.velocity[index]
         #if pygame.Rect.collidepoint(self.center):
          
class Paddle:
   
   def __init__(self, rect, color, width, window):
   # Initialize a Paddle.
   # - self is the Paddle to initialize
   # - rect is a pygame.Rect object
   # height int values of the Paddle
   # - color is the pygame.Color of the Paddle
   # - window is the uagame window object
      
      self.rect = rect
      self.color = color
      self.window = window
      self.width = width

    
   def draw(self):
   # Draw the Paddle
   # - self is the Paddle to draw
      #self.left_rect = pygame.Rect(75, 225, 10, 50)
      #self.right_rect = pygame.Rect(515, 225, 10, 50)           
      pygame.draw.rect(self.window.get_surface(), self.color, self.rect, self.width)
      
   def move(self):
      self.rect.move(paddle_x, paddle_y)
      
      
class Game:
   # An object in this class represents a complete game.

   def __init__(self, window):
      # Initialize a Game.
      # - self is the Game to initialize
      # - window is the uagame window object
      
      self.window = window
      self.bg_color = pygame.Color('black')
      self.fg_color_str = pygame.Color('white')
      self.window.set_font_size(72)
      self.pause_time = 0.003 # smaller is faster game
      self.close_clicked = False
      self.continue_game = True
      self.velocity = [2, 1]
      self.circle = Ball(window.get_surface(), [300, 250], 6, self.fg_color_str, self.velocity, window)
      self.left_y = 225
      self.left_rect = pygame.Rect((75, self.left_y), (10, 50))
      self.right_y = 225
      self.right_rect = pygame.Rect((515, self.right_y), (10, 50))
      self.left_paddle = Paddle(self.left_rect, self.fg_color_str, 0, window)
      self.right_paddle = Paddle(self.right_rect, self.fg_color_str, 0, window)
      self.left_score = 0
      self.right_score = 0
      #self.rect_color = (255,255,255)
    
    #self.left_paddle = pygame.Rect(75,225,10,50)
      #self.right_paddle = pygame.Rect(515,225,10,50)
         

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_event()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
         time.sleep(self.pause_time) # set game velocity by pausing

   def handle_event(self):
      # Handle each user event by changing the game state
      # appropriately.
      # - self is the Game whose events will be handled
      
      screen_height = self.window.get_height()
      event = pygame.event.poll()
      paddle_movement = 4     
      max_bottom = screen_height - 50
      if event.type == KEYDOWN:
         list_of_keys = pygame.key.get_pressed()
         if list_of_keys[K_q] == True:
            self.left_rect.move_ip(0, -paddle_movement)
            if self.left_rect.top < 0:
               self.left_rect.top = 0
         if list_of_keys[K_a] == True:  
            self.left_rect.move_ip(0, paddle_movement)
            if self.left_rect.top > max_bottom:
               self.left_rect.top = max_bottom            
         if list_of_keys[K_p] == True:
            self.right_rect.move_ip(0, -paddle_movement)
            if self.right_rect.top < 0:
               self.right_rect.top = 0            
         if list_of_keys[K_l] == True:
            self.right_rect.move_ip(0, paddle_movement) 
            if self.right_rect.top > max_bottom:
               self.right_rect.top = max_bottom                 
         
      
      if event.type == QUIT:
         self.close_clicked = True

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw

      self.window.clear()
      self.circle.draw()
      self.left_paddle.draw()
      self.right_paddle.draw()
      x_coord = self.window.get_width() - self.window.get_string_width(str(self.right_score))
      self.window.draw_string(str(self.left_score), 0, 0)
      self.window.draw_string(str(self.right_score), x_coord, 0)
      self.window.update()
      
   def update(self):
      # Update the game objects.
      # - self is the Game to update
      screen_width = self.window.get_width()
      self.circle.move()
      if self.circle.center[0] >= screen_width - self.circle.radius:
         self.left_score +=1
      if self.circle.center[0] <= self.circle.radius:
         self.right_score +=1   
      if self.circle.velocity <= [0, 0]:
         left_coll = self.left_rect.collidepoint(self.circle.center)
         if left_coll == True:
            self.circle.velocity[0] = -self.circle.velocity[0]
      if self.circle.velocity >= [0, 0]:
         right_coll = self.right_rect.collidepoint(self.circle.center)
         if right_coll == True:
            self.circle.velocity[0] = -self.circle.velocity[0]      
      #self.left_rect = pygame.Rect(75, 225, 10, 50)
      #self.right_rect = pygame.Rect(515, 225, 10, 50)      
      
      self.left_paddle.draw()
      
         
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      
      if self.left_score == 11:
         self.continue_game = False
      if self.right_score == 11:
         self.continue_game = False
   
main()



