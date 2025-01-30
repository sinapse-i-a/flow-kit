from ultralytics import YOLO
from matplotlib import pyplot as plt
import cv2

# Função para verificar se a janela está aberta
def is_window_open(fig):
    return plt.fignum_exists(fig.number)

# Captura de vídeo da webcamq
cap = cv2.VideoCapture(0)

model = YOLO("yolo11n.pt")
model.to('cuda')

print(f"Device: {model.device}")  # Deve exibir "cuda"

# Cria a figura
fig, ax = plt.subplots()
plt.ion()  # Modo interativo

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    results = model(frame)

    for result in results:
        frame = result.plot()

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
