# Use a base image with Python, for example
FROM python:3.9-alpine

# Create a directory to store your files inside the container
WORKDIR /home/data

# Copy your local files into the container
COPY IF.txt Limerick-1.txt read_files.py /home/data/

# Create the output directory
RUN mkdir -p /home/output

# Run the script
CMD ["python", "read_files.py"]
