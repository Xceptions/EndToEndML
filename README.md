An end to end ML pipeline

To run

1. Because we are using two distinct ports (one for the site layout, one for API calls), we must tell k3d to map both external ports when creating the cluster. Build both images locally:

```bash
   docker build -t my-flask-backend:latest ./backend
   docker build -t my-html-frontend:latest ./frontend
```

Create the K3d Cluster exposing two ports:
Port 8080 maps to the frontend service (Nginx).
Port 8081 maps to the backend service (Flask).

'''bash
    k3d cluster create mycluster -p "8080:80@loadbalancer" -p "8081:5000@loadbalancer"
'''

Import images directly into k3d using imagePullPolicy:

'''bash
    k3d image import my-flask-backend:latest my-html-frontend:latest -c mycluster
'''

Deploy:

'''bash
    kubectl apply -f k8s/
'''

Navigate to http://localhost:8080 for frontend and port 8081 for querying backend.