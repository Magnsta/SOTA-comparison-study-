# SOTA-comparison-study-
Repository for my master thesis in Simulation and Visualization. Topic for the thesis is, A Comparative Study of Face Anonymization Performance on Multiple Systems for Real-Time Object Detection. The following repository represents the files used. See the README file for additional information.
# Preparing the environment
For setting up the environment with all depending libriaries, please refer to https://github.com/ultralytics/ultralytics for instructions. 

# Downloading the face datasets:

### Raw
Contains 5000 face images downloaded from Open Images V7. 
link: https://drive.google.com/drive/folders/1s49x9G8sjG4J9Pf_cige29oxVQMYQxH7?usp=sharing

### Filtered
Approximitly 3000 images remaining after a manual review of the raw datasets. All images downloaded from Open Images V7.
link: https://drive.google.com/drive/folders/1cLaivOMQTyiIMwHEjfVSH2DPHIjVAQIg?usp=sharing

### Mosaic
Approximitly 3000 images with mosaic augmentation applied on the filtered datasets. 
link: https://drive.google.com/drive/folders/1rLGF2lbyEXCLUN_q7s1CpYBBxfRqkcUS?usp=sharing

# Downloading the face model weights:
### Yolov8n
link: https://drive.google.com/drive/folders/1K0kUAYTYzLtabShGXLVqRoQyxD6LA-2v?usp=sharing

### Yolov8m
link: https://drive.google.com/drive/folders/1Gei09x-x2t5xjVrTQv4VSWbpFrwvJ8gr?usp=sharing

### Yolov8l
link: https://drive.google.com/drive/folders/1VzH9JZpsCRbnvzxNnPV1Y-k8s8yX9GU0?usp=sharing


# Implementing anonymization in already existing YOLOv8 project
In cases where YOLOv8, and ultralytics is already cloned and running on a computer it is possible to only swap the plotting.py file found at yolo/utils/plotting.py and the cfg file found at to enable anonymization, with minimal modification. See plotting.py file for further instructions.

### Anonymization
(a) default standard YOLOv8. Setting anonymization=True the model applies a blur and random noise filter to the detected instances as shown in (c). The standard blur fliter without the additional random noise is shown in (b). 
![anonymisert](https://github.com/Magnsta/SOTA-comparison-study-/assets/56515134/ce907823-ee66-4451-a3e3-510c5b20e291)

