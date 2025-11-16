from ultralytics import YOLO

model = YOLO("yolov8n.pt")

print("All Class Names:")
print(model.names)

print("\nLoop Through Classes:")
for class_id, class_name in model.names.items():
    print(f"Class ID: {class_id} -> Class Name: {class_name}")