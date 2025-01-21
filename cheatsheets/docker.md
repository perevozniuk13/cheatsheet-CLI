# Docker Cheat Sheet

## GENERAL COMMANDS
| Command | Description |
|---------|-------------|
| `docker -d` | Start the docker daemon |
| `docker --help` | Get help with Docker. Can also use --help on all subcommands |
| `docker info` | Display system-wide information |

## IMAGES
Docker images are a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings.

| Command | Description |
|---------|-------------|
| `docker build -t <image_name> .` | Build an Image from a Dockerfile |
| `docker build -t <image_name> . --no-cache` | Build an Image from a Dockerfile without the cache |
| `docker images` | List local images |
| `docker rmi <image_name>` | Delete an Image |
| `docker image prune` | Remove all unused images |

## CONTAINERS
A container is a runtime instance of a Docker image. A container will always run the same, regardless of the infrastructure. Containers isolate software from its environment and ensure that it works uniformly despite differences, for instance, between development and staging.

| Command | Description |
|---------|-------------|
| `docker run --name <container_name> <image_name>` | Create and run a container from an image, with a custom name |
| `docker run -p <host_port>:<container_port> <image_name>` | Run a container and publish a container’s port(s) to the host |
| `docker run -d <image_name>` | Run a container in the background |
| `docker start <container_name>` or `docker stop <container_name>` | Start or stop an existing container |
| `docker rm <container_name>` | Remove a stopped container |
| `docker exec -it <container_name> sh` | Open a shell inside a running container |
| `docker logs -f <container_name>` | Fetch and follow the logs of a container |
| `docker inspect <container_name>` or `docker inspect <container_id>` | Inspect a running container |
| `docker ps` | List currently running containers |
| `docker ps --all` | List all Docker containers (running and stopped) |
| `docker container stats` | View resource usage stats |