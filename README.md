# A simple RESTful API which provides a service for storing, updating, retrieving and deleting Person entities in Dynamodb using AWS Lambda, API Gateway and ServerlessFramework.

## Prerequisite 

1. Install serverless globally (The Serverless Framework is a free and open-source web framework written using Node.js. Serverless is the first framework that was originally developed for building applications exclusively on AWS Lambda, a serverless computing platform provided by Amazon as a part of the Amazon Web Services.)
    More information related Serverless Framework can be found on serverless.com
   
      **npm install serverless -g**
    
2. Configure AWS credentials - through which we are going to deploy the architecture in AWS.
    *Note - A aws user you are using for deployment should have proper roles assign to it to access AWS services such as Lambda, API                 Gateway, Dynamodb, CloudFormation, IAM and S3.
    
    **sls config credentials --provider aws --key {Access key ID} --secret {Secret access key}**

3. The **rolearn** you are using in serverless.yml should have right permission/role assigned to (post/create, get, update, delete)        entry in Dynamodb table.
   

## Deploy
 1.  Deploy your code using serverless framework using below command *also make sure you will run command where you have your serverless.yml file.*
 
     **sls deploy**


## Somethings about Serverless
   
   1. **Stack Name**
   
        ```
        service: TTdevelopement
        ```
   2. **Lambda Function Example**
   
        ```                                              
         postuser:                                          #name of Lambda function
           handler: src/function/postuser/handler.handler   #source code file
           events:                                          #API Gateway event
             - http:                                        
                 path: person                               #Resource path and method
                 method: post
       

3. **Dynamodb table creation using resource**
     AWS infrastructure resources which the AWS Lambda functions in your Service depend on, like AWS DynamoDB or AWS S3.
     Using the Serverless Framework, you can define the infrastructure resources you need in serverless.yml, and easily deploy them.
     ```
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
 1. POST USER
    While posting user information make sure you use unique id while posting new user entry to dynamodb.
    first_name, last_name, age, favourite_colour are mandatory fields while posting user information.
    
    ```
    curl -X POST https://{apigatewayendpoint}/dev/person -d '{
    "id":"1",
    "first_name": "John",
    "last_name": "Keynes",
    "age": "29",
    "favourite_colour": "red"
    }'
 
 2. GET USER
 
    ```
    curl -X GET https://{apigatewayendpoint}/dev/person/ids/1

 3. UPDATE User Information

    ```
    curl -X PUT https://{apigatewayendpoint}/dev/person/ids/1 -d '{
    "fields": {
    "last_name":"Collyer"
    }
    }'
    
 4. DELETE USER info/entry from table
    
    ```
    curl -X DELETE https://{apigatewayendpoint}/dev/person/ids/1


## ERROR HANDLING
    Above code has been tested for various user-inputs and it is handling almost all user errors.
    For e.g. 
             1. Wrong field while posting user information.
             2. Missing field check while posting user information.
             3. Unique id check while posting user information.
             4. Wrong user id while retriving user information.
             5. Wrong id check while updating user information.
             6. Wrong field while updating/modifying user information.
             7. Wrong id while deleting user information for dynamodb table.
             8. Wrong user id while retriving user information.
             9. Wrong **method** or **pathParameters** while usig above code.
          
