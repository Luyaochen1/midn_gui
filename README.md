1. the docker images have been commited to dockerhub
    
   
2. run server

    sudo docker run  -it -d -p ssss:80 --name=midn_server luyaochen/midn_server
      where ssss is the server GUI port exposed to external network

3. run remote 
  
    sudo docker run  -it -d -p remote_port_1:80 --name=midn_remote_1 luyaochen/midn_remote
      where remote_port_1 is the remote server 1 GUI port exposed to external network
    
    sudo docker run  -it -d -p remote_port_2:80 --name=midn_remote_2 luyaochen/midn_remote 
      where remote_port_2 is the remote server 2 GUI port exposed to external network

~~ the below demo URL assumes that the remote and central docker container running on the same host

 4. Access central server
    http://cental_ip:central_port/start_midn.sh/             -- the ending "/" is a must
      where central_ip is the host running the docker ( not the IP of central container)   
      
 6. Access remote server
    http://remote_ip:remote_port/start_midn.sh/ 
      where temote_ip is the host running the docker ( not the IP of remote container)
    
    change and save the defaul setup on remote server
    - update the site name
    - update the central server app url:
      eg, if you get "Central Host IP address: 172.17.0.26" on central server, setup http://172.17.0.26  on all remote sites

