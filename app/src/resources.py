import boto3


def remove_endpoints(region_name):
    client = boto3.client("sagemaker", region_name=region_name)
    endpoint_list = client.list_endpoints()
    for endpoint in endpoint_list["Endpoints"]:
        endpoint_name = endpoint["EndpointName"]
        endpoint_status = client.describe_endpoint(EndpointName=endpoint_name)["EndpointStatus"]
        if endpoint_status == "InService":
            client.delete_endpoint(EndpointName=endpoint_name)


def remove_notebooks(region_name):
    client = boto3.client("sagemaker", region_name=region_name)
    notebook_list = client.list_notebook_instances()
    for notebook in notebook_list["NotebookInstances"]:
        notebook_name = notebook["NotebookInstanceName"]
        notebook_status = notebook["NotebookInstanceStatus"]
        if notebook_status == "InService":
            client.stop_notebook_instance(NotebookInstanceName=notebook_name)
        if notebook_status == "Stopped":
            client.delete_notebook_instance(NotebookInstanceName=notebook_name)
