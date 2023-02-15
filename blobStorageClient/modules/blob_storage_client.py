from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

'''
The Class perform  CRUD operation on Azure Blobs.
'''
class BlobStorageClient:
    def __init__(self, connection_string, container_name):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.blob_service_client.get_container_client(container_name)

    def create_blob(self, blob_name, data):
        blob_client = self.container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data)

    def read_blob(self, blob_name):
        blob_client = self.container_client.get_blob_client(blob_name)
        data = blob_client.download_blob().content_as_text()
        return data

    def update_blob(self, blob_name, data):
        blob_client = self.container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data, overwrite=True)

    def delete_blob(self, blob_name):
        blob_client = self.container_client.get_blob_client(blob_name)
        blob_client.delete_blob()

    def list_container_blobs(self):
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            print("\t" + blob.name)

    