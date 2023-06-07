from ultralytics import YOLO

model = YOLO("best.pt") #Load model


#Set anonymization TRUE to enable the anonymization filter. 
#If set to FALSE, standard YOLOv8 code is running.
model.predict(source=0, show=True,imgsz=640,save=True,anonymization=True)