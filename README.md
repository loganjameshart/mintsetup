# Linux Mint Setup and Program Installation

This Python script automates the setup of a Linux system by updating the system, installing various programs using `apt`, and installing Flatpak applications.

Additionally, it installs the Dracula theme for the GNOME Terminal.

## Usage

Since this program installs `git`, you can grab the script with `wget`:

```bash
wget https://raw.githubusercontent.com/loganjameshart/mintsetup/main/mintsetup.py
```

To run this script:

```bash
sudo python3 mintsetup.py
```

## What the Script Does

1. **Update**:

 The script first updates the package lists and upgrades the installed packages on the system.

2. **Program Installation**:

 It then proceeds to install the following programs using `apt`. These are just my "have to have" ones:

    - git
    - wine
    - htop
    - black
    - psensor
    - spotify-client
    - steam

3. **Flatpak Installation**:

 It installs the following Flatpak applications:

  - org.gnome.gitlab.somas.Apostrophe *(Apostrophe Markdown Editor)*
  - com.bitwarden.desktop *(Bitwarden Password Manager)*
  - com.github.tchx84.Flatseal *(Flatseal Permissions Manager)*
  - com.usebottles.bottles *(Bottles, a WINE Frontend and Manager)*
  - com.discordapp.Discord *(Discord)*

4. **Dracula Theme Installation**:

 The script fetches and installs the Dracula theme for the GNOME Terminal.

 This involves cloning the Dracula theme repository, running its installation script, and then cleaning up by removing the cloned repository.
