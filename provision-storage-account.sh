#!/bin/bash

az storage account list --resource-group NadavHomework --query '[*].name' --output tsv | while read -r storage_account_name; do
  printf "Storage Account Name : %s \n" $storage_account_name
done

