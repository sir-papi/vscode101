import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arabic Language Learning Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up fonts
FONT = pygame.font.Font(None, 36)
BUTTON_FONT = pygame.font.Font(None, 28)

# Define the question bank
questions = [
    {"arabic": "كتاب", "english": "Book"},
    {"arabic": "قلم", "english": "Pen"},
    {"arabic": "ماء", "english": "Water"},
    {"arabic": "شجرة", "english": "Tree"},
    {"arabic": "بيت", "english": "House"}
]

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Function to display a question
def display_question(question, options):
    window.fill(WHITE)
    draw_text(f"Translate: {question['arabic']}", FONT, BLACK, window, 50, 50)
    y_offset = 150
    for i, option in enumerate(options):
        pygame.draw.rect(window, BLUE, (50, y_offset + i * 60, 700, 50))
        draw_text(option, BUTTON_FONT, WHITE, window, 60, y_offset + i * 60)
    pygame.display.update()

# Main game loop
def main():
    pygame.mixer.music.load('background_music.mp3')  # Add your background music file
    pygame.mixer.music.play(-1, 0.0)  # Loop the music indefinitely
    score = 0
    question_index = 0
    random.shuffle(questions)
    clock = pygame.time.Clock()
    while question_index < len(questions):
        question = questions[question_index]
        correct_answer = question['english']
        options = [correct_answer]
        while len(options) < 4:
            option = random.choice(questions)['english']
            if option not in options:
                options.append(option)
        random.shuffle(options)
        display_question(question, options)
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    for i, option in enumerate(options):
                        if 50 < mouse_x < 750 and 150 + i * 60 < mouse_y < 200 + i * 60:
                            if option == correct_answer:
                                score += 1
                            question_index += 1
                            waiting_for_input = False
                            break
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()