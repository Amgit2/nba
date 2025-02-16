import boto3
import json
import pandas as pd

def read_nba_season_data_from_s3():
    # Define the S3 bucket and file path
    s3_bucket = "mynbadashboard"
    s3_key = "raw/season_data_20250213.json"  

    # Initialize the S3 client
    s3 = boto3.client(
        "s3",
        aws_access_key_id="AKIASLVYSPINBLTGBU6N",
        aws_secret_access_key="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",
        region_name="us-west-2"
    )

    # Download the data from S3
    response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
    data = response['Body'].read().decode('utf-8')

    # Load the JSON data
    nba_data = json.loads(data)

    df = pd.json_normalize(nba_data)
    print(df)
    

if __name__ == "__main__":
    read_nba_season_data_from_s3()