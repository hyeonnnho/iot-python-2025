# 벽돌깨기 게임

import pygame 
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect, K_SPACE
import sys 

import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

class Block:
    def __init__(self, col, rect, speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45,45) + 270  # 225 ~ 315

    def move(self): # 공 움직임
        # 공의 움직이는 x축 값을 계속 계산하려면 x는 dir 값을 라디언으로 변환 후 코사인 처리
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        # 공의 움직이는 y축 값을 계속 계산하려면 y는 dir 값을 라디언으로 변환 후 사인 처리
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw_E(self): # 공을 circle이 아니라 ellipse로 생성
        pygame.draw.ellipse(Surface, self.col, self.rect)
    def draw_R(self):
        pygame.draw.rect(Surface, self.col, self.rect)     

pygame.init()
Surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Blocks!!')
pygame.key.set_repeat(10,10)

def main():
    is_game_start = False
    score = 0
    BlOCK = []
    BALL = Block((200,200,0), Rect(375, 650, 20, 20), 10)
    # 클래스 생성
    # 무지개색 정보
    colors = [(255, 0, 0),(255, 165, 0),(255, 255, 0),(0, 255, 0),(0, 0, 255),(75, 0, 130),(238, 130, 238)]
    # 초기에 생성될 블럭들(무지개색으로 9x6 = 54개 블록)
    for y, color in enumerate(colors, start=0): # y값은 0~6
        for x in range(0,9):
            BlOCK.append(Block(color, Rect(x*80 + 150, y*40+ 40, 60, 20)))
    bigFont = pygame.font.SysFont('NanumGothic', 80)
    smallFont = pygame.font.SysFont('NanumGothic', 45)
    M_GAME_TITLE = bigFont.render('GAME START?', True, 'white')
    M_GAME_SUBTITLE = smallFont.render('PRESS SPACE_BAR', True, 'white')
    M_CLEAR = bigFont.render('START!!', True, 'yellow')
    M_FAIL = bigFont.render('FAILED', True, 'red')

    while True:
        # 스코어, 스피드 글자.
        Surface.fill((0, 0, 0))  
        for event in pygame.event.get():  # 이벤트 처리 기본
            if event.type == QUIT: 
                pygame.quit() 
                sys.exit() 
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pass
                elif event.key == K_RIGHT:
                    pass
                elif event.key == K_SPACE:
                    is_game_start = True # 게임시작

        # 게임 화면 렌더링
        if is_game_start == False:
            Surface.blit(M_GAME_TITLE, ((SCREEN_WIDTH/ 2)-(400/2), (SCREEN_HEIGHT)/2-(50/2)))
            Surface.blit(M_GAME_SUBTITLE, ((SCREEN_WIDTH/2) - (300/2), (SCREEN_HEIGHT/2)+50))
        else: # 게임 시작 후 부 블록 다 그리고 볼이 움직이게 처리,바로 움직이도록
            LenBlock = len(BlOCK) # 54으로 시작
            # BlOCK = [x for x in BlOCK]

            if BALL.rect.centery < 1000:
                BALL.move()

            if BALL.rect.centerx < 0 or BALL.rect.centerx > 1000: # 게임화면 양쪽 벽 밖으로 못 나가게
                BALL.dir = 180 - BALL.dir # 반사각만큼 방향 전환
            elif BALL.rect.centery < 0: # 게임화면 천장에 부딪히면 반사
                BALL.dir = -BALL.dir
        
            BALL.draw_E()

            for i in BlOCK: # Block()
                i.draw_R()

        pygame.display.update() 
        FPSCLOCK.tick(30) 

if __name__ == '__main__':
    main()









