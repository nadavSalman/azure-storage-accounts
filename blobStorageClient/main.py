from modules.blob_storage_client import BlobStorageClient
import os


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

accounts = {
    'account_a': {
        'name': os.getenv('ACCOUNT_A'),
        'key': os.getenv('KEY_ACCOUNT_A') 
    },
    'account_b': {
        'name': os.getenv('ACCOUNT_B'),
        'key': os.getenv('KEY_ACCOUNT_B')
    }
}
accounts['account_a']['connect_str'] = 'DefaultEndpointsProtocol=https;AccountName=' + accounts['account_a']['name'] + ';AccountKey=' + accounts['account_a']['key'] + ';EndpointSuffix=core.windows.net'
accounts['account_b']['connect_str'] = 'DefaultEndpointsProtocol=https;AccountName=' + accounts['account_b']['name'] + ';AccountKey=' + accounts['account_b']['key'] + ';EndpointSuffix=core.windows.net'

def main():
    rocket_emoji = "\U0001F680"
    sparkles_emoji= "\u2728"
    print(f'{sparkles_emoji} BlobClient - Upload and Copy 100 blobs from one storage account A to B. {rocket_emoji}')

    # blob_sorage_client = BlobStorageClient(connect_str,container_name)
    blob_sorage_client = BlobStorageClient(accounts['account_a']['connect_str'],container_name="main")

    local_files_path = "./files"
    for file_name in os.listdir(local_files_path):
        upload_file_path = os.path.join(local_files_path, file_name)
        print(f" Uploging file : {upload_file_path} {rocket_emoji}")
        with open(file=upload_file_path, mode="rb") as data:
            blob_sorage_client.update_blob(file_name,data)
            #blob_sorage_client.delete_blob(blob_name=file_name)

if __name__ == '__main__':
    main()