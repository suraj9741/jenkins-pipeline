### install single node k8s with help of rancher
docker run -d --restart=unless-stopped -p 80:80 -p 443:443 -p 30038:30038 -p 30042:30042 --privileged rancher/rancher:latest

### docker build command
docker build -t suraj9741/koko:1 .

### application
docker run -p 8080:5000 -d suraj9741/koko:1