# sagemakerRemediation
Schedularized lambda function to delete Sagemaker resources actives but unused


## Background

Everyday I forget many Sagemaker endpoints and notebook instances unused at my AWS account.

Everyday I cry when seeing my billing report.

But tomorrow is going not to be another crying day.

## Description

This projects creates the infrastructure and aplication of a AWS Lambda function runs every hour to detect and delete Sagemaker endpoints and notebook instances in Service.

Lambda function runs are sent by AWS SNS to a personal email account.


## Usage

To replicate this implementation on your AWS account:

- Fork this repository to your Github namespace
- Deploy a AWS code pipeline instance and link it with your repository.

A code pipeline template for this purpose can be found: [HERE](https://github.com/adelmofilho/mlworks-service-catalog/blob/main/pipeline/lambda.yaml)