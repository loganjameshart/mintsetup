#! /usr/bin/env python3

import subprocess

PROGRAMS = ["git", "wine", "htop", "black", "psensor", "spotify-client"]

FLATPAKS = [
    "org.gnome.gitlab.somas.Apostrophe",
    "com.bitwarden.desktop",
    "com.github.tchx84.Flatseal",
    "com.usebottles.bottles",
    "com.discordapp.Discord",
]


def update():
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
        subprocess.run(["sudo", "apt", "install", "-y", program])
        print("\n")


def flatpak_install(flatpak_list: list) -> None:
    """Install Flatpak programs from list."""

    print(">>> Installing Flatpaks...\n")
    for flatpak in flatpak_list:
        print(f"Installing {flatpak}...\n")
        subprocess.run(["flatpak", "install", flatpak])
        print("\n")

def main():
    update()
    apt_install(PROGRAMS)
    flatpak_install(FLATPAKS)


if __name__ == "__main__":
    main()
