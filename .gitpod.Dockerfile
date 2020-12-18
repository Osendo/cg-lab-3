FROM gitpod/workspace-full

RUN sudo apt-get install -y libgl1-mesa-dev

RUN pip install numpy scipy opencv-python numba
