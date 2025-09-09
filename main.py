
import pygame



pygame.init()
size = 1000,800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe game")
WHITE =(255, 255, 255 )
BLACK = (0, 0, 0)

def grid(screen):

    pygame.draw.line(screen, WHITE, (200, 100), (800, 100))
    pygame.draw.line(screen, WHITE, (200, 700), (800, 700))
    pygame.draw.line(screen, WHITE, (200, 100), (200, 700))
    pygame.draw.line(screen, WHITE, (800, 100), (800, 700))


    pygame.draw.line(screen, WHITE, (200, 300), (800, 300))
    pygame.draw.line(screen, WHITE, (200, 500), (800, 500))

    pygame.draw.line(screen, WHITE, (400, 100), (400, 700))
    pygame.draw.line(screen, WHITE, (600, 100), (600, 700))



def main():
    
    clock = pygame.time.Clock()
    running = True

    while running:


        screen.fill(BLACK)
        grid(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(30)
if __name__ == "__main__":
    main()
