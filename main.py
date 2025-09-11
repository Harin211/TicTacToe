
import pygame



pygame.init()
size = 1000,800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe game")
WHITE =(255, 255, 255 )
BLACK = (0, 0, 0)
squares = [[ 0 for i in range(3)] for i in range(3)]

def grid(screen):
    # horizontally from 200 to 800
    # height from 100 to 700
    pygame.draw.line(screen, WHITE, (200, 100), (800, 100))
    pygame.draw.line(screen, WHITE, (200, 700), (800, 700))
    pygame.draw.line(screen, WHITE, (200, 100), (200, 700))
    pygame.draw.line(screen, WHITE, (800, 100), (800, 700))


    pygame.draw.line(screen, WHITE, (200, 300), (800, 300))
    pygame.draw.line(screen, WHITE, (200, 500), (800, 500))

    pygame.draw.line(screen, WHITE, (400, 100), (400, 700))
    pygame.draw.line(screen, WHITE, (600, 100), (600, 700))

def find_square(coords):

    print(coords)
    mouse_x_coord  =coords [0]
    mouse_y_coord  = coords [1]
    
    if (mouse_x_coord > 200 and mouse_x_coord < 400):
        if (mouse_y_coord > 100 and mouse_y_coord < 300):
            return (0, 0)
        elif (mouse_y_coord > 300 and mouse_y_coord < 500):
            return (1,0)
        elif (mouse_y_coord > 500 and mouse_y_coord < 700):
            return (2,0)
    elif (mouse_x_coord > 400 and mouse_x_coord < 600):
        if (mouse_y_coord > 100 and mouse_y_coord < 300):
            return (0, 1)
        elif (mouse_y_coord > 300 and mouse_y_coord < 500):
            return (1,1)
        elif (mouse_y_coord > 500 and mouse_y_coord < 700):
            return (2,1)
    elif (mouse_x_coord > 600 and mouse_x_coord < 800):
        if (mouse_y_coord > 100 and mouse_y_coord < 300):
            return (0,2)
        elif (mouse_y_coord > 300 and mouse_y_coord < 500):
            return (1,2)
        elif (mouse_y_coord > 500 and mouse_y_coord < 700):
            return (2,2)
    
    return (-1,-1)

def draw_x(coords, surface):


    if (coords == (0,0)):
        pygame.draw.line(surface, WHITE, (210, 110), (390, 290), 2)
        pygame.draw.line(surface, WHITE, (390, 110), (210, 290), 2)
        pygame.display.flip()

    elif(coords == (1,0)):
        pygame.draw.line(surface, WHITE, (210, 310), (390, 490), 2)
        pygame.draw.line(surface, WHITE, (390, 310), (210, 490), 2)
        pygame.display.flip()

    elif(coords == (2,0)):
        pygame.draw.line(surface, WHITE, (210, 510), (390, 690), 2)
        pygame.draw.line(surface, WHITE, (390, 510), (210, 690), 2)
        pygame.display.flip()

    elif (coords == (0,1)):
        pygame.draw.line(surface, WHITE, (410, 110), (590, 290), 2)
        pygame.draw.line(surface, WHITE, (590, 110), (410, 290), 2)
        pygame.display.flip()
    elif (coords == (1,1)):
        pygame.draw.line(surface, WHITE, (410, 310), (590, 490), 2)
        pygame.draw.line(surface, WHITE, (590, 310), (410, 490), 2)
        pygame.display.flip()
    elif (coords == (2,1)):
        pygame.draw.line(surface, WHITE, (410, 510), (590, 690), 2)
        pygame.draw.line(surface, WHITE, (590, 510), (410, 690), 2)
        pygame.display.flip()
    elif (coords == (0,2)):
        pygame.draw.line(surface, WHITE, (610, 110), (790, 290), 2)
        pygame.draw.line(surface, WHITE, (610, 290), (790, 110), 2)
        pygame.display.flip()
    elif (coords == (1,2)):
        pygame.draw.line(surface, WHITE, (610, 310), (790, 490), 2)
        pygame.draw.line(surface, WHITE, (610, 490), (790, 310), 2)
        pygame.display.flip()
    elif (coords == (2,2)):
        pygame.draw.line(surface, WHITE, (610, 510), (790, 690), 2)
        pygame.draw.line(surface, WHITE, (610, 690), (790, 510), 2)
        pygame.display.flip()

def draw_o(coords, surface):

    if (coords == (0, 0)):
        pygame.draw.circle(surface, WHITE, (300,200), 80, 2)
        pygame.display.flip()
    elif (coords == (1, 0)):
        pygame.draw.circle(surface, WHITE, (300, 400), 80, 2)
        pygame.display.flip()
    elif (coords == (2,0)):
        pygame.draw.circle(surface, WHITE, (300, 600), 80, 2)
        pygame.display.flip()
    elif (coords == (0,1)):
        pygame.draw.circle(surface, WHITE, (500, 200), 80, 2)
        pygame.display.flip()
    elif (coords == (1, 1)):
        pygame.draw.circle(surface, WHITE, (500, 400), 80, 2)
        pygame.display.flip()
    elif (coords == (2,1)):
        pygame.draw.circle(surface, WHITE, (500, 600), 80, 2)
        pygame.display.flip()
    elif (coords == (0,2)):
        pygame.draw.circle(surface, WHITE, (700, 200), 80, 2)
        pygame.display.flip()
    elif (coords == (1, 2)):
        pygame.draw.circle(surface, WHITE, (700, 400), 80, 2)
        pygame.display.flip()
    elif (coords == (2,2)):
        pygame.draw.circle(surface, WHITE, (700, 600), 80, 2)
        pygame.display.flip()

def square_is_empty(squares, coords):

    xcoord = coords[0]
    ycoord = coords[1]

    if (squares[xcoord][ycoord] == 0):
        return True

    return False

def draw_in_square(squares, curr_square, counter):

    if (square_is_empty(squares, curr_square)):
        if (counter % 2 == 0):
            draw_x(curr_square, screen)
            squares[curr_square[0]][curr_square[1]] = 2
        else:
            draw_o(curr_square, screen)
            squares[curr_square[0]][curr_square[1]] = 7
        counter += 1
    return counter

def check_win_sums(squares):
    new_list = []

    for i in range(3):
        sum_row = 0
        sum_col = 0
        for j in range(3):
            sum_row += squares[i][j]
            sum_col += squares[j][i]
        new_list.append(sum_row)
        new_list.append(sum_col)

    diagnonal_sum1 = 0
    diagnonal_sum2 = 0
    for i in range(3):
        for j in range(3):

            if (i == j):
                diagnonal_sum1 += squares[i][j]
            if (j == (2 - i)):
                diagnonal_sum2 += squares[i][j]


    new_list.append(diagnonal_sum1)
    new_list.append(diagnonal_sum2)
        
    return new_list

def game_over(squares, win_sums):

    print(win_sums)


    if (21 in (win_sums) or 6 in (win_sums)):
        return True

    for i in range(3):
        for j in range(3):
            coords = (i,j)
            if (square_is_empty(squares, coords) == True): return False # game not over return false

    return True

def main():
    clock = pygame.time.Clock()
    running = True

    counter = 0

    while running:


        # screen.fill(BLACK)
        grid(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos  = pygame.mouse.get_pos()
                curr_square  = find_square(pos)
                counter = draw_in_square(squares, curr_square, counter)
        
            # print(check_win_sums(squares))

        if (game_over(squares, check_win_sums(squares))):
            print("game over")
            break

        clock.tick(30)

if __name__ == "__main__":
    main()
