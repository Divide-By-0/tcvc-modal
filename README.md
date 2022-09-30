# tcvc-modal

Running image colorization on video in the cloud

## Install

On your laptop:

```
git clone --recursive git@github.com:Divide-By-0/tcvc-modal.git
cd tcvc-modal && git clone https://github.com/Divide-By-0/TCVC-Temporally-Consistent-Video-Colorization
mv TCVC-Temporally-Consistent-Video-Colorization TCVC
python3 main.py
```

Setup on the machine running the code:

```
sudo apt update && sudo apt-get install -y python3-pip
pip install --force-reinstall https://modal.com/api/client-library/us-szqX2y2eZXtjoc3loHEdiv/modal-0.0.33-py3-none-any.whl
wget https://tcvc.s3.amazonaws.com/TCVC_IDC.zip # Colorization backbone model
wget https://tcvc.s3.amazonaws.com/pretrained_models.zip # Pretrained TCVC
pip install -r TCVC/codes/requirements.txt
conda install --file TCVC/codes/conda_requirements.txt
# Run command to add modal api token here from modal.com setup (dm me at aayushg@mit.edu for access)
mkdir videos
gdown "https://drive.google.com/uc?id=1876eGDhyKhc2rx2X-A_FffB3ZX2FXTOc" # Get video
mv <videonam_that_you_just_downloaded> videos
python3 main.py
```

Uploaded the TCVC files to s3://tcvc.

<!-- gdown --fuzzy https://drive.google.com/file/d/1876eGDhyKhc2rx2X-A_FffB3ZX2FXTOc/view -->
