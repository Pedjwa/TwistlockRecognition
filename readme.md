Project for the SMR Twistlock Recognition Assignment.
A web page is created using Python Flask and the coupling is made to a YOLOv5 model using the detect.py inference

Prepare YOLOv5 environment
Python 3.8.7
Sypder IDE

Add git to path
"%LOCALAPPDATA%\GitHubDesktop\app-2.6.1\resources\app\git\cmd"

git clone https://github.com/Pedjwa/TwistlockRecognition
cd ./TwistlockRecognition
pip install -r requirements.txt

If torchvision error:
! pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

python camapp.py
Go to 127.0.0.0:5000