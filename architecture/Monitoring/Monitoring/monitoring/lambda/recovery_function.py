import os
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client("ec2")


def lambda_handler(event, context):
    instance_id = os.environ.get("INSTANCE_ID")

    if not instance_id:
        logger.error("INSTANCE_ID environment variable is missing.")
        return {
            "statusCode": 400,
            "body": "Instance ID is not configured."
        }

    try:
        response = ec2.reboot_instances(
            InstanceIds=[instance_id]
        )

        logger.info("EC2 reboot request submitted.")

        return {
            "statusCode": 200,
            "body": f"Reboot request submitted for {instance_id}."
        }

    except Exception:
        logger.exception("EC2 reboot request failed.")
        raise
