from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
#задай фон сцены
background = transform.scale(image.load('background.png'),(700, 500)) 
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('sprite1.png'), (100,100))
sprite2 = transform.scale(image.load('sprite2.png'), (100,100))
#обработай событие «клик по кнопке "Закрыть окно"»
clock = time.Clock()
x1 = 50
y1 = 300
FPS = 60
game = True
x2 = 500
y2 = 300
speed = 10
while game:
   keys_pressed = key.get_pressed()
   window.blit(background, (0,0))
   window.blit(sprite1, (x1, y1))
   window.blit(sprite2, (x2, y2))
   if keys_pressed[K_UP] and y1 > 5:
      y1 -= speed
   if keys_pressed[K_LEFT] and x1 > 5:
      x1 -= speed
   if keys_pressed[K_RIGHT] and x1 < 595:
      x1 += speed
   if keys_pressed[K_DOWN] and y1 < 395:
      y1 += speed

   if keys_pressed[K_s] and y2 < 395:
      y2 += speed
   if keys_pressed[K_w] and y2 > 5:
      y2 -= speed
   if keys_pressed[K_a] and x2 > 5:
      x2 -= speed
   if keys_pressed[K_d] and x2 < 595:
      x2 += speed

   for e in event.get():
        if e.type == QUIT:
           game = False

   display.update()
   clock.tick(FPS)