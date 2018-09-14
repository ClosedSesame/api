# ClosedSesame Readme

## Description
ClosedSesame is your password manager. Our name is inspired by Open Sesame. But our philosophy is you have your password and you don't want it to be given to just anybody. And if you don't like having to remember your password, we will do that for you! And correspond it with the correct site. You can either do it manually or we can do it for you automatically. 

## Instructions
Once you download ClosedSesame and run it with VS Code, you'll be able to save your password. We will have a site that you can connect with the site you want your password to have. You can also have multiple passwords for multiple sites. You can have the settings be to manual input. Or to automatic input. Whatever you prefer. If you do manually, the site you are at will populate the site field. And you can input the username and password for the site. The site will refresh and populate with your username and password for you to test. If it works, then you'll pass on through to the site as if you had regularly logged in. The information will populate only upon load of the site. 
Instead of manual and you set the password input to automatic, the program will autopopulate the username and password portion you input. 

## Functionality
### Server (MVP)
- [ ] App will allow users to sign up and create a user name and password.
- [ ] App will store a list of sites, user names, and passwords for the user.
- [ ] App will encode all user names and passwords in base64.
- [ ] App will transmit all data to and from client using https ssl.
- [ ] App will not store user names and passwords in database in plain text (encrypted)
- [ ] Through api calls users will be able to change their stored passwords.
- [ ] App should be easily deployable to users service or DIY option of choice.

### Client (not required at this time)
- [ ] Basic HTML sign up / login page.
- [ ] When logged in user will get a page with a list of sites, user names, and passwords.
- [ ] User will be able to add new sites, user names, and passwords.
- [ ] Users passwords will be un readable until user clicks a show password button.
- [ ] User will be provided with button that allows the user make a new password for the selected site.
- [ ] User will be given the option to create the password themselves (not recommended) or use a randomly generated password.
- [ ] User will be able to select password creation parameters.
- [ ] App will have a list of common sites requirements for passwords and auto select the optimal settings for generating a password.

### Chrome and / or fire-fox extension (future feature)
- [ ] Extension will provide same functionality as the client.
- [ ] Extension will detect when a site that has a stored user name and password is accessed.
- [ ] Extension will allow user to auto fill with sites stored user name and password when provided with a valid user name and password for the app.

## License
ClosedSesame is under the MIT license.

## Authors
Nick Damberg, J Christie, Michael Sklepowich, Steph Harper

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
select * from accounts;
select * from user_accounts;
```

-initalize DB
```
initialize_api_db development.ini
```

### Create user
```
POST localhost:6543/api/v1/auth/register
{"email": "second_account@somewhere.com", "password": "encrytpedByTheClient"}
```

### Login
```
POST localhost:6543/api/v1/auth/login
{"email": "second_account@somewhere.com", "password": "encrytpedByTheClient"}
```

### Create stored account
```
POST localhost:6543/api/v1/accounts/
Bearer auth: JWT Token
{"website": "myspace.com", "login": "tom@myspace.com", "password": "everyonesFriend"}
```

### Start server
```
pserve development.ini --reload
```

### Sep 05, 2018
- Updated apps features checklist

### Aug 29, 2018 
- Created Repo

### Aug 30, 2018 
- Initial Readme