from ultralytics import YOLO


model = YOLO("weight.pt") #Load model

#Set anonymization=True to enable the anonymization filter. 
model.predict(source=0, show=True,imgsz=640,save=True,anonymization=True)
