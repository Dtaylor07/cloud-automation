import boto3
from datetime import datetime, timezone, timedelta

# AWS IAM client
iam_client = boto3.client('iam')

# IAM user whose keys we need to manage
IAM_USER = "deployment"

# Time threshold (60 minutes)
IDLE_TIME = timedelta(minutes=43200)

def check_and_deactivate_keys():
    now = datetime.now(timezone.utc)

    # Get all access keys for the user
    response = iam_client.list_access_keys(UserName=IAM_USER)

    for key in response['AccessKeyMetadata']:
        key_id = key['AccessKeyId']
        key_status = key['Status']

        if key_status == 'Active':
            # Get the last used time of the key
            last_used_response = iam_client.get_access_key_last_used(AccessKeyId=key_id)
            last_used_date = last_used_response.get('AccessKeyLastUsed', {}).get('LastUsedDate')

            if last_used_date:
                elapsed_time = now - last_used_date
                if elapsed_time > IDLE_TIME:
                    # Deactivate the key
                    iam_client.update_access_key(UserName=IAM_USER, AccessKeyId=key_id, Status='Inactive')
                    print(f"Deactivated key {key_id} for user {IAM_USER} due to inactivity.")
            else:
                # If key has never been used, deactivate it
                iam_client.update_access_key(UserName=IAM_USER, AccessKeyId=key_id, Status='Inactive')
                print(f"Deactivated unused key {key_id} for user {IAM_USER}.")

if __name__ == "__main__":
    check_and_deactivate_keys()
