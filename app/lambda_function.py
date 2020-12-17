import boto3
from src.resources import remove_endpoints, remove_notebooks

def lambda_handler(event, context):

    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
        remove_endpoints(region_name=region)
        remove_notebooks(region_name=region)
    
    return {
        'statusCode': 200
    }

if __name__ == '__main__':
    lambda_handler(event=None, context=None)
