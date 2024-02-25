# Use Debian as base image
FROM debian:bookworm-slim

# The name of the Conda environment to create
ARG CONDA_ENV_NAME=myenv
ENV CONDA_ENV_NAME=${CONDA_ENV_NAME}

# The version of Node.js to install
ARG NODE_VERSION=20

# Set the PYTHONPATH
ENV PYTHONPATH=/app:/app/jupyter:/app/jupyter/lib:$PYTHONPATH

# Install git, wget, supervisor, etc.
RUN apt-get update \
    && mkdir -p /etc/apt/keyrings \
    && apt-get install -y gnupg wget curl zip unzip git supervisor sqlite3 fswatch

# Set the working directory to /app
WORKDIR /app

# Install Miniforge in /opt/conda
RUN wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O /tmp/miniforge.sh \
    && bash /tmp/miniforge.sh -b -p /opt/conda \
    && rm /tmp/miniforge.sh

# Update Mamba
RUN /opt/conda/bin/mamba update -n base -c defaults mamba

# Add Miniforge to PATH
ENV PATH="/opt/conda/bin:$PATH"

# Copy the environment.yml file from your host to the current location in the container (i.e., /app)
COPY environment.yml .

# Create Mamba environment
RUN mamba env create -f environment.yml

# Initialize Conda
RUN mamba init bash

# Activate environment when opening a terminal
RUN echo "mamba activate ${CONDA_ENV_NAME}" >> ~/.bashrc

# Install node, npm, yarn, bun
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_VERSION.x nodistro main" > /etc/apt/sources.list.d/nodesource.list \
    && apt-get update \
    && apt-get install -y nodejs \
    && npm install -g npm \
    && npm install -g pnpm \
    && npm install -g bun \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | tee /etc/apt/keyrings/yarn.gpg >/dev/null \
    && echo "deb [signed-by=/etc/apt/keyrings/yarn.gpg] https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list \
    && apt-get install -y yarn

# supervisord
COPY ./docker/development/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Set the entrypoint to supervisord
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
