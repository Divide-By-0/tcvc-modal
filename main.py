import modal

setup_image = modal.Image

volume = modal.SharedVolume().persist("tcvc-repo-vol")
CACHE_PATH = "~/Documents/projects/tcvc-modal"


stub = modal.Stub(mounts=[modal.Mount(local_dir="~/Documents/projects/tcvc-modal/", remote_dir="~/project"),
                          modal.Mount(local_dir="~/Documents/projects/tcvc-modal/videos", remote_dir="/data2/yhliu/old_film")],
                  image=setup_image.conda()
                  #    .conda_install(["cudatoolkit=10.2", "cudnn=7.6.5"])
                  .pip_install_from_requirements("./TCVC/codes/requirements.txt")
                  .run_commands([
                      'apt-get update',
                      'apt-get install git -y'])
                  .run_commands([
                      'conda install -c conda-forge -y cudatoolkit=10.2 cudnn=7.6.5',
                      'git clone --recursive https://github.com/Divide-By-0/tcvc-modal',
                  ])
                  .run_commands([
                      'cd tcvc-modal && git clone https://github.com/Divide-By-0/TCVC-Temporally-Consistent-Video-Colorization',
                  ])
                  .run_commands([
                      'mv tcvc-modal/TCVC-Temporally-Consistent-Video-Colorization tcvc-modal/TCVC',
                      'python tcvc-modal/TCVC/codes/models/archs/networks/channelnorm_package/setup.py develop',
                      'python tcvc-modal/TCVC/codes/models/archs/networks/correlation_package/setup.py develop',
                      'python tcvc-modal/TCVC/codes/models/archs/networks/resample2d_package/setup.py develop',
                      'python tcvc-modal/TCVC/codes/test_TCVC_onesampling_noGT.py',
                      #   'export PYTHONPATH=.'
                      # "gdown 'https://drive.google.com/uc?id=1876eGDhyKhc2rx2X-A_FffB3ZX2FXTOc'" # Get video
                  ],),
                  secret=modal.Secret.from_name("CUDA_HOME")
                  #    shared_volumes={CACHE_PATH: volume},
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
