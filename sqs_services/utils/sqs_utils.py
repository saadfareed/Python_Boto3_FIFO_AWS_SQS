import boto3
from uuid import uuid4
import json

def send_to_sqs(MESSAGE_PAYLOAD,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,QUEUE_URL):
    
    sqsConnection = boto3.client('sqs',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name='us-east-1')
    try:
        message_group_id = str(uuid4())
        message_deduplication_id = str(uuid4())
        response = sqsConnection.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(MESSAGE_PAYLOAD),
            MessageGroupId=message_group_id,
            MessageDeduplicationId=message_deduplication_id
        )
        return {
            'status': 'success', 
            'messageID': response['MessageId']
        }
    except Exception as e:
        return {'status': 'error', 'error': str(e)}
    

def retrieve_from_sqs(AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,QUEUE_URL):

    sqsConnection = boto3.client('sqs',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name='us-east-1')
    try:
        response = sqsConnection.receive_message(
            QueueUrl=QUEUE_URL,
            AttributeNames=['All'], 
            MaxNumberOfMessages=1
        )

        messages = response.get('Messages', [])
        if not messages:
            return {
                'status': 'Failed',
                "message": 
                    {
                        'Message': 'No messages available'
                    },
                "isDataAvailable": False
            }
        
        message = messages[0]
        return {
            'status': 'success', 
            "message": 
                {
                    'Message': json.loads(message['Body']), 
                    'ReceiptHandle': message
                },
            "isDataAvailable": True
        }
    except Exception as e:
        return {'status': 'error', 'error': str(e), "isDataAvailable": False}
    
    
def delete_from_sqs(MESSAGE,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,QUEUE_URL):

    sqsConnection = boto3.client('sqs',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name='us-east-1')
    try:
        response = sqsConnection.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=MESSAGE['ReceiptHandle']
        )
        return {
            'status': 'success', 
            "message":
                {
                    'Message': response
                }
        }
    except Exception as e:
        return {'status': 'error', 'error': str(e)}


def get_queue_message_count(AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,QUEUE_URL):

    sqsConnection = boto3.client('sqs',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name='us-east-1')
    try:
        response = sqsConnection.get_queue_attributes(
            QueueUrl=QUEUE_URL,
            AttributeNames=['ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesNotVisible']
        )
        message_count = int(response['Attributes']['ApproximateNumberOfMessages'])
        in_flight_message_count = int(response['Attributes']['ApproximateNumberOfMessagesNotVisible'])
        return {
            'status': 'success',
            "message":{ 
                'ApproximateNumberOfMessages': message_count,
                'ApproximateNumberOfMessagesNotVisible': in_flight_message_count
            }
        }
    except Exception as e:
        return {'status': 'error', 'error': str(e)}
    

# def retrieve_from_sqs(waitTime, AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,QUEUE_URL):

#     sqsConnection = boto3.client('sqs',
#         aws_access_key_id=AWS_ACCESS_KEY,
#         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
#         region_name='us-east-1')
#     try:
#         response = sqsConnection.receive_message(
#             QueueUrl=QUEUE_URL,
#             AttributeNames=['All'], 
#             MaxNumberOfMessages=1,
#             WaitTimeSeconds= waitTime
#         )

#         messages = response.get('Messages', [])
#         if not messages:
#             return {'status': 'Failed', "message": {'Message': 'No messages available', 'data': False}}
        
#         message = messages[0]
#         return {'status': 'success', "message": {'Message': json.loads(message['Body']), 'ReceiptHandle': message, 'data': True}}
#     except Exception as e:
#         return {'status': 'error', 'error': str(e), 'data': False}
