# Use official Python slim image for a smaller footprint
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && apt-get clean

# Copy the Python requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data (stopwords, punkt tokenizer)
ENV NLTK_DATA=/usr/local/nltk_data
RUN mkdir -p $NLTK_DATA && \
    python -c "import nltk; nltk.download('punkt', download_dir='$NLTK_DATA'); nltk.download('stopwords', download_dir='$NLTK_DATA')"


# Create a logs directory in case it's not already there
RUN mkdir -p instance/logs

# Copy the full project into the container
COPY . .

# Expose the port the Flask app will run on
EXPOSE 5000

# Run the Flask app via run.py
CMD ["python", "run.py"]
