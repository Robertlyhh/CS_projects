# filepath: /C:/Users/rober/OneDrive/Desktop/university_study/CS_projects/rubbber_duck_detection/Dockerfile
FROM pytorch/torchserve:latest

# Copy the model archive to the model store
COPY model_store/rubber_duck.mar /home/model-server/model-store/

# Expose the ports
EXPOSE 8080 8081

# Run TorchServe
CMD ["torchserve", "--start", "--model-store", "/home/model-server/model-store", "--models", "rubber_duck=rubber_duck.mar"]