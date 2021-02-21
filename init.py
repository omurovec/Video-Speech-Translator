import os

# Resource repos
Wav2Lip = "https://github.com/Rudrabha/Wav2Lip"
WaveRNN = "https://github.com/Tomiinek/WaveRNN"
Multilingual_Text_to_Speech = "https://github.com/Tomiinek/Multilingual_Text_to_Speech"

# Weights
Wav2Lip_face_weight = "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth"
WaveRNN_weight = "https://github.com/Tomiinek/Multilingual_Text_to_Speech/releases/download/v1.0/wavernn_weight.pyt"
tacotron = "https://github.com/Tomiinek/Multilingual_Text_to_Speech/releases/download/v1.0/generated_switching.pyt"

# Setup Wav2Lip
if not os.path.exists("./dependencies/Wav2Lip/"):
    os.system("git clone " + Wav2Lip + " ./dependencies/Wav2Lip")
    os.system(
        "curl -o ./dependencies/Wav2Lip/face_detection/detection/sfd/s3fd.pth "
        + Wav2Lip_face_weight
    )
    os.system("pip install -r ./dependencies/Wav2Lip/requirements.txt")

# Setup Multilingual TTS
if not os.path.exists("./dependencies/Multilingual_Text_to_Speech"):
    os.system("git clone " + Multilingual_Text_to_Speech + " ./dependencies/Multilingual_Text_to_Speech")
    os.system("curl -o ./dependencies/checkpoints/generated_switching.pyt " + tacotron)
    os.system("pip install -r ./dependencies/Multilingual_Text_to_Speech/requirements.txt")

# Setup WaveRNN
if not os.path.exists("./dependencies/WaveRNN"):
    os.system("git clone " + WaveRNN + " ./dependencies/WaveRNN/")
    os.system("curl -o ./dependencies/checkpoints/wavernn_weight.pyt " + WaveRNN_weight)
    os.system("pip install -r ./dependencies/WaveRNN/requirements.txt")
