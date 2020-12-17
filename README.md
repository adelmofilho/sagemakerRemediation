# sagemakerRemediation
Schedularized lambda function to delete Sagemaker resources actives but unused


## Background

Every day I forget many Sagemaker endpoints and notebook instances, unused at my AWS account.

Every day I cry when seeing my billing report.

But tomorrow will not to be another crying day.

## Description

This project creates the infrastructure and application of an AWS Lambda function runs every hour to detect and delete Sagemaker endpoints and notebook instances in Service.

Lambda function runs are sent by AWS SNS to a personal email account.


## Usage

To replicate this implementation on your AWS account:

- Fork this repository to your Github namespace
- Deploy an AWS code pipeline instance and link it with your repository.

A code pipeline template for this purpose can be found: [HERE](https://github.com/adelmofilho/mlworks-service-catalog/blob/main/pipeline/lambda.yaml)