import pygame

# Inicializa a biblioteca pygame
pygame.init()

# Caminho do arquivo .mp3
caminho_do_mp3 = 'C:/Users/arthur.rosa/Documents/GitHub/Estudos/Python/Arquivos/A7x-Cosmic.mp3'

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega o arquivo .mp3
pygame.mixer.music.load(caminho_do_mp3)

# Reproduz o áudio
pygame.mixer.music.play()

# Mantém o programa rodando para permitir a reprodução completa do áudio
pygame.time.Clock().tick(10)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Finaliza a biblioteca pygame
pygame.quit()
