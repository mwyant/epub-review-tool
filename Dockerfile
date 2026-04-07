FROM python:3.11-slim

WORKDIR /app

# Install cryptography for self-signed cert generation
RUN pip install cryptography

# Copy the player, server script, and cert generator
COPY index.html .
COPY server.py .
COPY generate_cert.py .

# Generate self-signed certs
RUN python generate_cert.py

EXPOSE 8002

# Run the custom server script
CMD ["python", "server.py"]
