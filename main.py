import pygame
import random


pygame.init()

def criaTiro(listaTiros, jogador):
    tiro = {
        
    }

# Screen
tamanho = (800, 600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Segue o mouse")
relogio = pygame.time.Clock()

# Variaveis
posicao_mouse = (0, 0)

# Imagens Jogador
jogador_parado = pygame.image.load("assets/Corvette/Idle.png").convert_alpha()
jogador_rect = jogador_parado.get_rect(center=(400, 300))

# Imagens Tiro
imagens_tiro =[]
for img in range(1, 10):
    imagens_tiro.append(pygame.image.load(f"assets/ataque/{img}.png").convert_alpha())

listaTiros = []

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.MOUSEMOTION:
            posicao_mouse = evento.pos

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                # Dispara um tiro
                criaTiro(listaTiros, jogador_rect)

    tela.fill((255, 255, 255))

    # Desenha Jogador

    # Calcula a direção da ponta do jogador de acordo com o mouse
    direcao = pygame.math.Vector2(posicao_mouse) - pygame.math.Vector2(jogador_rect.center)
    # direcao.normalize_ip() # Remove a magnitude do vetor e deixa apenas a direção

    # Calcula a rotação do jogador
    angulo = direcao.angle_to((1, 1))
    jogador_rotacionado = pygame.transform.rotate(jogador_parado, angulo)

    tela.blit(jogador_rotacionado, jogador_rect)

    pygame.display.update()
    relogio.tick(60)