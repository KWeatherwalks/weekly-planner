# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install cairo
RUN apt-get update && apt-get install -y \
    pkg-config \
    libcairo2-dev \
    libgirepository1.0-dev \
    python-cairo

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /planner
COPY . /planner

EXPOSE 5000

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /planner
USER appuser

# Create a volume for bind mount 
# to create bind mount, add following flag to docker run command:   -v ${PWD}:/planner
VOLUME [ "/planner/python-modules" ]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "planner:app"]
