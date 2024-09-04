import pyautogui
import time

# Tempo para garantir que o foco esteja na janela correta
time.sleep(5)  # Ajuste conforme necessário

# Número de repetições (colocar número de repetições -1, pois o primeiro é o [0])
repeticoes = 16

# Inicia o loop para repetir o processo
for i in range(0, repeticoes + 1):
    # Pressiona a tecla F2
    pyautogui.press('f2')

    # Aguarda um breve momento para garantir que a tecla F2 tenha efeito
    time.sleep(0.5)

    # Pressiona Ctrl + V para colar
    pyautogui.hotkey('ctrl', 'v')

    # Adiciona o número (i + 1) ao texto copiado
    pyautogui.typewrite(str(i + 1))

    # Pressiona Enter
    pyautogui.press('enter')

    # Pressiona a tecla para a esquerda
    pyautogui.press('right')

    # Aguarda um breve momento antes da próxima iteração
    time.sleep(0.5)


