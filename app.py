import boto3
client = boto3.client('ec2)
response = client.run_instances(
      ImageId='ami-0680f1a688cd311c',
      InstanceType='t2micro',
      KeyName='Public',
      MaxCount=1,
      MinCount=1
