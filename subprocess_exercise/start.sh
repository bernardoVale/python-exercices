
# Start basic ubuntu container with base dependencies

docker run -it --cap-add SYS_PTRACE --rm -p 8080:8080 -v "$PWD:/code" python-ubuntu

# Start container with all dependencies installed
docker run -it --cap-add SYS_PTRACE --rm -p 8080:8080 -v "$PWD:/code" python-ubuntu:deps
