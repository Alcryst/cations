# cations



*Ready to make productivity a habit?*

**cations** is a lightweight application that helps you build and maintain good habits through incremental progress. Using this application, you can apply the philosophy of leading productivity systems, such as James Clear's "Atomic Habits", to achieve significant long-term success in a manageable and realistic way.

**cations** is designed to run entirely in the terminal, allowing you to use it easily and conveniently. User-friendliness and efficiency are prioritized, so you can focus on completing your habits.



## Quick Start

Follow these steps to install **cations** and get started right away.

*Note: This application requires Python 3 and pip3 to be installed on your system.*

1. Not necessary, but recommended: Navigate to your home directory (or whichever directory you normally clone repositories to) first.

```bash
cd ~
```

2. Clone the repository:

```bash
git clone https://github.com/Alcryst/cations.git
```

3. Enter the project directory:

```bash
cd cations
```

4. Run the setup file:

```bash
sh install.sh
```

5. Once installation has completed, you will be able to start the application by simply entering the command:

```bash
cations
```

**NOTE:** if at this point you get an error saying that the command does not exist, please make sure your Python scripts are added to your $PATH variable. An easy fix is to install the most recent version of Python 3, as the modern official installer will automatically configure your $PATH variable for you.



## Usage

Each habit is represented by an "ion". When creating your ion, name it after a habit you want to repeat each day - for example, "Practice the piano" or "Write a line of code". Make it simple and easy to complete, to inspire you to get started and make consistent progress; once you've achieved consistency then you can slowly start to increase the intensity of your habit (and change the name of your ion if you wish).

You can complete each ion every day to extend your streak: the number of consecutive days that you've completed an ion. If you miss a day, your streak will reset to 0. Don't be demotivated, though; the important part is getting back on track.

Press C for full controls on how to use the application.



## Uninstallation/Deletion Instructions

1. You can uninstall everything except the repository files with pip3 like so:

```bash
pip3 uninstall cations
```

2. To remove the rest of the files, navigate to the directory containing cations and manually remove the directory, e.g. through the file explorer or command line:
```bash
rm -vrf cations/
```

**Note: be careful that you're using this command on the right directory if you choose to use it!**



## Update Instructions

Uninstall and do a fresh install as shown above.



## Patch Notes

- Ver 1.0.1: Fix file accessing issue when repository is not in home directory

- Ver 1.0.0: Release!

## Contributions & License

Contributions are more than welcome! Feel free to submit issues or pull requests if you have ideas for how to make **cations** even better.

This project is licensed under the MIT License. See the LICENSE file for more information.

___

**cations** by Alcryst
