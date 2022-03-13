# This is a dockerfile to build the sphinx stuff
# and upload it to somewhere

# Docker quick reference:
# Build image: sudo docker build -t svek/sphinx-full  .
# Run sth:     sudo docker run -it  svek/sphinx-full bash
# Register for uploading: sudo docker login -- or cp /root/.docker/config.json from some machine
# Upload:      sudo docker push svek/sphinx-full
# You can see the image then at https://hub.docker.com/u/svek

FROM sphinxdoc/sphinx-latexpdf

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        git \
        rsync \
        ssh \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /docs
ADD requirements.txt /docs
RUN pip3 install -r requirements.txt
