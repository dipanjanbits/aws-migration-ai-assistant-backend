from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

import boto3
import json

app = FastAPI(
    title="AWS Cloud Migration AI Assistant Backend",
    description="Backend service for AWS Cloud Migration AI Assistant",
    version="0.0.1"
)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Create Lambda client (credentials come from IAM role or env variables)
lambda_client = boto3.client("lambda", region_name="us-east-1")


@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "FastAPI service is healthy"}


@app.get("/aws_health")
async def call_lambda(name: str = "Guest"):
    # Simulate API Gateway event structure for GET
    event = {
        "queryStringParameters": {"name": name}
    }

    response = lambda_client.invoke(
        FunctionName="lmd-use1-awscmai-aws-health",  # replace with your Lambda name/ARN
        InvocationType="RequestResponse",
        Payload=json.dumps(event),
    )

    payload = json.loads(response["Payload"].read().decode("utf-8"))
    body = json.loads(payload["body"])  # extract message from Lambda response

    return {"lambda_result": body}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)