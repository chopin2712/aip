# AIP - Auto-Installer-Process
You know like me, Linux has a lot of different installation packages, sh, deb, AppImage, etc. All these packages are installed with a different way. Would you like to install all the packages of a directory in once? If the answer is yes, Aip is made for you!

Support :
Flatpak, deb, AppImage, Shell Script, Snap and Aptitude

Supported in the future:
exe, pip, python.

## Usage
This software is very easy to use, you have just to enter in the directory of the file and run :

`sudo aip`

It will install all software in the directory.

Or you can use AIPN, to install packages without downloading them (using snap, apt or flatpak as example)

1. Run `sudo aipn`
2. Then answer to the questions
3. When the software is installed (with one way) make CTRL+D

## Install
### Dependencies
To install this package you will need some basic component:
* Git (`sudo apt install git`)
* Python3.7 (`sudo apt install python3.7`)
* A Root Access
### Installation
Installing this script is very easy just run these commands:
```
git clone https://github.com/chopin2712/Auto-Installer-process
cd Auto-Installer-process
sudo sh setup.sh

cd ..
sudo rm -r Auto-Installer-process
```

### Update
To update this repository just re-start the installation, it will replace the oldest files

### Uninstall (Work in progress)
To Uninstall the repository:
```
sudo sh /opt/aip/remove.sh
```

## Contribute
Of course you can contribute to this project:

### I don't want to code
1. **Make sure you respect the CONTRIBUTING.m file**
2. Create an issue and describe your problem / feature request
3. Discuss the topic
4. Close if your problem's solved

## I want to code!
1. **Make sure you respect the CONTRIBUTING.md file.**
2. Fork this repository
3. Make changes
4. Make a pull request (on branch dev)
5. You will be notified when your code has been reviewed / merged

## Copyright
This project is under GNUv3 public general License.
