In this guide, we will outline the steps required to set up the VM in the Amazon Web Services server.

To begin, a VM should be updated to have all packages for all existing files be brought to the newest release. Our first step into setting up our VM must be to manually run `sudo apt update` in the terminal.

In order to connect our progress with Guthub, we now have to set up credentials on our server to connect to Github via an SSH (Secure Shell) key. First, we need to create a Github account, and create a new repository matching the format 'SP25_DS5111_<your_id_code_here>'. Then we use the email account used to create our Github account to run the line `ssh-keygen -t ed25519 -C "enter-your-email-here"`, use the default name and press enter to 'not' use a passkey. Going back to your Github repository, go to Settings on the top right, and then select SSH and GPG keys on the left side. Click 'Add a new SSH key', and name it so it matches your VM's name. 

Now you have generated a new SSH key in your VM, we will run the command `cat id_ed25519.pub`, copy the contents of the key and paste them on Github on the box where we just named our new SSH key. This should now link your repository with your VM, and allow you to establish global credentials to link your work online.

To check that everything so far has worked correctly, run the command `ssh -T -i ed25519 git@github.com` on the terminal, and you should see your Github name echoed back to you:

`ubuntu@ip-172-31-83-121:~/.ssh$  ssh -T -i id_ed25519 git@github.com
Hi etiennejimenez! You've successfully authenticated, but GitHub does not provide shell access.
ubuntu@ip-172-31-83-121:~/.ssh$`

Now we can move on to set up the credentials. To do this, we will type `vim 00_01_setup_git_global_creds.sh`, press `I` on your keyboard to insert text, and copy and paste the following code inside it:

```
!#/usr/bin/bash

USER=rcs2mh@virginia.edu
NAME=etiennejimenez

git config --global --list

git config --global user.email ${USER} 
git config --global user.name  ${NAME} 

git config --global --list
```

where you will rewrite your user and name information to be your own email address and Github username, respectively. Press the ESC key on your keyboard and type `:wq` to save and exit your changes on VIM. To finish setting up global creds, run this code using `bash 00_01_setup_git_global_creds.sh`. To check that everything went smoothly, run the line `git status` into the terminal, and you should see that the server acknowledges your username and your repository name.

Now, to get up to date with everything, you will clone this repository by running the following code on your terminal:

git clone git@github.com:etiennejimenez/SP25_DS5111_rcs2mh.git

so that all the remaining steps can be easily recreated by running some scripts already present on this repo. The first of these is going to be `bash init.sh`.


 
