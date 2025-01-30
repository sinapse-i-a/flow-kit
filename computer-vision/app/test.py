import cv2
from matplotlib import pyplot as plt

# Função para verificar se a janela está aberta
def is_window_open(fig):
    return plt.fignum_exists(fig.number)

# Captura de vídeo da webcam
cap = cv2.VideoCapture(0)

# Cria a figura
fig, ax = plt.subplots()
plt.ion()  # Modo interativo

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Converte a imagem para RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Atualiza a imagem na janela
    ax.clear()
    ax.imshow(img_rgb)
    ax.set_title('Image')
    ax.axis("off")
    plt.draw()
    plt.pause(0.01)

    # Verifica se a janela está aberta
    if not is_window_open(fig):
        break

# Libera a captura de vídeo e fecha todas as janelas
cap.release()
plt.close(fig)