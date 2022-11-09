
import boto3
import collections
import datetime 
from  datetime import date
counter=0
while counter==0:
    print("Region List")
    print("Select [0] for us-east-1")
    print("Select [1] for us-east-2")
    print("Select [2] for us-west-1")
    print("Select [3] for us-west-2")
    x=int(input("Enter Region you want to select:"))
    if x==0:
        region='us-east-1'
        counter=1
    elif x==1:
        region='us-east-2'
        counter=1
    elif x==2:
        region='us-west-1'
        counter=1
    elif x==3:
        region='us-west-2'
        counter=1
    else:
        print("Invalid Choice Entered.Select Again:")
target_tag = 'tr:expiration'
y=0
email_id=input("Enter TR Email ID [in format Firstname.MiddlenameLastname@thomsonreuters.com as Capitalized in the format]:")
while (y==0 or y==1):
    y=int(input("Enter the serivce for which you want to update the tag\nSelect[0] for RDS\nSelect[1] for EC2:\n"))

    if y==0:
        client = boto3.client('rds', region)
        
        rds_instances = client.describe_db_instances()
        db_instance_arn=[]
        for r in rds_instances['DBInstances']:
                db_instance_name1 = r['DBInstanceArn']
                db_instance_arn.append(db_instance_name1)
        listlen=str(len(db_instance_arn))
        print("Your aws account has created  ",listlen," instances so far with poweruser2 role.")   
        #print("They are",db_instance_arn)

        for i in range (len(db_instance_arn)):
            dict1={}
            
            function=db_instance_arn[i]
            #print(function)
            tags = client.list_tags_for_resource(ResourceName=function).get('TagList')
            #print(tags)
            dol = collections.defaultdict(list)
            for d in tags:
                k = d["Key"]
                v=d["Value"]
                dict1.update({k:v})
            #print(dict1)
            if (dict1.get('c7n_rds_resource_owner')==email_id or dict1.get('tr:resource-owner')==email_id):
                print(db_instance_arn[i],"Matches with the email id",email_id)
                print("Checking for",db_instance_arn[i])
                #print(db_instance_arn[i])
                if target_tag not in dict1.keys():
                    print(f"RDS {function} is missing tag {target_tag}")
                    tag_value = None
                    date_tag=0
                    while date_tag==0:
                        date_entry=(input("Enter date in YYYY-MM-DD form:"))
                        dateinput=datetime.datetime.strptime(date_entry,"%Y-%m-%d").date()
                        datenow=datetime.datetime.today()
                        daterange=datenow+datetime.timedelta(days=30)
                        daterange=daterange.date()
                        if dateinput<daterange:
                            client.add_tags_to_resource(ResourceName=function,Tags=[
                            {
                                'Key': target_tag,
                                'Value': date_entry
                            },
                            ])
                            print("Successfully updated tr:expiration tag with date value as ",date_entry)
                            date_tag=1
                        else:
                            print("Date not in range.Enter a date which is within 30 days of today's date and try again")
                            date_tag=0
                    #date_entry=input("Enter date in YYYY-MM-DD form:")

                    #tag_value = date_entry
                    #tr_tag_update=[{'target_tag':'tag_value'}]
                    #client.add_tags_to_resource(ResourceName=function,Tags=[
                    #{
                    #    'Key': target_tag,
                    #    'Value': date_entry
                    #},
                    #])
                    #print("Successfully updated tr:expiration tag with date value as ",date_entry)
                else:
                    print("Expiration Tag Exists..Checking Next Instance....If None left,Exiting")
        y=2                
    elif y==1:
        client = boto3.resource('ec2',region)
        target_tag='tr:expiration'
        ec2_instances_list=[]
        for instance in client.instances.all():
            ec2_instances_list.append(instance.id)
        #ec2_instances = ec2.instances()
        #print(ec2_instances_list)
        print("Total Number of EC2 instances created by the AWS Account using Poweruser2 credentials is :  ",len(ec2_instances_list))

        for i in range (len(ec2_instances_list)):
            
            function=ec2_instances_list[i]
            ec2instance = client.Instance(ec2_instances_list[i])
            dict1={}
            tags=ec2instance.tags
            dol = collections.defaultdict(list)
            for d in tags:
                k = d["Key"]
                v=d["Value"]
                dict1.update({k:v})
            ##pprint(dict1)
            if dict1.get('tr:resource-owner' or 'c7n_rds_resource_owner')==email_id:
                print(ec2_instances_list[i],"Matches with the email id",email_id)
                if target_tag not in dict1.keys():
                    print(f"EC2 instance {function} is missing tag {target_tag}")
                    tag_value = None
                    date_tag=0
                    while date_tag==0:
                        date_entry=(input("Enter date in YYYY-MM-DD form:"))
                        dateinput=datetime.datetime.strptime(date_entry,"%Y-%m-%d").date()
                        datenow=datetime.datetime.today()
                        daterange=datenow+datetime.timedelta(days=30)
                        daterange=daterange.date()
                        if dateinput<daterange:
                            client.create_tags(Resources=[function],Tags=[
                                {
                                    'Key': target_tag,
                                    'Value': date_entry
                                },
                            ])
                            date_tag=1
                        else:
                            print("Date not in range.Enter a date which is within 30 days of today's date and try again")
                            date_tag=0 
                        
                   # date_entry=(input("Enter date in YYYY-MM-DD form:"))
                    #datenow=date.today()
                    #daterange=date+date.delta(days=30)
                    
                    print("Successfully updated tr:expiration tag with date value as ",date_entry)
        y=2                
print("All the instances have AWS tags added or they already exist")       
print("Thanks for adding the tags.Exiting the Window.....")
