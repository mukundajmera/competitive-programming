# Deployment Guide

## Prerequisites

- Docker 20.10+
- Docker Compose 2.0+
- Kubernetes 1.25+ (for production)
- Helm 3.0+ (optional)

## Local Development

### Using Python Virtual Environment

1. **Setup environment**:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Configure environment**:
```bash
cp .env.example .env
# Edit .env with your settings
```

3. **Initialize database**:
```bash
./scripts/init_db.sh
```

4. **Run development server**:
```bash
./scripts/run_dev.sh
# Or directly:
uvicorn app.main:app --reload
```

### Using Docker Compose

1. **Start all services**:
```bash
docker-compose up -d
```

2. **Check logs**:
```bash
docker-compose logs -f api
```

3. **Access services**:
- API: http://localhost:8000
- Docs: http://localhost:8000/api/v1/docs
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090
- Flower: http://localhost:5555

4. **Stop services**:
```bash
docker-compose down
```

## Production Deployment

### Docker Deployment

1. **Build production image**:
```bash
docker build -t ai-content-platform:latest .
```

2. **Run with environment variables**:
```bash
docker run -d \
  -p 8000:8000 \
  -e DATABASE_URL="postgresql+asyncpg://..." \
  -e REDIS_URL="redis://..." \
  -e OPENAI_API_KEY="sk-..." \
  --name ai-platform \
  ai-content-platform:latest
```

### Kubernetes Deployment

1. **Create namespace**:
```bash
kubectl create namespace ai-platform
```

2. **Create secrets**:
```bash
kubectl create secret generic api-secrets \
  --from-literal=SECRET_KEY="your-secret-key" \
  --from-literal=OPENAI_API_KEY="sk-..." \
  --from-literal=ANTHROPIC_API_KEY="sk-ant-..." \
  -n ai-platform
```

3. **Apply configurations**:
```bash
kubectl apply -f k8s/ -n ai-platform
```

4. **Check deployment status**:
```bash
kubectl get pods -n ai-platform
kubectl logs -f deployment/api -n ai-platform
```

### AWS Deployment

#### Using ECS (Elastic Container Service)

1. **Push image to ECR**:
```bash
aws ecr create-repository --repository-name ai-content-platform
docker tag ai-content-platform:latest <account-id>.dkr.ecr.<region>.amazonaws.com/ai-content-platform:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/ai-content-platform:latest
```

2. **Create task definition** (ECS task definition JSON)

3. **Create service** (ECS service with load balancer)

#### Using EKS (Elastic Kubernetes Service)

1. **Create EKS cluster**:
```bash
eksctl create cluster --name ai-platform-cluster --region us-west-2
```

2. **Configure kubectl**:
```bash
aws eks update-kubeconfig --name ai-platform-cluster --region us-west-2
```

3. **Deploy application**:
```bash
kubectl apply -f k8s/
```

### GCP Deployment

#### Using Google Kubernetes Engine (GKE)

1. **Create GKE cluster**:
```bash
gcloud container clusters create ai-platform-cluster \
  --zone us-central1-a \
  --num-nodes 3
```

2. **Get credentials**:
```bash
gcloud container clusters get-credentials ai-platform-cluster
```

3. **Deploy application**:
```bash
kubectl apply -f k8s/
```

### Azure Deployment

#### Using Azure Container Instances

1. **Create resource group**:
```bash
az group create --name ai-platform-rg --location eastus
```

2. **Create container**:
```bash
az container create \
  --resource-group ai-platform-rg \
  --name ai-platform \
  --image ai-content-platform:latest \
  --dns-name-label ai-platform \
  --ports 8000
```

## Environment Configuration

### Production Environment Variables

```env
# Application
APP_NAME=AI Content Platform
ENVIRONMENT=production
DEBUG=false

# Security
SECRET_KEY=<strong-random-key>
ALGORITHM=HS256

# Database
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/db
DATABASE_POOL_SIZE=50
DATABASE_MAX_OVERFLOW=100

# Redis
REDIS_URL=redis://host:6379/0
REDIS_CACHE_TTL=3600

# AI Providers (use secrets management)
OPENAI_API_KEY=<from-secrets>
ANTHROPIC_API_KEY=<from-secrets>

# CORS
BACKEND_CORS_ORIGINS=["https://yourdomain.com"]

# Monitoring
PROMETHEUS_ENABLED=true
LOG_LEVEL=INFO
```

## Database Setup

### PostgreSQL Setup

1. **Create database**:
```sql
CREATE DATABASE ai_content_platform;
CREATE USER ai_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE ai_content_platform TO ai_user;
```

2. **Run migrations**:
```bash
alembic upgrade head
```

3. **Create indexes** (for performance):
```sql
CREATE INDEX idx_contents_owner ON contents(owner_id);
CREATE INDEX idx_contents_project ON contents(project_id);
CREATE INDEX idx_content_versions_content ON content_versions(content_id);
```

### Database Backup

```bash
# Backup
pg_dump -U ai_user ai_content_platform > backup_$(date +%Y%m%d).sql

# Restore
psql -U ai_user ai_content_platform < backup_20240101.sql
```

## Redis Setup

### Redis Configuration

```conf
# redis.conf
maxmemory 2gb
maxmemory-policy allkeys-lru
save 900 1
save 300 10
save 60 10000
```

## Load Balancer Setup

### Nginx Configuration

```nginx
upstream api_servers {
    least_conn;
    server api1:8000;
    server api2:8000;
    server api3:8000;
}

server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://api_servers;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /ws/ {
        proxy_pass http://api_servers;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

## SSL/TLS Setup

### Using Let's Encrypt with Certbot

```bash
certbot --nginx -d api.yourdomain.com
```

## Monitoring Setup

### Prometheus Configuration

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'fastapi'
    static_configs:
      - targets: ['api:8000']
```

### Grafana Dashboards

Import dashboards:
- FastAPI Dashboard (ID: 14291)
- PostgreSQL Dashboard (ID: 9628)
- Redis Dashboard (ID: 11835)

## Scaling

### Horizontal Pod Autoscaler (HPA)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### Database Read Replicas

Configure read replicas for PostgreSQL to distribute read load.

## Health Checks

### Kubernetes Health Probes

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 5
  periodSeconds: 5
```

## Backup Strategy

### Automated Backups

```bash
# Cron job for daily backups
0 2 * * * /usr/local/bin/backup_database.sh
```

### Disaster Recovery

1. Regular database backups
2. Configuration backups
3. Documented recovery procedures
4. Regular DR testing

## Security Hardening

### Production Checklist

- [ ] Use strong SECRET_KEY
- [ ] Enable HTTPS/TLS
- [ ] Configure CORS properly
- [ ] Set up firewall rules
- [ ] Use secrets management (AWS Secrets Manager, etc.)
- [ ] Enable rate limiting
- [ ] Set up monitoring and alerting
- [ ] Regular security audits
- [ ] Keep dependencies updated
- [ ] Use non-root container user

## Troubleshooting

### Common Issues

1. **Database connection errors**
   - Check connection string
   - Verify network connectivity
   - Check database credentials

2. **Redis connection errors**
   - Verify Redis is running
   - Check Redis URL
   - Check firewall rules

3. **High memory usage**
   - Check for memory leaks
   - Adjust worker count
   - Enable caching properly

4. **Slow API responses**
   - Check database queries
   - Enable caching
   - Scale horizontally

## Maintenance

### Regular Tasks

- Update dependencies monthly
- Review and optimize database queries
- Clean up old logs
- Monitor resource usage
- Review security alerts
- Update documentation

## Support

For deployment issues:
- GitHub Issues
- Email: devops@example.com
