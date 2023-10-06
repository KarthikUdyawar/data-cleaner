"""Cleaning Temporary files and prefetch folder"""
import subprocess


def run_command(command: str) -> None:
    """Run a command in the Windows command prompt.

    Args:
        command (str): The command to be executed.
    """
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}: {e.cmd}")
    except FileNotFoundError as e:
        print(f"Command not found: {e.filename}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Prompt the user to press Enter to continue or 'q' to quit
    print("🧹 Temporary files, %temp%, and prefetch folder cleaned.")
    print("Press Enter to continue or 'q' to quit.")
    user_input = input()

    if user_input.strip().lower() == "q":
        print("❌ Script execution aborted.")
    else:
        # Remove temporary files
        run_command("rd /s /q C:\\Windows\\Temp")
        run_command("rd /s /q %temp%")

        # Remove contents of the prefetch folder
        run_command("del /q /f C:\\Windows\\Prefetch\\*.*")

        # Add code here to perform actions after the cleanup process completes
        print("✅ Cleanup process completed.")

    # Add additional code here for actions after the script completes
    input(
        "Script completed. Additional actions can be performed here. Press Enter to exit"
    )
