# !
# Experimental! Could not work! Make sure all files are in the same directory as Dashboard.py and in "rainpy" folder
# !

import os
from colorama import Fore, Style

def find_rainpy_folder():
    # Check all drives
    drives = ['%s:' % d for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists('%s:' % d)]

    for drive in drives:
        # Look for rainpy
        for root, dirs, files in os.walk(drive):
            if 'rainpy' in dirs:
                return os.path.join(root, 'rainpy')

    return None

def print_menu():
    print(Fore.YELLOW + "WARNING: Experimental! Make sure all files are in rainpy directory!\n" + Style.RESET_ALL)
    print("Welcome to Administration Dashboard!\n")
    print("Menu:")
    print("[", Fore.GREEN + "1" + Style.RESET_ALL, "] - Start the server")
    print("[", Fore.GREEN + "2" + Style.RESET_ALL, "] - Open the ConfigPreferences file")
    print("[", Fore.YELLOW + "R" + Style.RESET_ALL, "] - Restart the server")
    print("[", Fore.RED + "0" + Style.RESET_ALL, "] - Quit\n")

def main():
    rainpy_folder = find_rainpy_folder()

    if rainpy_folder:
        while True:
            print_menu()
            choice = input("< # > Choice: ")

            if choice == '1':
                # Server start
                dashboard_script_path = os.path.join(rainpy_folder, 'Admin/DeployServer.py')
                try:
                    os.system(f"python {dashboard_script_path}")
                    print(Fore.GREEN + "Server started successfully." + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"Error starting the server: {e}" + Style.RESET_ALL)

            elif choice == '2':
                # Open ConfigPreferences.txt
                config_file_path = os.path.join(rainpy_folder, "Admin", "ConfigPreferences.txt")
                try:
                    os.system(f"notepad.exe {config_file_path}")
                    print(Fore.GREEN + "ConfigPreferences file opened." + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"Error opening the file: {e}" + Style.RESET_ALL)

            elif choice.lower() == 'r':
                # Server restart
                dashboard_script_path = os.path.join(rainpy_folder, 'Dashboard.py')
                try:
                    os.system(f"python {dashboard_script_path}")
                    print(Fore.GREEN + "Server restarted successfully." + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"Error restarting the server: {e}" + Style.RESET_ALL)

            elif choice == '0':
                # Quit
                break

            else:
                print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

    else:
        print(Fore.RED + "Folder 'rainpy' not found on any drive." + Style.RESET_ALL)

if __name__ == '__main__':
    main()
