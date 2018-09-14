# ClosedSesame Readme

## Deployed Link
https://ec2-18-191-251-70.us-east-2.compute.amazonaws.com

## Authors
Nick Damberg, J Christie, Michael Sklepowich, Steph Harper

## Overview
ClosedSesame is your password manager. Our name is inspired by Open Sesame. But our philosophy is you have your password and you don't want it to be given to just anybody. And if you don't like having to remember your password, we will do that for you! And correspond it with the correct site. We do it for you automatically.

## Installation Instructions
To run ClosedSesame, you will have to download Postman.
Once you download ClosedSesame and run it with VS Code, you'll be able to save your password.
We will have a site that you can connect with the site you want your password to have. You can also have multiple passwords for multiple sites. You can have the settings be to manual input. Or to automatic input. Whatever you prefer. If you do manually, the site you are at will populate the site field. And you can input the username and password for the site. The site will refresh and populate with your username and password for you to test. If it works, then you'll pass on through to the site as if you had regularly logged in. The information will populate only upon load of the site.
Instead of manual and you set the password input to automatic, the program will autopopulate the username and password portion you input.

## Step by Step Walkthrough

## License
ClosedSesame is under the MIT license.


## Change log

### Sep 12, 2018
- setup database
```
sudo -u postgres psql
\du
ALTER USER postgres WITH PASSWORD 'Password!1';
CREATE DATABASE closedsesame;
\l
\c closedsesame
\dt
```

-initalize DB
```
initialize_api_db development.ini
```

### Sep 05, 2018
- Updated apps features checklist

### Aug 29, 2018
- Created Repo

### Aug 30, 2018
- Initial Readme
