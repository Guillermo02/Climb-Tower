# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 500
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Climbing Tower')

# ----- Inicia assets
METEOR_WIDTH = 50
METEOR_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('img/trump.png').convert()
background = pygame.transform.scale(background, (500, 800))
PP = pygame.image.load('img/Plataforma.png').convert()
PP = pygame.transform.scale(PP, (150,200))


class Plataforma(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100,300)
        self.rect.y = random.randint(100,600)

# Criando um grupo de meteoros
Tudo = pygame.sprite.Group()
# Criando os meteoros
for i in range(8):
    TP = Plataforma(PP)
    Tudo.add(TP)

# ----- Inicia estruturas de dados
game = True
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    Tudo.draw(window)
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados