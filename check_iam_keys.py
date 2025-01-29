import boto3
from datetime import datetime, timezone, timedelta

def deactivate_idle_keys():
    # Initialize AWS IAM client
    iam_client = boto3.client('iam')
    now = datetime.now(timezone.utc)

    # Fetch all IAM users
    users = iam_client.list_users()['Users']
    for user in users:
        # Fetch all access keys for the user
        access_keys = iam_client.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
        
        for key in access_keys:
            key_id = key['AccessKeyId']
            key_status = key['Status']
            key_name = key.get('AccessKeyId')  # AWS IAM does not support direct key naming, so we check the ID

            # Check last used date only for active keys
            if key_status == 'Active' and key_name == "deployment":
                response = iam_client.get_access_key_last_used(AccessKeyId=key_id)
                last_used_date = response.get('AccessKeyLastUsed', {}).get('LastUsedDate')
                
                if last_used_date:
                    elapsed_time = now - last_used_date
                    # Deactivate key if it has been idle for more than 2 minutes
                    if elapsed_time > timedelta(minutes=2):
                        iam_client.update_access_key(
                            UserName=user['UserName'],
                            AccessKeyId=key_id,
                            Status='Inactive'
                        )
                        print(f"Deactivated unused key {key_id} (deployment) for user {user['UserName']}")
                else:
                    # If key has never been used, deactivate it
                    iam_client.update_access_key(
                        UserName=user['UserName'],
                        AccessKeyId=key_id,
                        Status='Inactive'
                    )
                    print(f"Deactivated unused key {key_id} for user {user['UserName']}")

if __name__ == "__main__":
    deactivate_idle_keys()
