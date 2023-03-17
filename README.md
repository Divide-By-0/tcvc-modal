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
Choose an AWS Community AMI with Cuda 10.2 in the name.

```
sudo apt update && sudo apt-get install -y python3-pip
curl https://bootstrap.pypa.io/pip/3.5/get-pip.py -o get-pip.py && python3 get-pip.py
# pip install --force-reinstall https://modal.com/api/client-library/us-szqX2y2eZXtjoc3loHEdiv/modal-0.0.33-py3-none-any.whl
pip3 install -r requirements.txt
wget "https://tcvc.s3.amazonaws.com/TCVC_IDC.zip" # Colorization backbone model
wget "https://tcvc.s3.amazonaws.com/pretrained_models.zip" # Pretrained TCVC
pip install -r TCVC/codes/requirements.txt
conda install --file TCVC/codes/conda_requirements.txt
# Run command to add modal api token here from modal.com setup (dm me at aayushg@mit.edu for access)
mkdir videos
gdown "https://drive.google.com/uc?id=1876eGDhyKhc2rx2X-A_FffB3ZX2FXTOc" # Get video
mv <videonam_that_you_just_downloaded> videos
python3 main.py
```

Amazon Linux: AMI ID  ami-0d245d4b67431f496 with name nvidia-driver-440.53-cuda-10.2-v14-g4dn-AMI
```
sudo yum install git
sudo yum update -y
sudo yum install -y python3
git clone https://github.com/Divide-By-0/tcvc-modal/
cd tcvc-modal && git clone https://github.com/Divide-By-0/TCVC-Temporally-Consistent-Video-Colorization
mv TCVC-Temporally-Consistent-Video-Colorization TCVC
sudo yum –y install python3-pip
pip3 install -r requirements.txt
wget "https://tcvc.s3.amazonaws.com/TCVC_IDC.zip" # Colorization backbone model
wget "https://tcvc.s3.amazonaws.com/pretrained_models.zip" # Pretrained TCVC
pip3 install -r TCVC/codes/requirements.txt --use-feature=2020-resolver
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
exit
# re-ssh
cd tcvc-modal
conda install --file TCVC/codes/conda_requirements.txt
sudo yum groupinstall "Development Tools"
wget "https://tcvc.s3.amazonaws.com/cudnn-local-repo-rhel7-8.6.0.163-1.0-1.x86_64.rpm"
sudo yum localinstall cudnn-local-repo-rhel7-8.6.0.163-1.0-1.x86_64.rpm
cd TCVC/codes/models/archs/networks/channelnorm_package/
CUDA_HOME=~/miniconda3/pkgs/cuda-toolkit/ python setup.py develop
CUDA_HOME=~/miniconda3/pkgs/cudatoolkit-10.1.243-0 python setup.py develop
```

Uploaded the TCVC files to s3://tcvc.

<!-- gdown --fuzzy https://drive.google.com/file/d/1876eGDhyKhc2rx2X-A_FffB3ZX2FXTOc/view -->
