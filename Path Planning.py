import pygame
import math

tunwid = int(input("Enter width of the deviation path : "))

pygame.init()
dis=pygame.display.set_mode((1200,600))
 
pygame.display.set_caption('Robot Path Planning')
dis.fill((255, 255, 255)) 
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
yellow = (255,255,0)
game_over=False
robot =[]
cord = []
dist = [5]
no = 0
w = 15
l = 40
anglerot = 'Angle Rotation'
rot = 0  
start = 0
point = 0
radian = 0
degree = 0




pygame.draw.rect(dis,black,pygame.Rect(30, 30, 160, 60),1)

image = pygame.Surface((l , w))
image.set_colorkey(white)
image.fill(green)
rect = image.get_rect()
rect.center=(100,100)


def caldegree(cord,point):
    if (cord[point+1][0]-cord[point][0] != 0):
            y2 = 600-cord[point+1][1]
            y1 = 600-cord[point][1]
            x2 = cord[point+1][0]
            x1 = cord[point][0]

            
            slope = (y2-y1)/(x2-x1)
            radian = math.atan(slope)
            degree = math.degrees(radian)

    if (cord[point+1][0]-cord[point][0] == 0):
            degree = 0
            radian = 0
            
    list = [degree,radian]
    return list



while not game_over:
    dis.fill((255, 255, 255)) 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.MOUSEBUTTONDOWN and start == 0:
            p = pygame.mouse.get_pos()
            cord.append(p)
            no=no+1
            
            print("no value "+str(no))
            print(cord[0][0])
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_s:
                start = 1
                xd = cord[0][0]
                yd = cord[0][1]
                l = caldegree(cord,point)
                degree = l[0]
                radian = l[1]
                anglerot = 'Angle Rotation '+str(degree)

                
        
    if no == 1:
        robot = cord[0]

    if no > 1:
        for x in range(0,no-1):
           
           l = math.dist(cord[x],cord[x+1])
           tempimage = pygame.Surface((l , tunwid))
           tempimage.set_colorkey(white)
           tempimage.fill(yellow)
           l = caldegree(cord,x)
           tempimage = pygame.transform.rotate(tempimage ,l[0])
           rect = tempimage.get_rect()
           rect.center=((cord[x][0]+cord[x+1][0])/2,(cord[x][1]+cord[x+1][1])/2)
           dis.blit(tempimage , rect)

           if x > 0:
               pygame.draw.circle(dis,yellow,cord[x],tunwid/2)
           
           
        for x in range(0,no-1):    
           pygame.draw.line(dis,black,cord[x],cord[x+1],2)



    font = pygame.font.Font('freesansbold.ttf', 12) 
    text = font.render(anglerot, True, blue, white)
    textRect = text.get_rect()
    textRect.center = (200 ,100) 
    dis.blit(text, textRect)


    
    if start ==1:
       
       rot = degree
       image1 = pygame.transform.rotate(image , rot)
       rect = image1.get_rect()
       rect.center = (xd,yd) 
       dis.blit(image1 , rect)

    
       
        
    if start == 1 and point <= no-2:
        
       
        

        if(cord[point+1][0]>cord[point][0]):
           xd = xd+5*math.cos(radian)
           yd = yd-5*math.sin(radian)

        if(cord[point+1][0]<cord[point][0]):
           xd = xd-5*math.cos(radian)
           yd = yd+5*math.sin(radian)

        

        dist1 = math.dist(cord[point],cord[point+1])
        dist2 = math.dist(cord[point],(xd,yd))
       
        if(dist2>dist1):
           point = point+1
           xd = cord[point][0]
           yd = cord[point][1]
           if point <= no-2: 
             l = caldegree(cord,point)
             degree = l[0]
             radian = l[1]
             anglerot = degree
             anglerot = str(anglerot)
             anglerot = 'Angle Rotation '+anglerot
             
             
             

        pygame.time.wait(50)   
 

        
    pygame.display.update()

pygame.quit()

    
    
quit()
