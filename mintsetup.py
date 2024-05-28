#! /usr/bin/env python3

import subprocess
import os

NAME = os.getlogin()
WORKING_DIRECTORY = os.getcwd()

PROGRAMS = ["git", "htop", "black", "psensor", "vlc", "steam"]

FLATPAKS = [
    "com.bitwarden.desktop",
    "com.github.tchx84.Flatseal",
    "com.usebottles.bottles",
    "com.discordapp.Discord",
    "com.github.Rosalie241.RMG",
    "net.rpcs3.RPCS3",
]


def update() -> None:
    """Update and upgrade."""

    print(">>> Running update, upgrade, and autoremove...\n")
    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])
    subprocess.run(["sudo", "apt", "autoremove", "-y"])


def apt_install(program_list: list) -> None:
    """Install programs from list using apt."""

    print(">>> Installing programs using apt...\n")
    for program in program_list:
        print(f">>> Installing {program}...\n")
        try:
            result = subprocess.run(["sudo", "apt", "install", "-y", program], stderr=subprocess.PIPE)
            if result.returncode != 0:
                print(f">>> Error installing {program}: {result.stderr.decode()}\n")
            else:
                print(f">>> {program} successfully installed!\n")
        except Exception as e:
            print(f">>> An error occurred while installing {program}: {e}\n")


def flatpak_install(flatpak_list: list) -> None:
    """Install Flatpak programs from list."""

    print(">>> Installing Flatpaks...\n")
    for flatpak in flatpak_list:
        try:
            print(f">>> Installing {flatpak}...\n")
            result = subprocess.run(["flatpak", "install", flatpak, "-y"], stderr=subprocess.PIPE)
            if result.returncode != 0:
                print(f">>> Error installing {flatpak}: {result.stderr.decode()}\n")
            else:
                print(f">>> {flatpak} successfully installed!\n")
        except Exception as e:
            print(f">>> An error occurred while installing {flatpak}: {e}\n")


def get_dracula() -> None:
    """Get and install the Dracula theme for gnome-terminal, then cleanup."""

    print(">>> Installing Dracula theme for gnome-terminal...\n")
    try:
        subprocess.run(["git", "clone", r"https://github.com/dracula/gnome-terminal"], check=True)
        os.chdir("gnome-terminal")
        subprocess.run(r"./install.sh", check=True)
        os.chdir(WORKING_DIRECTORY)
        subprocess.run(["rm", "-rf", "gnome-terminal"], check=True)
        print(">>> Dracula theme successfully installed and cleaned up!\n")
    except subprocess.CalledProcessError as e:
        print(f">>> Error: {e}\n")
    except Exception as e:
        print(f">>> An error occurred: {e}\n")

def get_musescore() -> None:
    mscore_link = "https://cdn.jsdelivr.net/musescore/v4.3.0/MuseScore-Studio-4.3.0.241231431-x86_64.AppImage"
    appimage_name = mscore_link.split("/")[-1]
    subprocess.run(["wget", "https://cdn.jsdelivr.net/musescore/v4.3.0/MuseScore-Studio-4.3.0.241231431-x86_64.AppImage"])
    subprocess.run(["chmod u+x", f"{appimage_name}"])
    subprocess.run([f"./{appimage_name}", "install"])


def main():
    update()
    apt_install(PROGRAMS)
    flatpak_install(FLATPAKS)
    get_dracula()
    get_musescore()


if __name__ == "__main__":
    main()
