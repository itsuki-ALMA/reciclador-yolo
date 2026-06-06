from ultralytics import YOLO

model = YOLO("yolo11n-cls.pt")

results = model.train(
    data="dataset",
    epochs=15,
    imgsz=160,
    batch=8,
    workers=2,
    device="cpu",
    project="runs",
    name="reciclaveis"
)

print("Treinamento concluído!")