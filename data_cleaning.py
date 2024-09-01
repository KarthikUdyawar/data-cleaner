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
            print(f"Access denied while executing: {e.cmd}")
        else:
            print(f"Command failed with exit code {e.returncode}: {e.cmd}")
    except FileNotFoundError as e:
        print(f"Command not found: {e.filename}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def is_admin() -> bool:
    """Check if the script is running with administrator privileges.

    Returns:
        bool: True if running as admin, otherwise False.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        print(f"Error checking admin status: {e}")
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
            run_command(f'rd /s /q "{dir_path}"')

    if os.path.exists(prefetch_dir):
        run_command(f'del /q /f "{prefetch_dir}\\*.*"')


if __name__ == "__main__":
    if not is_admin():
        print("This script requires administrator privileges. Please run as administrator.")
        input("Press Enter to exit.")
        exit()

    print(r"""
        ____        _           ____ _                            
        |  _ \  __ _| |_ __ _   / ___| | ___  __ _ _ __   ___ _ __ 
        | | | |/ _` | __/ _` | | |   | |/ _ \/ _` | '_ \ / _ \ '__|
        | |_| | (_| | || (_| | | |___| |  __/ (_| | | | |  __/ |   
        |____/ \__,_|\__\__,_|  \____|_|\___|\__,_|_| |_|\___|_|   
    """)

    print("Press Enter to continue or 'q' to quit.")
    user_input = input()

    if user_input.strip().lower() == "q":
        print("❌ Script execution aborted.")
    else:
        # Remove temporary files
        delete_temp_files()

        # Add code here to perform actions after the cleanup process completes
        print("✅ Cleanup process completed.")

    # Add additional code here for actions after the script completes
    input("Script completed. Additional actions can be performed here. Press Enter to exit.")
