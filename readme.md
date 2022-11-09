# Project Title

tr:expiration tag added to missing resources

## Description

This script can be used to add tr:expiration tag to resources which do not have the tag.
They can be added to the missing resources with the key value being 29 days from the current day.

## Getting Started

### Dependencies

Libraries used for the program:
* boto3 
* collections
* datetime


### Installing

* Download the script named trexpire.py
* 

### Executing program

* Check to see if the .aws credentials have been updated,update them using cloud-tool login command from cloud-tool
```
cloud-tool login
```

* Change the credentials of defualt with the credentials stored on the profile by the cloud login tool present in the users>611XXX>.aws>credentials folder

![cloud-tool-login](https://user-images.githubusercontent.com/101724244/200761864-eb2a7f04-7709-43ff-b110-9d59faae26b8.PNG)

