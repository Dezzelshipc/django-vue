# django-vue

# Installation

## Install docker

### Windows
Run ```wsl --install``` in powershell with admin privileges

Download Docker from official website and follow instructions: [link](https://docs.docker.com/desktop/windows/install/)


## Starting
Clone repository using [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
```
git clone https://github.com/Dezzelshipc/django-vue
cd django-vue
```

And start all containers using ```docker-compose```
```
docker-compose up
```
Add ```-d``` option to run docker in background

# Docker commands
Run using ```docker-compose```
```
docker-compose up
```

Stop all containers
```
docker-compose stop
```

Rebuild all containers
```
docker compose up --build
```

Or you can rebuild a single container:
```
docker-compose up --build [container-name]
```

#### Container names
- frontend
- web
- celery (tba)