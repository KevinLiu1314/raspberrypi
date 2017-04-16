import sys
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(sys.argv[1])

try:
    while True:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(1)
except KeyboardInterrupt:
    sys.exit("\nBye!")
