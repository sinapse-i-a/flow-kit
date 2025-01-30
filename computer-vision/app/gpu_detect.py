import torch

print("Versão do PyTorch:", torch.__version__)
print("CUDA Disponível:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("Nome da GPU:", torch.cuda.get_device_name(0))
    print("Versão do CUDA suportada pelo PyTorch:", torch.version.cuda)
else:
    print("CUDA não está disponível.")
