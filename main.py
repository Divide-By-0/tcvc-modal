import modal

setup_image = modal.Image

volume = modal.SharedVolume().persist("tcvc-repo-vol")
CACHE_PATH = "~/Documents/projects/tcvc-modal"


stub = modal.Stub(mounts=[modal.Mount(local_dir="~/Documents/projects/tcvc-modal/", remote_dir="~/project"),
                          modal.Mount(local_dir="~/Documents/projects/tcvc-modal/videos", remote_dir="/data2/yhliu/old_film")],
                  image=setup_image.conda()
                  #    .conda_install(["cudatoolkit=10.2", "cudnn=7.6.5"])
                  #   .pip_install_from_requirements("./requirements_pip.txt")
                  .conda_update_from_environment(environment_yml="./environment.yml")
                  .run_commands([
                      'apt-get update',
                      'apt-get install git -y'])
                  .run_commands([
                      'git clone --recursive https://github.com/Divide-By-0/tcvc-modal',
                      'cd tcvc-modal && git clone https://github.com/Divide-By-0/TCVC-Temporally-Consistent-Video-Colorization',
                      'mv tcvc-modal/TCVC-Temporally-Consistent-Video-Colorization tcvc-modal/TCVC',
                  ])
                  .run_commands(["find / -name '*nvcc*'"])
                  .run_commands(['conda install anaconda && conda update --all'])
                  .run_commands(['conda env update --name base -f /tcvc-modal/environment.yml'])
                  .run_commands(["find / -name '*nvcc*'"])
                  .run_commands(['apt install build-essential wget -y'])
                  #   .run_commands(['wget https://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda_10.2.89_440.33.01_linux.run',
                  #  ])
                  #   .run_commands(['sh cuda_10.2.89_440.33.01_linux.run'])
                  .run_commands([
                      'conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch'
                      #   'conda install -c conda-forge -y cudatoolkit=10.1 cudatoolkit-dev=10.0 cudnn=7.6.5',
                      #   'conda install -c hcc cudatoolkit=10.1'
                  ])
                  .run_commands(['find / -name "*nvcc*"'])
                  .run_commands(['find / -name "*cuda*"'])
                  .run_commands(['nvcc --version'])
                  .run_commands(['ls /usr/local'])
                  .run_commands([                  # 'ls /usr/local/lib/python3.9/site-packages/cuda',
                      'CUDA_HOME=/usr/local/lib/python3.9/site-packages/cuda python tcvc-modal/TCVC/codes/models/archs/networks/channelnorm_package/setup.py develop',
                      'CUDA_HOME=/usr/local/lib/python3.9/site-packages/cuda python tcvc-modal/TCVC/codes/models/archs/networks/correlation_package/setup.py develop',
                      'CUDA_HOME=/usr/local/lib/python3.9/site-packages/cuda python tcvc-modal/TCVC/codes/models/archs/networks/resample2d_package/setup.py develop',
                      'CUDA_HOME=/usr/local/lib/python3.9/site-packages/cuda python tcvc-modal/TCVC/codes/test_TCVC_onesampling_noGT.py',
                      # 'export PYTHONPATH=.'
                      # "gdown 'https://drive.google.com/uc?id=1876eGDhyKhc2rx2X-A_FffB3ZX2FXTOc'" # Get video
                      # ],)
                  ])  # .run_commands(['python -c "import torch; print(torch.version.cuda)"'])
                  ,
                  # shared_volumes={CACHE_PATH: volume},
                  secret=modal.Secret.from_name("CUDA_HOME"), gpu=True
                  )

if __name__ == "__main__":
    with stub.run():
        print("Running")

    # def download_file(url):
    # import gdown
    # url = 'https: //drive.google.com/uc? id $=0$ B9P 1L--7Wd2vNm9zMTJWOGxobkU'
    # output = '20150428_collected_images.tgz'
    # gdown. download(url, output, quiet=False)
    # $\mathrm{md} 5=$ 'fa837a88f0c40c513d975104edf3da17'
    # gdown. cached_download(url, output, md5=md5, postprocess=gdown. extractall)
