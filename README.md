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


## Somethings about Serverless
   
   1. **Stack Name**
   
        service: TTdevelopement <br />
        
   2. **Lambda Function Example**
   
        functions:                                           <br />               
        postuser:                                            #name of Lambda function <br />
            handler: src/function/postuser/handler.handler   #source code file  <br />
            events:                                          #API Gateway event <br />
              - http:                                        <br />
                  path: person                               #Resource path and method <br />
                  method: post


3. **Dynamodb table creation using resource**

     resources:
      Resources:
        usertable:
          Type: AWS::DynamoDB::Table
          Properties:
            TableName: userinformation
            AttributeDefinitions:
              - AttributeName: id
                AttributeType: S
            KeySchema:
              - AttributeName: id
                KeyType: HASH
            ProvisionedThroughput:
              ReadCapacityUnits: 1
              WriteCapacityUnits: 1
            StreamSpecification:
              StreamViewType: NEW_AND_OLD_IMAGES
              
## Input
