"""Cleaning Temporary files and prefetch folder"""
import subprocess
import os
import ctypes


def run_command(command: str) -> None:
    """Run a command in the Windows command prompt.

    Args:
        command (str): The command to be executed.
    """
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        if e.returncode == 5:
            print(f"\033[93mAccess denied while executing: {e.cmd}\033[0m")
        else:
            print(f"\033[91mCommand failed with exit code {e.returncode}: {e.cmd}\033[0m")
    except FileNotFoundError as e:
        print(f"\033[91mCommand not found: {e.filename}\033[0m")
    except PermissionError as e:
        print(f"\033[91mPermission error: {e}\033[0m")
    except Exception as e:
        print(f"\033[91mAn unexpected error occurred: {e}\033[0m")


def is_admin() -> bool:
    """Check if the script is running with administrator privileges.

    Returns:
        bool: True if running as admin, otherwise False.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        print(f"\033[93mError checking admin status: {e}\033[0m")
        return False


def delete_temp_files():
    """Delete temporary files and handle access issues."""
    temp_dirs = [
        "C:\\Windows\\Temp",
        os.getenv("TEMP")
    ]
    prefetch_dir = "C:\\Windows\\Prefetch"

    for dir_path in temp_dirs:
        if os.path.exists(dir_path):
            # Attempt to delete without additional exception handling
            run_command(f'rd /s /q "{dir_path}"')

    if os.path.exists(prefetch_dir):
        # Attempt to delete Prefetch files
        run_command(f'del /q /f "{prefetch_dir}\\*.*"')


if __name__ == "__main__":
    if not is_admin():
        print("\033[91mThis script requires administrator privileges. Please run as administrator.\033[0m")
        input("Press Enter to exit.")
        exit()

    print("\033[92m" + r"""
        ____        _           ____ _                            
        |  _ \  __ _| |_ __ _   / ___| | ___  __ _ _ __   ___ _ __ 
        | | | |/ _` | __/ _` | | |   | |/ _ \/ _` | '_ \ / _ \ '__|
        | |_| | (_| | || (_| | | |___| |  __/ (_| | | | |  __/ |   
        |____/ \__,_|\__\__,_|  \____|_|\___|\__,_|_| |_|\___|_|   
    """ + "\033[0m")

    print("Press Enter to continue or '\033[91mq\033[0m' to quit.")
    user_input = input()

    if user_input.strip().lower() == "q":
        print("\033[91m❌ Script execution aborted.\033[0m")
    else:
        # Remove temporary files
        delete_temp_files()

        # Add code here to perform actions after the cleanup process completes
        print("\033[92m✅ Cleanup process completed.\033[0m")

    # Add additional code here for actions after the script completes
    input("\033[93mScript completed. Additional actions can be performed here. Press Enter to exit.\033[0m")
