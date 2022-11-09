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

* Go to the source file and run the script trexpire.py
```
python trexpire.py
```
* Select the region needed to be checked
![Region_select](https://user-images.githubusercontent.com/101724244/200762885-e384f54b-bf07-453d-a37e-d206baa501cb.PNG)

* Enter the tr:resource-owner credentials used by you while creating the resources 
  
![name](https://user-images.githubusercontent.com/101724244/200763260-9be9c6f7-3510-484e-8573-7211fe7ba0d7.PNG)

* Select the service you want to update the tags for 

![selec_service](https://user-images.githubusercontent.com/101724244/200763714-d36a7a6a-088b-4ed3-91b4-474b4659a8e3.PNG)

* The script checks the service selected and iterates through every resource missing the tr:expiration tag and prompts the user to enter it
![enterddmmyyyy](https://user-images.githubusercontent.com/101724244/200764350-29cd1e91-ef9a-46d1-be59-b647892f4a98.PNG)

* The resource gets updated with the tr:expiration tag and checks if any other resource needs updating.If it does,iterates through the program again and if not,exits     the program
 
![updated](https://user-images.githubusercontent.com/101724244/200764649-763ed3c9-f0a8-45f9-a578-5bf3f6f57a46.PNG)

