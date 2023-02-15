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
rocket_emoji = "\U0001F680"
sparkles_emoji= "\u2728"
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

def accounts_state(blob_sorage_client_a,blob_sorage_client_b):
    print('*'*90)
    print('List blobs in from Storage account A to B')
    print(f'{sparkles_emoji} Storage account A {sparkles_emoji}')
    blob_sorage_client_a.list_container_blobs()
    print(f'{sparkles_emoji} Storage account B {sparkles_emoji}')
    blob_sorage_client_b.list_container_blobs()
    print('*'*90)

def main():
    print(f'{sparkles_emoji} BlobClient - Upload and Copy 100 blobs from one storage account A to B. {rocket_emoji}')

    # blob_sorage_client = BlobStorageClient(connect_str,container_name)
    blob_sorage_client_a = BlobStorageClient(accounts['account_a']['connect_str'],container_name="main")
    blob_sorage_client_b = BlobStorageClient(accounts['account_b']['connect_str'],container_name="main")

    accounts_state(blob_sorage_client_a,blob_sorage_client_b)

    local_files_path = "./files"
    for file_name in os.listdir(local_files_path):
        upload_file_path = os.path.join(local_files_path, file_name)
        print(f" file : {upload_file_path} {rocket_emoji}")
        with open(file=upload_file_path, mode="rb") as data:
             blob_sorage_client_a.update_blob(file_name,data)
            #blob_sorage_client_b.delete_blob(blob_name=file_name)
            # blob_sorage_client_a.delete_blob(blob_name=file_name)


    accounts_state(blob_sorage_client_a,blob_sorage_client_b)

    # Copy 100 blobs from Storage account A to B

    #   Upload  & Delete
    count = 0
    for blob in blob_sorage_client_a.get_container_blobs():
        print(f'{count}/100 copied {rocket_emoji}')
        count+=1
        source_blobs_data = blob_sorage_client_a.read_blob(blob)
        blob_sorage_client_b.update_blob(blob_name=blob,data=source_blobs_data)
        blob_sorage_client_a.delete_blob(blob_name=blob)

    accounts_state(blob_sorage_client_a,blob_sorage_client_b)

    # Clean Up  Storage account A to B
    print(f'{sparkles_emoji} Clean Up  Storage account A to B {sparkles_emoji}')
    blob_sorage_client_a.clean_blobs()
    blob_sorage_client_b.clean_blobs()
    accounts_state(blob_sorage_client_a,blob_sorage_client_b)
if __name__ == '__main__':
    main()