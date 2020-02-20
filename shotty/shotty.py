import boto3
import click

session = boto3.Session(profile_name='python-aws')
ec2 = session.resource('ec2')

@click.command()
@click.option('--project', default=None,
    help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    "List EC2 instances"
    instances=[]

    if project:
        filters = [{'Name':'tag:project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
           print (', '.join((
               i.id,
               i.instance_type,
               i.placement['AvailabilityZone'],
               i.state['Name'],
               i.public_dns_name)))

    return

if __name__ == '__main__':
   list_instances()
