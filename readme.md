Prepare YOLOv5 environment
Python 3.8.7
Sypder IDE

Add git to path
"C:\Users\pkiai\AppData\Local\GitHubDesktop\app-2.6.1\resources\app\git\cmd"

cd E:\Programming\SMR Siemens\PyTorch YOLOv5\PlaygroundMode
git clone https://github.com/ultralytics/yolov5 && cd yolov5 # clone latest
% cd ./yolov5
! ls
pip install -r requirements.txt
# If torchvision error:
! pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

Prepare html evironment
pip install flask
cd "E:\Programming\SMR Siemens\PyTorch YOLOv5\PlaygroundMode\CamApp"
python camapp.py

