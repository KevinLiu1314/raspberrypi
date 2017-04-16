import sys
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(sys.argv[1])

try:
    while True:
        pygame.mixer.music.play()
        #pygame.event.wait()  # CTRL-C won't work
        while pygame.mixer.music.get_busy(): 
            #pygame.time.Clock().tick(1)
            pass
except KeyboardInterrupt:
    sys.exit("\nBye!")
