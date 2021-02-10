import pygame
from random import randrange

pygame.init()

# TAMANHO
largura = 420
altura = 380
cobra = 10
placar = 40
# CORES
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255, 0, 0)
cinza = (47,79,79)
verde = (0, 128, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
roxo = (128,0,128)
ciano = (0,255,255)
rosa = (255,20,147)
#Inicialização
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('made by the blessed ')
#musica = pygame.mixer.music.load("Lofi-byRiddiman.mp3")
fundo = pygame.image.load("fundo.jpg")
#Mensagem -
def texto(msg,cor,tamanho,x,y):
    fonte = pygame.font.SysFont(None, tamanho)
    txt1 = fonte.render(msg,True,cor)
    janela.blit(txt1,[x,y])
#FPS
relogio = pygame.time.Clock()
def cobrinha(CobraXY,cor):
    for XY in CobraXY:
        pygame.draw.rect(janela, cor, [XY[0], XY[1], cobra, cobra])
def apple(apple_x, apple_y,cor_maca):
       pygame.draw.rect(janela, cor_maca, [apple_x, apple_y, cobra, cobra])
def menu():
    janela.fill(branco)
    texto('- SNAKE -', verde, 100, 30, 20)
    texto('Jogo feito por: OS ABENÇOADOS 911-A', preto, 25, largura / 10, 300)
#ifal = pygame.image.load(r"C:\Users\Eliezir\Pictures\ifal.png")
def jogo():
    cor = verde
    dificuldade = 1
    start = True
    pre_jogo = True
    skin = True
    while pre_jogo == True:
        while start == True:
            menu()
            pygame.draw.rect(janela, preto, [95, 115, 220, 50])
            texto('START (S)', branco,65,100,120)
            pygame.draw.rect(janela, preto, [85, 185, 268, 55])
            texto('OPÇOES (O)',branco,65,90,190)
            #janela.blit(ifal,(10,10))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        start = False
                        pre_jogo = False
                    elif event.key == pygame.K_o:
                        start = False
                        opc = True
                        while opc == True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_f:
                                        dificuldade = 1

                                        opc = False
                                    elif event.key == pygame.K_d:
                                        dificuldade = 2
                                        opc = False
                            menu()
                            texto('Escolha a dificuldade:',preto,45,40,150)
                            pygame.draw.rect(janela, preto, [55,195,125,45])
                            texto('Facil (F) ', branco, 45, 60, 200)
                            pygame.draw.rect(janela, preto, [245, 195, 145, 45])
                            texto('Dificil (D) ', branco, 45, 250, 200)
                            pygame.display.update()
                        while skin == True:
                            menu()
                            texto('Escolha a cor da cobra:', preto, 45, 40, 85)
                            pygame.draw.rect(janela, preto, [40, 120, 100, 30])
                            texto('ROSA (R)',rosa,30,45,125)
                            pygame.draw.rect(janela, preto, [40, 170, 110, 30])
                            texto('CIANO (C)', ciano,30, 45, 175)
                            pygame.draw.rect(janela, preto, [40, 220, 120, 30])
                            texto('PURPLE(P)',roxo, 30, 45, 225)
                            pygame.draw.rect(janela, preto, [245, 120, 94, 30])
                            texto('BLUE (B)', azul, 30, 250, 125)
                            pygame.draw.rect(janela, preto, [245, 170, 145, 30])
                            texto('AMARELO (A)', amarelo, 30, 250, 175)
                            pygame.draw.rect(janela, preto, [245, 220, 105, 30])
                            texto('VERDE (V)', verde, 30, 250, 225)
                            pygame.display.update()
                            for event in pygame.event.get():
                                  if event.type == pygame.QUIT:
                                      pygame.quit()
                                  if event.type == pygame.KEYDOWN:
                                      if event.key == pygame.K_r:
                                          cor = rosa
                                          skin = False
                                          start = True
                                      elif event.key == pygame.K_c:
                                          cor = ciano
                                          skin = False
                                          start = True
                                      elif event.key == pygame.K_p:
                                          cor = roxo
                                          skin = False
                                          start = True
                                      elif event.key == pygame.K_b:
                                          cor = azul
                                          skin = False
                                          start = True
                                      elif event.key == pygame.K_a:
                                          cor = amarelo
                                          skin = False
                                          start = True
                                      elif event.key == pygame.K_v:
                                          cor = verde
                                          skin = False
                                          start = True
    jogar_dnv = True
    #pygame.mixer.music.play(-1)

    while jogar_dnv:
          pontos = 0
          maca = 0
          cor_maca = vermelho
          #Sort cobra
          pos_x = randrange(0, largura- cobra, 10)
          pos_y = randrange(0, altura - cobra -placar, 10)
          #Sort Maçã
          apple_x= randrange(0, largura - cobra, 10)
          apple_y = randrange(0, altura - cobra-placar, 10)
          #Variaveis
          perdeu = False
          velocidade_x = 0
          velocidade_y = 0
          sair = False
          CobraXY = []
          CobraComp = 1
          while sair == False:
              while perdeu:
                  janela.fill(branco)
                  texto("Você Perdeu",vermelho,70,60,30)
                  texto('Sua pontuação foi: '+str(pontos),preto,40,65,80)
                  pygame.draw.rect(janela,preto,[50,120,185,40])
                  texto('Continuar (C)',branco,40,50,125)
                  pygame.draw.rect(janela, preto, [260,120,110,40])
                  texto('Sair (S)',branco,40,265,125)
                  texto('Jogo feito por: OS ABENÇOADOS 911-A',preto,25,largura/10,300)
                  pygame.display.update()
                  for event in pygame.event.get():
                      if event.type == pygame.QUIT:
                          sair = True
                          perdeu = False
                          jogar_dnv = False
                      if event.type == pygame.KEYDOWN:
                          if event.key == pygame.K_c:
                              sair = True
                              perdeu = False
                          elif event.key == pygame.K_s:
                              sair = True
                              perdeu = False
                              jogar_dnv = False
              #Detectar comandos
              for event in pygame.event.get():
                  #Fechar o jogo
                  if event.type == pygame.QUIT:
                      sair = True
                      jogar_dnv = False
                  #Andar
                  if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_LEFT and velocidade_x != cobra:
                          velocidade_y = 0
                          velocidade_x = -cobra
                      if event.key == pygame.K_RIGHT and velocidade_x != -cobra:
                          velocidade_y = 0
                          velocidade_x = cobra
                      if event.key == pygame.K_UP and  velocidade_y != cobra:
                          velocidade_x = 0
                          velocidade_y = -cobra
                      if event.key == pygame.K_DOWN and velocidade_y != -cobra:
                          velocidade_x = 0
                          velocidade_y = cobra
              janela.fill(branco)
              janela.blit(fundo,(0,0))
              pos_x += velocidade_x
              pos_y += velocidade_y
              if apple_x == pos_x and apple_y == pos_y:
                  apple_x = randrange(0, largura - cobra, 10)
                  apple_y = randrange(0, altura - cobra - placar, 10)
                  if maca != 4 :
                      maca += 1
                      CobraComp += 1
                      pontos +=1
                      if maca != 4:
                          cor_maca = vermelho
                      elif maca==4:
                        cor_maca = cinza
                  elif maca == 4 :
                      maca = 0
                      CobraComp += 3
                      pontos += 3
                      cor_maca = vermelho
              apple(apple_x, apple_y,cor_maca)
              relogio.tick(10)
              # Bordas
              if dificuldade == 1:
                  if pos_x < 0:
                      pos_x = largura
                  elif pos_x + cobra > largura:
                      pos_x = 0
                  if pos_y < 0:
                      pos_y = altura-placar
                  elif pos_y + cobra > altura-placar:
                      pos_y = 0
              elif dificuldade == 2 or dificuldade == 3:
                  if pos_x + cobra > largura:
                      perdeu = True
                  elif pos_x < 0:
                      perdeu = True
                  elif pos_y + cobra > altura-placar:
                      perdeu = True
                  elif pos_y < 0:
                      perdeu = True
              CobraInicio = []
              CobraInicio.append(pos_x)
              CobraInicio.append(pos_y)
              CobraXY.append(CobraInicio)
              if len(CobraXY) > CobraComp:
                  del CobraXY[0]
              if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                  perdeu = True
              pygame.draw.rect(janela, preto, [0,altura-40, largura, 40])
              texto('Pontuação: '+ str(pontos),branco,30,10,altura-30)
          cobrinha(CobraXY,cor)              
          pygame.display.update()

jogo()