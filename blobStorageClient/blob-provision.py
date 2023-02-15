import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


#  Main Goal : 
# Write a script that will create, upload, and copy 100 blobs from Storage account A to B, execute it on the server you created earlier using CD pipeline.

'''
Blob storage offers three types of resources:

The storage account
A container in the storage account
A blob in the container

BlobServiceClient: The BlobServiceClient class allows you to manipulate Azure Storage resources and blob containers.
ContainerClient: The ContainerClient class allows you to manipulate Azure Storage containers and their blobs.
BlobClient: The BlobClient class allows you to manipulate Azure Storage blobs.


You can also authorize requests to Azure Blob Storage by using the account access key
'''


account_name = 'sa1norm2gkl5vfjm'
account_key = 'sR4ddgOttORIVNqRDxvQqF+XIRKs3Fs7GyhM4u4ct4ErKX7POMZh43KPIT4jH/6r+ctPCUCPFdo6+AStGcMNsw=='
container_name = 'main'

connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + account_name + ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net'




try:
    print("Azure Blob Storage Python Client")
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # container_client = blob_service_client.get_container_client(container_name)
    


    # 
    local_path = "./files"
    local_file_name = "file1.tgz"
    upload_file_path = os.path.join(local_path, local_file_name)

    blob_client = blob_service_client.get_blob_client(container=container_name,blob=local_file_name)
    print(dir(blob_client))

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(file=upload_file_path, mode="rb") as data:
        blob_client.upload_blob(data)



    # /Users/nsalman/dev-me/azure-storage-accounts/blobStorageClient/files/file1.tgz

    # Create a local directory to hold blob data
    # local_path = "./data"
    # os.mkdir(local_path)

    # Create a file in the local data directory to upload and download
    # local_file_name = str(uuid.uuid4()) + ".txt"
    # upload_file_path = os.path.join(local_path, local_file_name)

    # # Write text to the file
    # file = open(file=upload_file_path, mode='w')
    # file.write("Hello, World!")
    # file.close()

    # print(dir(blob_service_client))
    # print(dir(container_client))

except Exception as ex:
    print('Exception:')
    print(ex)