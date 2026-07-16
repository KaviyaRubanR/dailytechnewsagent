import json
import boto3

def lambda_handler(event, context):
    ses = boto3.client('ses')

    sender = "kaviyarubanr@gmail.com"
    receiver = "kaviyarubanr@gmail.com"

    subject = "Daily Tech News"

    body = """Good Morning,

Here is your Daily Tech News:

- AI tools are transforming everyday work.
- Cloud computing demand is rising.
- Cybersecurity awareness is increasing.
- New smartphones focus on AI features.
- Remote work tools are improving.

Have a great day!
"""

    ses.send_email(
        Source=sender,
        Destination={'ToAddresses': [receiver]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}}
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Email sent successfully!')
    }
