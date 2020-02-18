import boto3
import click

session = boto3.Session(profile_name='default')
rds = boto3.client('rds')

@click.command()
def describe_db_instances():
    "Describe RDS instances"
    for i in rds.describe_db_instances.all():
           print (', '.join((
               i.DBInstanceIdentifier,
               i.DBInstanceClass,
               i.Engine,
               i.DBInstanceStatus,
               i.DBName,
               i.Endpoint)))

    return

if __name__ == '__main__':
   describe_db_instances()
