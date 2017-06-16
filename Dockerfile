# ------------------------------------------------------------------------------- 
# METADATA
# ------------------------------------------------------------------------------- 
FROM ubuntu:latest
MAINTAINER "dmsurti@gmail.com"

# ------------------------------------------------------------------------------- 
# Install basic dependencies
# ------------------------------------------------------------------------------- 
RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties
RUN apt-get install -y wget curl bzip2 git

# ------------------------------------------------------------------------------- 
# Install blender
# ------------------------------------------------------------------------------- 
RUN apt-get install -y blender

# ------------------------------------------------------------------------------- 
# Add repository to install openfoam4
# ------------------------------------------------------------------------------- 
RUN add-apt-repository http://dl.openfoam.org/ubuntu
RUN sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"

# ------------------------------------------------------------------------------- 
# SEE:https://github.com/ludwigprager/docker-openfoam4/blob/master/Dockerfile#L13
# ------------------------------------------------------------------------------- 
RUN apt-get install apt-transport-https

# ------------------------------------------------------------------------------- 
# Install openfoam4
# ------------------------------------------------------------------------------- 
RUN apt-get update 
RUN apt-get -y install openfoam4
RUN apt-get -y install mlocate

# ------------------------------------------------------------------------------- 
# Clone reynolds, if updated
# ------------------------------------------------------------------------------- 
ADD https://api.github.com/repos/dmsurti/reynolds/git/refs/heads/master version.json
RUN git clone https://github.com/dmsurti/reynolds.git 

# ------------------------------------------------------------------------------- 
# Clone reynolds-blender, if updated
# ------------------------------------------------------------------------------- 
ADD https://api.github.com/repos/dmsurti/reynolds-blender/git/refs/heads/master version.json
RUN git clone https://github.com/dmsurti/reynolds-blender.git 

# ------------------------------------------------------------------------------- 
# Install reynolds in blender's python3.5m
# ------------------------------------------------------------------------------- 
RUN cd /reynolds && python3.5m setup.py install

# ------------------------------------------------------------------------------- 
# Start BLENDER!
# TODO: INSTALL reynolds-blender addon, right now done manually
# ------------------------------------------------------------------------------- 
ENTRYPOINT ["blender"]
