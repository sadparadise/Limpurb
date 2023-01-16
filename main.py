import sys, pygame, random

pygame.init()

run = True
alive = True

size = width, height = 600, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Limpurb Remastered")

bg_color = [0, 0, 0]

player_size = 30
player_pos = [int((width - player_size)/2), int((height - player_size)/2)]
player_color = [0, 0, 255]
player_speed = 0.1

trash_size = 10
trash_pos = []
trash_color = [100, 100, 100]
for i in range(50):
    x = 0
    y = 0
    while x < 80 and y < 80:
        x = random.randint(0, width)
        y = random.randint(0, height)
    trash_pos.append([x, y])

plant_size = 10
plant_pos = []
plant_color = [0, 255, 0]
for i in range(7):
    x = 0
    y = 0
    while x < 80 and y < 80:
        x = random.randint(0, width)
        y = random.randint(0, height)
    plant_pos.append([x, y])

img_life = pygame.image.load("coração.png")

score = 0
life = 3

fnt_gameover = pygame.font.SysFont("inconsolata.ttf", 50)
txt_gameover = fnt_gameover.render("FALECEU", True, (255, 255, 255))
fnt_win = pygame.font.SysFont("inconsolata.ttf", 30)
txt_win = fnt_win.render("VOCÊ COMPLETOU O SEU TRABALHO", True, (255, 255, 255))
fnt_msg = pygame.font.SysFont("inconsolata.ttf", 21)
txt_msg = fnt_msg.render("Agora receba um salário deprimente", True, (255, 255, 255))

pygame.mixer.init()
pygame.mixer.music.load("Im-blue.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if pygame.key.get_pressed()[pygame.K_UP]:
        player_pos[1] -= player_speed
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        player_pos[1] += player_speed

    for pos in trash_pos:
        if player_pos[0] + player_size >= pos[0] and \
           player_pos[0] <= pos[0] + trash_size and \
           player_pos[1] + player_size >= pos[1] and \
           player_pos[1] <= pos[1] + trash_size:
            trash_pos.remove(pos)
            score += 1

    for pos in plant_pos:
        if player_pos[0] + player_size >= pos[0] and \
           player_pos[0] <= pos[0] + trash_size and \
           player_pos[1] + player_size >= pos[1] and \
           player_pos[1] <= pos[1] + trash_size:
            plant_pos.remove(pos)
            life -= 1

    if life <= 0:
        alive = False

    screen.fill(bg_color)
    pygame.draw.rect(screen, player_color, player_pos + [player_size] * 2)

    for pos in plant_pos:
        pygame.draw.rect(screen, plant_color, pos + [plant_size] * 2)
    for pos in trash_pos:
        pygame.draw.rect(screen, trash_color, pos + [trash_size] * 2)

    for i in range(life):
        screen.blit(img_life, [20 * i + 20, 20])

    if not alive:
        player_speed = 0
        screen.blit(txt_gameover, [width/2, height/2])
        
    if score == 50:
        player_speed = 0
        screen.blit(txt_win, [100, height/2.5])
        screen.blit(txt_msg, [170, height/2.1])

    pygame.display.update()

pygame.quit()
sys.exit()
