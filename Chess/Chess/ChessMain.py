"""
Main file. Will handle user input and display current GameState object.
"""
import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #dimension of a chess board is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animations later on
IMAGES = {}

"""
Initialise a global dictionary of images. This will be called once in main
"""
def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN','bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('Chess/' + 'images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying "Images['wp']"

"""
The main driver for our code. This will handle user input and updating the graphics
"""

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_images() #only do this once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


# Responsible for all the graphics within a current game state

def draw_game_state(screen, gs):
    draw_board(screen) #draw squares on the board
    draw_pieces(screen, gs.board) #draw pieces on top of those squares
    

def draw_board(screen):
    colours = [p.Color("white"), p.Color("gray")]
    for rows in range(DIMENSION):
        for cols in range(DIMENSION):
            colour = colours[((rows+cols) % 2)]
            p.draw.rect(screen, colour, p.Rect(cols*SQ_SIZE, rows*SQ_SIZE, SQ_SIZE, SQ_SIZE))


#Draws the pieces on the board using the current GameState.board
def draw_pieces(screen, board):
    for rows in range(DIMENSION):
        for cols in range(DIMENSION):
            piece = board[rows][cols]
            if piece != "--": #not an empty square
                screen.blit(IMAGES[piece], p.Rect(cols*SQ_SIZE, rows*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            



if __name__ == "__main__":
    main()