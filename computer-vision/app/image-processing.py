from ultralytics import YOLO
import cv2
import os

# Certifique-se de que o modelo utiliza a GPU
model = YOLO('yolov8x.pt')  # Baixa o modelo YOLOv8
model.to('cuda')
print(f"Device: {model.device}")  # Deve exibir "cuda"

# Cria o diretório de saída se não existir
# input_dir = "/usr/src/app/input"
# output_dir = "/usr/src/app/output"
input_dir = "./input"
output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)

# Processa todas as imagens do diretório
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(input_dir, filename)
        results = model(image_path)
        
        for i, result in enumerate(results):
            annotated_image = result.plot()
            output_path = os.path.join(output_dir, f"{filename.split('.')[0]}_result.jpg")
            cv2.imwrite(output_path, annotated_image)
            print(f"Imagem processada salva em: {output_path}")