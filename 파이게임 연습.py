import pygame

#pygame초기화
pygame.init()

#창 크기 설정
WINDOW_WIDTH = 1368
WIDOW_HETGHT = 768
 
#창 설정
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WIDOW_HETGHT))
pygame.display.set_caption("환갑")

#게임이 동작하는 동안 이벤트 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()