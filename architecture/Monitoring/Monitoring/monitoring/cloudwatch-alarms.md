CloudGuard — CloudWatch Monitoring

1. Objective

The objective of this module is to monitor Amazon EC2 resources and detect abnormal conditions using Amazon CloudWatch.

2. AWS Service

Amazon CloudWatch

CloudWatch collects metrics, monitors logs, and triggers alarms when configured conditions are met.

3. Monitoring Plan

The project will monitor:

- EC2 CPU utilization.
- EC2 instance status checks.
- Application health.
- Relevant application logs, where configured.

4. Alarm Configuration

Example CPU alarm:

- Metric: CPUUtilization
- Threshold: Greater than 80%
- Evaluation period: 5 minutes
- Purpose: Identify sustained high CPU utilization.

The exact alarm settings must be configured and tested in AWS.

5. Recovery Workflow

1. CloudWatch evaluates the configured metric.
2. The alarm changes state when its condition is met.
3. The configured automation workflow is triggered.
4. AWS Lambda may perform an authorized recovery action.
5. Amazon SNS can notify the administrator.
6. Monitoring verifies whether the issue has been resolved.

6. Security

- Use least-privilege IAM permissions.
- Avoid unnecessary automated recovery actions.
- Log and verify recovery attempts.
- Review AWS pricing before enabling additional monitoring features.

7. Testing Status

Planned: Configure the alarm and verify its behavior in AWS.

Implementation status will be updated after testing.
