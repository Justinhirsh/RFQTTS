import pygame, os, pyttsx3, random, linecache

pygame.init()
background_colour = (255, 255, 255)
running = False
BLACK = 0,0,0
SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption('RFQTTS')
SCREEN.fill(background_colour)
font = pygame.font.Font('OpenSans-Bold.ttf', 32)
pygame.display.flip()
start = False
def make_quote():
   text_draw = font.render(line, True, BLACK)
   SCREEN.blit(text_draw, (0, 250))
def tts(text):
    pyobj = pyttsx3.init()
    pyobj.say(text, "slow")
    pyobj.runAndWait()
def clear():
    os.system('cls')
def make_text(text,location1,location2,color):
    text_draw = font.render(text, True, color)
    SCREEN.blit(text_draw, (location1, location2))
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
while True:
    make_text("Welcome to RFQTTS", 125, 0, BLACK)
    make_text("press space to generate a quote", 50, 150, BLACK)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if running == False:
                    running = True
                    with open('quotes.txt','r', encoding= 'UTF-8') as file:
                        for line_number, line in enumerate(file):
                            pass
                    line_chosen = random.randint(1, line_number + 1)
                    line = linecache.getline(r"quotes.txt", line_chosen)
                    clear()
                    blit_text(SCREEN, line, (0, 250 ), font)
                    
                    pygame.display.update()
            if running == True:
                tts(line)
        if event.type == pygame.QUIT:
            pygame.quit()
        

