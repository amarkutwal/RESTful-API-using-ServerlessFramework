# A simple RESTful API which provides a service for storing, updating, retrieving and deleting Person entities in Dynamodb using AWS Lambda and API Gateway. Deploy the architecture using ServerlessFramework.

## Prerequisite 

1. Install serverless globally (The Serverless Framework is a free and open-source web framework written using Node.js. Serverless is the first framework that was originally developed for building applications exclusively on AWS Lambda, a serverless computing platform provided by Amazon as a part of the Amazon Web Services.)
    More information related Serverless Framework can be found on serverless.com
    
    **npm install serverless -g**

2. Configure AWS credentials - through which we are going to deploy the architecture in AWS.
    *Note - A aws user you are using for deployment should have proper roles assign to it to access AWS services such as Lambda, API Gateway, Dynamodb and S3.
    
    **sls config credentials --provider aws --key <Access key ID> --secret <Secret access key>**


## Deploy
 1.  Deploy your code using serverless framework using below command *also make sure you will run command where you have your serverless.yml file.*
 
     **sls deploy**
