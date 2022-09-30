import modal

setup_image = modal.Image.debian_slim()
stub = modal.Stub()

volume = modal.SharedVolume().persist("tcvc-repo-vol")
CACHE_PATH = "~/Documents/projects/tcvc-modal"

@stub.function(mounts=[modal.Mount(local_dir="~/Documents/projects/tcvc-modal/", remote_dir="~/project"),
                       modal.Mount(local_dir="~/Documents/projects/tcvc-modal/videos", remote_dir="/data2/yhliu/old_film")],
               image=setup_image.conda()
               .conda_install(["cudatoolkit=10.2", "cudnn=7.6.5"])
               .pip_install_from_requirements("./TCVC/codes/requirements.txt")
               .run_commands([
                    'apt-get update',
                    'apt-get install git -y'])
               .run_commands([
                    'git clone --recursive https://github.com/Divide-By-0/tcvc-modal',
                    'cd tcvc-modal && git clone https://github.com/Divide-By-0/TCVC-Temporally-Consistent-Video-Colorization',
                    'ls',
                    'cd ~/project/TCVC/codes/models/archs/networks/channelnorm_package/',
                    'python setup.py develop',
                    'cd ~/project/TCVC/codes/models/archs/networks/correlation_package/',
                    'python setup.py develop',
                    'cd ~/project/TCVC/codes/models/archs/networks/resample2d_package/',
                    'python setup.py develop',
                    'cd ~/project/TCVC/codes/',
                    'python test_TCVC_onesampling_noGT.py',
                    'export PYTHONPATH=~project/TCVC/codes'
                    # "gdown 'https://drive.google.com/uc?id=1876eGDhyKhc2rx2X-A_FffB3ZX2FXTOc'" # Get video
                    ],
                ),
               shared_volumes={CACHE_PATH: volume},
               gpu=True)
def square(x):
    print("This code is running on a remote worker!")
    return x**2


if __name__ == "__main__":
    with stub.run():
        print("the square is", square(42))

# def download_file(url):
    # import gdown
    # url = 'https: //drive.google.com/uc? id $=0$ B9P 1L--7Wd2vNm9zMTJWOGxobkU'
    # output = '20150428_collected_images.tgz'
    # gdown. download(url, output, quiet=False)
    # $\mathrm{md} 5=$ 'fa837a88f0c40c513d975104edf3da17'
    # gdown. cached_download(url, output, md5=md5, postprocess=gdown. extractall)

