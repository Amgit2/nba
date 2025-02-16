import requests
import json
import boto3
from datetime import datetime

import http.client




def fetch_nba_season_data():
    # Define the NBA API endpoint
    #api_url = "https://api.nba.com/stats/season"
    url = "https://api-nba-v1.p.rapidapi.com/games"

    querystring = {"season":"2021"}

    headers = {
        "x-rapidapi-key": "8ecc64b251mshee3e1f83d92f07ep13f29bjsnc7f04016b16f",
        "x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
    }


    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    print(response.json())
    #print(data.decode("utf-8"))

    # Fetch the data from the NBA API
    #response = requests.get(api_url)
    #data = response.json()

    s3 = boto3.client(
        "s3",
        aws_access_key_id="AKIASLVYSPINBLTGBU6N",
        aws_secret_access_key="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",
        region_name="us-west-2"
    )

    # Define the S3 bucket and file path
    s3_bucket = "mynbadashboard"
    s3_key = f"raw/season_data_{datetime.now().strftime('%Y%m%d')}.json"
    # Access = AKIASLVYSPINBLTGBU6N
    # Secret = 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


    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Upload the data to S3
    s3.put_object(
        Bucket=s3_bucket,
        Key=s3_key,
        Body=json.dumps(data),
        ContentType='application/json'
    )


if __name__ == "__main__":
    fetch_nba_season_data()