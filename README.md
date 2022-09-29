# tcvc-modal

Running image colorization on video in the cloud

## Install

```
git clone --recurse-submodules --remote-submodules git@github.com:Divide-By-0/tcvc-modal.git
sudo apt update && sudo apt-get install -y python3-pip
pip install --force-reinstall https://modal.com/api/client-library/us-szqX2y2eZXtjoc3loHEdiv/modal-0.0.33-py3-none-any.whl
pip install opencv-python
# add modal api token here, dm Aayush for command
mkdir videos
gdown "https://drive.google.com/uc?id=1876eGDhyKhc2rx2X-A_FffB3ZX2FXTOc" # Get video
mv <videonam_that_you_just_downloaded> videos
python3 main.py
```

<!-- gdown --fuzzy https://drive.google.com/file/d/1876eGDhyKhc2rx2X-A_FffB3ZX2FXTOc/view -->
