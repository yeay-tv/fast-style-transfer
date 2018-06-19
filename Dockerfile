FROM tensorflow/tensorflow:1.8.0-gpu-py3

RUN add-apt-repository ppa:jonathonf/ffmpeg-3 && apt update && apt install -y ffmpeg libav-tools x264 x265 git wget nano

RUN pip install moviepy scipy

RUN git clone https://github.com/yeay-tv/fast-style-transfer.git /fast-style-transfer

WORKDIR /fast-style-transfer

RUN ./setup.sh
RUN wget https://s3.us-east-2.amazonaws.com/yeay-ml-data-us/fast-style-transfer/chkpts.tar.gz && tar xzvf chkpts.tar.gz

# nvidia-docker run --rm -it yeay-fast-style-transfer python transform_video.py --in-path examples/content/fox.mp4 --checkpoint chkpts/joan_miro --out-path /tmp/fox.mp4 --device /gpu:0 --batch-size 4
