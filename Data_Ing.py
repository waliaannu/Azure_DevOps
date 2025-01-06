from azure.storage.blob import BlobServiceClient

# Azure Blob Storage connection
connection_string = "your_connection_string"
container_name = "health-claims"

# Initialize Blob Service Client
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Upload a file
file_path = "claims_data.csv"  # Local file
blob_name = "raw/claims_data.csv"  # Destination in Azure

with open(file_path, "rb") as data:
    container_client.upload_blob(blob_name, data)
print(f"File {file_path} uploaded to Azure Blob Storage.")
