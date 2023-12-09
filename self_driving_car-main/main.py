import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track.png')
car = pygame.image.load('tesla2.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 1100
car_y = 150
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 30
direction = 'down'
drive = True
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    print(up_px, right_px, down_px)

    # change direction (take turn)
    # if direction == 'up' and up_px != 255 and right_px == 255:
    #     direction = 'right'
    #     cam_x_offset = 30
    #     car = pygame.transform.rotate(car, -90)
    # elif direction == 'right' and right_px != 255 and down_px == 255:
    #     direction = 'down'
    #     car_x = car_x + 30
    #     cam_x_offset = 0
    #     cam_y_offset = 30
    #     car = pygame.transform.rotate(car, -90)
    # if direction == 'down' and down_px != 255 and right_px == 255:
    #     direction = 'right'
    #     car_y = car_y + 30
    #     cam_x_offset = 30
    #     cam_y_offset = 0
    #     car = pygame.transform.rotate(car, 90)
    # elif direction == 'right' and right_px != 255 and up_px == 255:
    #     direction = 'up'
    #     car_x = car_x + 30
    #     cam_x_offset = 0
    #     car = pygame.transform.rotate(car, 90)
    # drive
    if direction == 'down' and down_px == 255:
         car_y = car_y + 2
    # elif direction == 'right' and right_px == 255:
    #     car_x = car_x + 2
    # if direction == 'down' and down_px == 255:
    #     car_y = car_y + 2
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()