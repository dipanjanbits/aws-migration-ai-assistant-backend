# AWS Cloud Migration AI Assistant Backend

A FastAPI-based backend service that interfaces with AWS Lambda to provide AI-assisted cloud migration recommendations and health checks.

## Features

- AWS Lambda Integration for Cloud Migration Analysis
- AWS Cognito Authentication
- RESTful API Endpoints
- CORS Support
- Swagger/OpenAPI Documentation
- Health Monitoring

## Prerequisites

- Python 3.8+
- AWS Account with configured credentials
- AWS Cognito User Pool
- AWS Lambda Function(s)

## Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/dipanjanbits/aws-migration-ai-assistant-backend.git
cd aws-migration-ai-assistant-backend
```

2. **Set up Python virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
Create a `.env` file in the root directory with the following:
```env
AWS_REGION=us-east-1
JWT_ISSUER=https://cognito-idp.us-east-1.amazonaws.com/us-east-1_e7Lr8DWuw
JWT_AUDIENCE=your-app-client-id
JWKS_URL=https://cognito-idp.us-east-1.amazonaws.com/us-east-1_e7Lr8DWuw/.well-known/jwks.json
```

5. **Start the server:**
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Public Endpoints

- `GET /health` - Service health check
- `GET /aws_health` - AWS Lambda integration health check

### Protected Endpoints (Require Authentication)

- `GET /protected-health` - Protected health check endpoint

## Authentication

The service uses AWS Cognito for authentication. To access protected endpoints:

1. Obtain a JWT token from your Cognito User Pool
2. Include the token in API requests:
```bash
curl -H "Authorization: Bearer <your-cognito-token>" http://localhost:8000/protected-health
```

## API Documentation

Once the server is running, access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Dependencies

- FastAPI - Modern web framework for building APIs
- Uvicorn - ASGI server implementation
- Boto3 - AWS SDK for Python
- Python-dotenv - Environment variable management
- PyJWT - JWT token handling
- Requests - HTTP library

## Project Structure

```
aws-migration-ai-assistant-backend/
├── main.py              # FastAPI application and route handlers
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (create this)
└── README.md           # This file
```

## Development

To run in development mode with auto-reload:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Error Handling

The API uses standard HTTP status codes:
- 200: Success
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Support

For support, please open an issue in the GitHub repository.
