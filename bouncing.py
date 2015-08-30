import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rect_x = 50
rect_y = 50
rectW = 50
rectH = 50
velocity = [5,5]
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
	
    #check for collision
    if rect_x <= 0 or rect_x >=  size[0] - rectW :
        velocity[0] = -velocity[0]
	
    if rect_y <= 0 or rect_y >=  size[1] - rectH :
        velocity[1] = -velocity[1]
		
	#iterate movement
    rect_x += velocity[0]
    rect_y += velocity[1]
    
    pygame.draw.rect(screen, BLACK, [rect_x, rect_y, rectW, rectH] )
		
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()