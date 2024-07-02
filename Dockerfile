FROM ubuntu:22.04

WORKDIR /usr/src/mergebot
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y apt-utils python3 python3-pip git \
    p7zip-full p7zip-rar xz-utils wget curl pv jq \
    ffmpeg unzip neofetch mediainfo

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x start.sh
CMD ["bash","start.sh"]
