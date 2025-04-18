# AI Text Similarity Microservice

This Flask-based microservice provides an API to compute similarity between two text prompts using different methods (e.g., cosine, jaccard). It can also interact with a simulated LLM component.

---

## 🚀 Features

- Cosine similarity using TF-IDF
- Jaccard similarity using token set
- Clean input via sanitization pipeline
- LLM placeholder for advanced text analysis
- Logging and test coverage
- Containerized with Docker
- Load testing with Locust

---

## 🛠️ Development Setup

### 1. Clone the repo
```bash
git clone <repo-url>
cd ai_text_similarity_service
```
2. Create virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

🐳 Docker Support
```bash
docker build -t text-similarity-service .
docker run -p 5000:5000 text-similarity-service
```

Sample curl:

```bash
curl -X POST http://127.0.0.1:5000/analyze \
     -H "Content-Type: application/json" \
     -d '{"prompt1": "Hello world", "prompt2": "Hello again", "method": "cosine"}'
```

🧪 Running Tests
```bash
# Run unit tests
python -m unittest tests/

# Run integration tests
python -m unittest tests/test_integration.py
```


⚙️ Load Testing with Locust
```bash
pip install locust
locust -f .\loadtesting.py --host=http://127.0.0.1:5000
```

📂 Project Structure
```bash
ai_text_similarity_service/
│
├── app.py                  # Flask app factory
├── run.py                  # App entry point
├── analyze.py              # /analyze route
├── llm_handler.py          # LLM mock interaction
├── text_sanitization.py    # Tokenization and filtering
├── similarity.py           # Cosine/Jaccard logic
├── logs/                   # Log directory
├── tests/                  # Unit and integration tests
├── Dockerfile              # Container definition
├── requirements.txt
└── README.md
```

🚀 Deployment Process
1. Containerization with Docker
  Build the Docker image.
  Run the Docker container.
  This approach ensures consistency across different environments and simplifies deployment.

2. Production Deployment Options
   
  a. Gunicorn with Nginx
    Set up Nginx as a reverse proxy to handle client requests and serve static files efficiently.
    This setup enhances performance and provides better handling of concurrent requests.
  b. Cloud Deployment with Docker
    Push your Docker image to a container registry like Docker Hub or AWS ECR.
    Deploy using orchestration tools such as:
      AWS ECS/Fargate: For serverless container deployment.
      Kubernetes: For managing containerized applications at scale.
      Azure Container Instances: For quick deployment without managing servers.
    
  These platforms offer scalability, load balancing, and easy management of your application.

📈 Scaling Considerations
1. Horizontal Scaling
  Add more instances of your application to handle increased load.
  Use a load balancer (e.g., Nginx, AWS ALB) to distribute traffic evenly across instances.
  This method improves availability and ensures your application can handle more users.

2. Asynchronous Task Processing
  Integrate Celery with a message broker like Redis or RabbitMQ to handle long-running tasks asynchronously.
  This prevents blocking the main application thread and improves responsiveness.

3. Caching
  Implement caching mechanisms (e.g., Redis) to store frequently accessed data.
  Reduces database load and speeds up response times.

4. Monitoring and Logging
  Set up monitoring tools (e.g., Prometheus, Grafana) to track application performance.
  Implement centralized logging (e.g., ELK Stack) to collect and analyze logs from all instances.
  Monitoring helps in proactive issue detection and maintaining application health.

5. Security and Configuration Management
  Use environment variables to manage configuration and sensitive information.
  Implement HTTPS to secure data in transit.
  Regularly update dependencies to patch security vulnerabilities.  
  Proper security measures protect your application and user data.

By following these deployment and scaling strategies, your Flask-based AI Text Similarity Service will be well-equipped to handle production workloads efficiently and securely.






