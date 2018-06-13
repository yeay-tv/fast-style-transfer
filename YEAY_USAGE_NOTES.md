# Yeay Usage and Installation Notes

## Preface

[pending] The license for this requires permission from the author for non-research related use.  Since we never put this into production, an inquiry to the author has not yet been made.

## Setup

You should follow the directions to get Detectron running.  We will assume you have done that and install only the additional libraries and datasets that are needed.

### 0) Activate Conda environment
  - `conda activate mlpy2`

### 1) Clone Yeay's version of [fast-style-transfer](https://github.com/lengstrom/fast-style-transfer) implementation
  - clone into ~/repos. `cd ~/repos && git clone https://github.com/yeay-tv/fast-style-transfer.git && cd fast-style-transfer`

### 2) Install requirements
  - make sure your conda environment is activated `conda activate mlpy2`
  - install tensorflow gpu `pip install --upgrade tensorflow-gpu`.  The Tensorflow install instructions are more confusing than helpful, but they are [here](https://www.tensorflow.org/install/install_linux) if you need them
  - make sure ffmpeg is installed `conda install ffmpeg`  (you can also install this systemwide but Ubuntu's ffmpeg tends to not get update very often).

### 3) Run setup.sh `./setup.sh`
  - the joan miro style network can be found [here](https://drive.google.com/drive/u/0/folders/16PwqT3hvSAnVUjk8NHJJnUeEpwPSDVD6)

### 4) Inference on videos
  - if you are on the server that I have already created, you can run the following command
  - `python transform_video.py --in-path ~/datasets/dummy/video/trim_test_vid.mp4 \
    --checkpoint chkpts/joan_miro \
    --out-path /tmp/trim_test_vid_joan_miro.mp4 \
    --device /gpu:0 \
    --batch-size 4`

### 4) [Optional]  If you want to train more models, you will need to download the COCO 2014 train dataset.
  - make approriate dirs in the repo folder and in our datasets folder.  `mkdir -p ~/datasets/COCO && cd ~/datasets/COCO`
  - download the dataset `wget http://images.cocodataset.org/zips/train2014.zip` and unzip it
  - move back into the repo and symlink this folder `cd ~/repos/fast-style-transfer/data && ln -s /home/ubuntu/datasets/COCO/train2014 train2014`
  - follow the repo's instructions as normal.

## Notes

Training a new network took approximately 11 hours on a K80 using the settings in the sample from the repo's docs.
