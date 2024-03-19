import pygame

#pygame초기화
pygame.init()

#창 크기 설정
WINDOW_WIDTH = 1368
WIDOW_HETGHT = 768
 
#RGE 색상 기준으로 사용할 색깔 정의
BKACK = (0, 0, 0)
WHITE = (255,255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#창 설정
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WIDOW_HETGHT))
pygame.display.set_caption("환갑")

#백그라운드 색깔 설정
display_surface.fill(WHITE)

#이미지 붙이고 설정
yuhan_image = pygame.image.load("yuhan.png")
yuhan_rect = yuhan_image.get_rect()
yuhan_rect.topleft = (20,20)

#게임이 동작하는 동안 이벤트 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.blit(yuhan_image, yuhan_rect)
    #디스플레이 업데이트
    pygame.display.update()
pygame.quit()