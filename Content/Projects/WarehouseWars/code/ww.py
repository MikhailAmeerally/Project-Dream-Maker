import pygame

class Actor:

	def __init__(self, icon_file, stage, x, y, delay=5):
		self._icon=pygame.image.load(icon_file) # the image image to display of self
		self.set_position(x, y) # self's location on the stage
		self._stage=stage # the stage that self is on

		# the following can be used to change this Actors 'speed' relative to other
		# actors speed. See the delay method.
		self._delay=delay  
		self._delay_count=0
	
	def set_position(self, x, y):
		(self._x, self._y) = (x, y)

	def get_position(self):
		return (self._x, self._y)

	def get_icon(self):
		return self._icon

	def is_dead(self):
		''' Return whether self is dead. '''
		return False

	def move(self, other, dx, dy):
		''' other is telling us to move in direction (dx, dy), in this case, we just move.
		(dx,dy) is in {(1,1), (1,0), (1,-1), (0,1), (0,0), (0,-1), (-1,1), (-1,0), (-1,-1)} '''
	
		''' In the more general case, in subclasses, self will determine 
		if they will listen to other, and if so, will try to move in
		the specified direction. If the target space is occupied, then we 
		may have to ask the occupier to move. '''

		self.set_position(self._x+dx, self._y+dy)
		return True

	def delay(self):
		''' Used to change self's speed relative to other Actors. 
		Each time we get a chance to take a step, we delay. If our count wraps around to 0
		then we actually do something. Otherwise, we simply return from the step method.
		'''

		self._delay_count=(self._delay_count+1)% self._delay
		return self._delay_count==0

	def step(self):
		''' self takes a single step in the animation of the game.
		self can ask the stage to help as well as ask other Actors
		to help us get our job done. '''

		pass

class Player(Actor):
	''' A Player is an Actor that can handle events. These typically come
	from the user, for example key presses etc. '''

	def __init__(self, icon_file, stage, x=0, y=0):
		Actor.__init__(self, icon_file, stage, x, y)
	
	def handle_event(self, event):
		''' Used to register the occurrence of an event with self. '''
		pass

class KeyboardPlayer(Player):
	''' A KeyboardPlayer is a Player that can handle keypress events '''
	def __init__(self, icon_file, stage, x=0, y=0):
		Player.__init__(self, icon_file, stage, x, y)
		self._last_event=None # we are only interested in the last event
	
	def handle_event(self, event):
		''' Record the last event directed at this KeyboardPlayer, self
		ignores all previous events since self last took a step.  '''

		self._last_event=event

	def step(self):
		''' Take a single step in the animation. 
		For example: if the user asked us to move right, then we do that. '''

		if self._last_event is not None:
			dx, dy=None, None
			if self._last_event==pygame.K_m:
				dx, dy=0,1
			if self._last_event==pygame.K_j:
				dx, dy=-1,0
			if self._last_event==pygame.K_k:
				dx, dy=1,0
			if self._last_event==pygame.K_i:
				dx, dy=0,-1
			if dx is not None and dy is not None:
				self.move(self, dx, dy) # we are asking ourself to move

			self._last_event=None

	def move(self, other, dx, dy):
		''' other asked self to move. In this case, move if possible, return whether I moved.
		if there is a space available go to it, otherwise, we may need to ask a neighbour 
		to move to get our work done. '''


		# Where we are supposed to move. 
		new_x=self._x+dx
		new_y=self._y+dy
		

		''' Check if (new_x, new_y) is on the stage.
		If it is, then determine if another Actor is occupying that spot. If so,
		self asks them to move. If they moved, then we can occupy the spot. Otherwise
		we can't move. We return True if we moved and False otherwise. '''
		# FIX THIS !!

		# LAB QUESTION 2 (Hint: Check the Monster.move method, they do something similar).
		# LAB QUESTION 3 (Hint: self._stage.get_actor(new_x, new_y))
		# LAB QUESTION 4

		Actor.move(self, other, dx, dy)
		return True
		
class Box(Actor):
	def __init__(self, icon_file, stage, x=0, y=0):
		Actor.__init__(self, icon_file, stage, x, y)

	def move(self, other, dx, dy):
		''' other asked me to move self. I do it if possible, return whether I moved '''
		new_x=self._x+dx
		new_y=self._y+dy

		''' If (new_x, new_y) is on the stage, and is empty, then 
		we simply move there. Otherwise, we ask whomever is at (new_x, new_y)
		to move, also the same direction. If they moved, the space is now
		empty, so we now move into (new_x, new_y). If we successfully
		moved, then we return True, otherwise, we return False. '''

		# FIX THIS
		# LAB QUESTION 5

		return False

class Wall: # LAB QUESTION 6
	pass

class Monster(Actor):
	def __init__(self, icon_file, stage, x=0, y=0, delay=5):
		Actor.__init__(self, icon_file, stage, x, y, delay)
		self._dx=1
		self._dy=1
	
	def is_dead(self):
		''' Return whether self has died. That is, if self is surrounded on all sides, 
		by either Boxes or other Monsters. '''

		# FIX THIS
		return False

	def step(self):

		if not self.delay(): return 
		self.move(self, self._dx, self._dy)
		return True

	def move(self, other, dx, dy):
		''' other asked self to move if possible, return whether I moved '''

		if other!=self: # Noone pushes me around
			return False

		bounce_off_edge=False

		new_x=self._x+self._dx
		new_y=self._y+self._dy

		if not self._stage.is_in_bounds_x(new_x): 
			self._dx=-self._dx
			bounce_off_edge=True
			
		if not self._stage.is_in_bounds_y(new_y):
			self._dy=-self._dy
			bounce_off_edge=True

		if bounce_off_edge: 
			return False

		# LAB QUESTION 7
		# MONSTERS SHOULD BOUNCE BACK FROM BOXES AND OTHER MONSTERS
		# HINT: actor=self._stage.get_actor(new_x,new_y)
		
		return Actor.move(self, other, dx, dy)
	
class Stage:
	def __init__(self, width, height, icon_dimension):

		self._actors=[] # all actors on this stage (monsters, player, boxes, ...)
		self._player=None # a special actor, the player

		# the logical width and height of the stage
		self._width, self._height = width, height

		self._icon_dimension=icon_dimension # the pixel dimension of all actors
		# the pixel dimensions of the whole stage
		self._pixel_width = self._icon_dimension * self._width
		self._pixel_height = self._icon_dimension * self._height
		self._pixel_size = self._pixel_width, self._pixel_height

		# get a screen of the appropriate dimension to draw on
		self._screen = pygame.display.set_mode(self._pixel_size)

	def is_in_bounds(self, x,y):
		return self.is_in_bounds_x(x) and self.is_in_bounds_y(y)

	def is_in_bounds_x(self, x):
		return 0<=x and x<self._width

	def is_in_bounds_y(self, y):
		return 0<=y and y<self._height

	def get_width(self): 
		return self._width

	def get_height(self): 
		return self._height

	def set_player(self, player):
		''' A Player is a special actor,
		self may need to contact them directly '''
		self._player=player
		self.add_actor(self._player)

	def remove_player(self):
		self.remove_actor(self._player)
		self._player=None

	def player_event(self, event):
		''' Send a user event to the player (this is a special Actor). '''
		self._player.handle_event(event)

	def add_actor(self, actor):
		self._actors.append(actor)

	def remove_actor(self, actor):
		self._actors.remove(actor)

	def step(self):
		''' Take one step in the animation of the game. 
		Do this by asking each of the actors to take a single step. '''

		for a in self._actors:
			a.step()

	def get_actors(self):
		return self._actors

	def get_actor(self, x, y):
		''' return the first actor at coordinates (x,y) 
		return None if there is no such actor
		'''
		for a in self._actors:
			if a.get_position()==(x,y):
				return a
		return None

	def draw(self):
		''' draw all Actors on self to the screen '''
		self._screen.fill((0,0,0)) # (0,0,0)=(r,g,b)=black
		for a in self._actors:
			icon=a.get_icon()
			(x,y)=a.get_position()
			d=self._icon_dimension
			rect=pygame.Rect(x*d, y*d, d, d)
			self._screen.blit(icon, rect)
		pygame.display.flip()

