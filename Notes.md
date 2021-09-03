# NGINX
[Tutorial Link](https://www.digitalocean.com/community/tutorials/understanding-nginx-http-proxying-load-balancing-buffering-and-caching)

## Briefly:

nginx is used as a reversed proxy to redirect client requests to backend servers.  
Using 
```
upstream backend {
    server backend1.example.com weight=5;
    server 127.0.0.1:8080       max_fails=3 fail_timeout=30s;
    server unix:/tmp/backend3;

    server backup1.example.com  backup;
}
```
Where weight=5 indicates that backend1 server would recieve 5 times more redirects than other servers
Servers where we are proxying can also be specified as docker container names with associated exposed ports.    
**WARNING!**    
*Docker container should run on the same host as its name, because each container has its own localhost and shared named hosts*

```
server {
  listen        80;
  server_name   localhost;

  location /api {
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For    $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Host $http_host;
    proxy_set_header X-NginX-Proxy true;
    proxy_redirect off;
    # Attention! api server should be exposed at api host, not localhost!!
    proxy_pass  http://api:4000;
  }
  
}
```
## Example NGINX file
```
server {
  listen        80;
  server_name   localhost;

  location /api {
    # Attention! api server should be exposed at api host, not localhost!!
    proxy_pass  http://api:4000;
  }
  location /api2 {

    # Attention! api server should be exposed at api host, not localhost!!
    proxy_pass  http://api2:4000;
  }
}

```
**Warning!**    
*Don't use the same ports, because it becomes a mess when scaling :)*

# DOCKER-COMPOSE
[Stack Answer](https://stackoverflow.com/questions/40801772/what-is-the-difference-between-docker-compose-ports-vs-expose)   
First of all we need to define what are EXPOSE and PORTS parameters:    
- **EXPOSE** - Expose ports without publishing them to the host machine - they’ll only be accessible to linked services. Only the internal port can be specified.    
**In recent versions of Dockerfile, EXPOSE doesn't have any operational impact anymore, it is just informative. (see also)**
- **PORTS** - Ports will be exposed to the host machine to a random port or a given port. Ports mentioned in docker-compose.yml will be shared among different services started by the docker-compose.

So to sum up, you can (but not obligated) define exposed ports to inner docker-compose network. If you want to connect with outer network (machine running docker), you need to use ports to redirect outer port to inner docker port.   

For example this maps outer 3305 to docker 3306:
```
mysql:
  image: mysql:5.7
  ports:
    - "3305:3306"
```

## Example dockerr-compose
```
version: "2.1"

services: 
  api:
    build: ./api
    container_name: api
    restart: always
  api2:
    build: ./api2
    container_name: api2
    restart: always
  nginx2:
    build: ./nginx
    container_name: nginx2
    restart: always
    ports: 
      - "80:80"

```

# GIT LFS
## Handling large files using git

### Installation LINUX
- `curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash`
- `sudo apt-get install git-lfs`
- `git lfs install`

### Adding large files
- `git lfs track file_path` - to track large file
- then just normally commit it and use git :)

# Docker-Compose Linux installation
[Official Docs](https://docs.docker.com/compose/install/)

# Network problems with Docker-compose
[Address already in use](https://stackoverflow.com/questions/37971961/docker-error-bind-address-already-in-use)


# Screen Linux 
Helps to control the sessions and keep processes running even after exiting the terminal
## Usage
- `screen` - to run a new screen session
- `ctrl + a + d` - to detach from session
- `screen -ls` - to view all screen sessions and their id's
- `screen -r {<session_id>}` - to attach to runnning screen session/ or without id if you have only one running
- `ctrl + a + k and type yes` - to kill running screen session
- `screen -XS <session-id> quit` - another option to kill running screen session

# Memory and CPU Stats Linux
- `df -h` - disk space usage
- `free -m` - RAM usage


# TODOS
- Can't find a way to initialize a script inside docker that would control the data inserting and building of elastic, so by now it should be done manually