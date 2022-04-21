import pygame, random                                     #mooduli pygame,random importimine

pygame.init()                                             #pygame käivitamine

pygame.mixer.music.load('heli1.wav')                      #helifaili avamine kasutades pygame.mixer.music moodulit
pygame.mixer.music.play(-1)                               #helifaili mängimine, -1 tähistab heli mängimist lõpmatult
pygame.mixer.music.set_volume(0.4)                        #helifaili hääletugevuse seadistamine

# värvid
lBlue = [153, 204, 255]                                   #muutuja mille väärtus värv helesinine

# ekraani seaded
screenX = 640                                             #muutuja väärtus akna pikkus
screenY = 480                                             #muutuja väärtus akna kõrgus
screen = pygame.display.set_mode([screenX, screenY])      #soovitud suurusega akna tekitamine, mis lisatakse muutujasse.
pygame.display.set_caption("PingPong")                    #aknale nimetuse andmine
screen.fill(lBlue)                                        #ekraani tausta täitmine helesinine


pall = pygame.Rect(0, 0, 20, 20)                                         #muutuja mille väärtus Rect objektina, asukoht ja objekti mõõtmed
pallImage = pygame.image.load("ball.png")                                #pildi avamine ,muutuja omistab pildi.
pallImage = pygame.transform.scale(pallImage, [pall.width, pall.height]) #muutuja omastab palli suuruse xy koordinaadid laius, kõrgus.


alus = pygame.Rect(0, 0, 120, 20)                                        #muutja mille väärtus Rect objektina, asukoht ja objekti mõõtmed
alusimage = pygame.image.load("pad.png")                                 #pildi avamine ,muutuja omistab pildi.
alusimage = pygame.transform.scale(alusimage, [alus.width, alus.height]) #muutuja omastab aluse suuruse xy koordinaadid laius, kõrgus.


clock = pygame.time.Clock()                                                #muutuja mis võimaldab mängu ajaga (liikumine) sidumine
posX1, posY1 = random.randint(0,screenX-pallImage.get_rect().width), 0     #positsioon mille väärtus xy koordinaatidega juhuslik palli asukoht kogu ekraani ulatuses 0
posX2, posY2 = random.randint(0,screenX-alusimage.get_rect().width), screenY / 1.5 # aluse positsioon mille väärtus xy koordinaatidega , palgi y postisioon 1.5 ekraanil

speedX1, speedY1 = 3, 4         #palli kiiruse väärtused x y teljel
speedX2, speedY2 = 2, 4         #aluse kiiruse väärtused x y teljel

temp = 0                        #muutuja mille väärtus 0
skoor = 0                       #muutuja mille väärtus 0
mäng_läbi = False               #muutuja mäng_läbi mille väärtus vale


speedX, speedY = 0, 0          # muutuja kiiruse väärtused 0
directionX = 0                 #klavatuuri x suuna liigutamise väärtus liikumine kogu ekraani ulatuses ehk 0

juurdelisa, mahavota = 0, 0     #muutujad mille väärtused 0

gameover = False                    #muutuja mille väärtus on vale
while not gameover:                 #korduslause kui ei ole vale.

    # screen.fill(lBlue)
    clock.tick(60)                            #kella seadistus 60 kaadrit sekundis

    # mängu sulgemine ristist
    for event in pygame.event.get():          #event omistab tsüklis väärtuse kasutades pygame moodulit
        if event.type == pygame.QUIT:         #kui event tüübi väärtuseks sulgumine(pygame.QUIT)
            gameover = True                   #muutuja mängu lõpp mille väärtus õige, kui mäng suletakse

        elif event.type == pygame.KEYDOWN:    #tingimusel kui event tüübi väärtuseks võrdne klahvi allavajutamisel
            if event.key == pygame.K_RIGHT:   #kui klahvistik (võrdne) on parem nooleklahv
                directionX = "move_right"     #liikumise x koordinaadi väärtus on paremale liikumine
            elif event.key == pygame.K_LEFT:  #kui klahvistik (võrdne) on vasak nooleklahv
                directionX = "move_left"      #liikumise x koordinaadi väärtus on vasakule liikumine


        elif event.type == pygame.KEYUP:                                 #tingimusel kui event tüübi väärtuseks võrdne klahvistik lahtilastud
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:#kui võrdne klahvistiku parem nool või võrdne vasak nool
                directionX = 0                                           #liikumise väärtus võrdne nulliga

    if directionX == "move_left":                           #kui liikumine võrdne vasakule suund
        if posX2 > 0:                                       #kui positsioon suurem nullist
            posX2 -= 6                                      #positsiooni vähendamine 6 võrra ehk iseenda vasakule liikumine kiirusega 6
    elif directionX == "move_right":                        #kui liikumine võrdne paremale suund
        if posX2 + alusimage.get_rect().width < screenX:    #kui aluse positsioon väiksem ekraani x teljest
            posX2 += 6                                      #positsiooni suurendamine 6 võrra ehk iseenda(palgi) paremale liikumine kiirusega 6



        font1 = pygame.font.Font(pygame.font.match_font('tahoma'),24)  #muutja font 1 väärtusega fondi kirjastiil, teksti suurus
        font2 = pygame.font.Font(pygame.font.match_font('arial'), 40)  #muutja font 2 väärtusega fondi kirjastiil, teksti suurus


    screen.blit(pallImage, (posX1, posY1)) #tausta uuesti joonistamine vastavalt asetusele

    posX1 += speedX1       #postitsiooni X väärtus asetus muutub vastavalt kiirusele
    posY1 += speedY1       #postitsiooni Y väärtus asetus muutub vastavalt kiirusele

    if posX1 > screenX - pallImage.get_rect().width or posX1 < 0:  #kui X1 juhusliku palli positsioon on suurem ekraanil objektist või väiksem kui 0 ehk kokkupõrkeni äärtest
        temp = posY1                                               #muutuja väärtus posY1
        speedX1 = -speedX1                                         #objekti(palli) enda kiiruse suunamuutus kokkupuutel x telje äärtega

    screen.blit(alusimage, (posX2, posY2))  # tausta uuesti joonistamine vastavalt palgi asetusele


    if posY1 < 0:            #kui positsioon(palli) väiksem 0`st.
        temp = posY1         #muutuja väärtus Y1 positsioon
        speedY1 = -speedY1   #objekti(palli) enda kiiruse suunamuutus kokkupuutel y telje äärtega


    if posY1 == posY2 and temp < posY2:                                     #kui positsiooon Y1 võrdne Y2 ehk palli/aluse kokkupuutepunkt ja temp(0) väiksem Y2 positsioonist
        if posX1 >= posX2 and posX1 <= posX2 + alusimage.get_rect().width:  #kui postitsioon X1 suurem või võrdne X2 ja X1 väiksem või võrne X2 koos aluse laiusega
            speedY1 = -speedY1                                              #kiirus väheneb, liigub teisele poole
            skoor += 1                                                      #muutujale skoor lisatakse enda väärtusele +1
            juurdelisa = pygame.time.get_ticks() + 1000                     #muutja mille väärtusena kasutatakse pygame, time moodulit

    elif posY1 == posY2 and temp > posY2:                                                #tingimusel kui positsiooon Y1 võrdne Y2 ehk palli/aluse kokkupuutepunkt ja temp(0) suurem Y2 positsioonist
        if posX1 >= posX2 and posX1 <= posX2 + alusimage.get_rect().width and skoor > 0: #kui postitsioon X1 suurem või võrdne X2 ja X1 väiksem või võrne X2 koos aluse laiusega ja skoor suurem kui 0
            skoor -= 1                                                                   #muutujale skoor vähendatakse enda väärtust -1
            mahavota = pygame.time.get_ticks() + 1000                                    #muutja mille väärtusena kasutatakse pygame, time moodulit

    font1 = pygame.font.Font(pygame.font.match_font('tahoma'), 24)                 #muutja font 1 väärtusega fondi suurus, kirjastiil
    font2 = pygame.font.Font(pygame.font.match_font('arial'), 40)                  #muutja font 2 väärtusega fondi suurus, kirjastiil
    punktisumma = font1.render("Punkte: " + str(skoor), True, [255, 255, 255])     #muutuja mille väärtus sõnena valge värvusega
    screen.blit(punktisumma, [screenX - 630, screenY - 470])                       #punktisumma fondi asukoht x y koordinaatidega ekraanil

    juurde = font2.render("+1", True, [0, 255, 0])                     #muutuja mille värvus rohelise värvusega sõnena +1


    if pygame.time.get_ticks() < juurdelisa:                           #kui aja mooduli väärtus väiksem juurdelisa väärtusest

        screen.blit(juurde, [(screenX - 50) / 2.3, screenY / 3])        #teksti ekraanile joonistamine/värskendamine x y koordinaatidega ekraani suurusest jagatis võimalikult keskkkohta




    if posY1 == screenY + pallImage.get_rect().height:              #kui posY1 võrdne palli asukohaga
        pygame.mixer.music.load('heli2.wav')                        #helifaili avamine kasutades pygame.mixer.music moodulit
        pygame.mixer.music.play()                                   #helifaili mängimine
        pygame.mixer.music.set_volume(0.2)                          #helifaili hääletugevuse seadistamine
        lopp = font2.render("Mäng läbi", True, [255, 0, 0])         #muutuja mille väärtus tektina, punase värvusega
        screen.blit(lopp, [(screenX - 150) / 2, screenY / 3])       #tekst ekraanile joonistamine/värskendamine x y koordinaatidega ekraani suurusest jagatis võimalikult keskkkohta
        pygame.display.update()                                     #ekraani uuendamine
        pygame.time.delay(2500)                                     #aja viivitus kaua tekst ekraanil on
        mäng_läbi = True                                            #muutuja mille väärtus tõene



    pygame.display.flip()            #ekraani värskendamine
    screen.fill(lBlue)               #ekraani tausta uuesti täitmine helesinine



pygame.quit()                        #mängu sulgemine


# Github link