FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir -p /home/doc-bd-a1/

COPY Israel-Palestine.csv /home/doc-bd-a1/

CMD ["/bin/bash"]