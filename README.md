# python-aws
Project to access and manage AWS with Python

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile python-aws`

## Running

`pipenv run "python3 shotty/shotty.py <command> <subcommand> <--project=PROJECT>"`
  or
`python3 shotty/shotty.py <command> <subcommand> <--project=PROJECT>"`

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional
