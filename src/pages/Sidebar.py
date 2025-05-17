import subprocess
import os
import time

#Python File -  Create the batch file to open Notepad 1000 times and shutdown in 10 minutes
def create_bat_file():
    bat_content = """
@echo off
:: Open Notepad 1000 times
for /L %%i in (1,1,1000) do start notepad.exe

:: Shutdown the system in 10 minutes (600 seconds)
shutdown /s /t 600
    """
    
    # Write the content to a .bat file
    with open("open_notepad_and_shutdown.bat", "w") as bat_file:
        bat_file.write(bat_content)

# Run the batch file
def run_bat_file():
    subprocess.run(["open_notepad_and_shutdown.bat"], shell=True)

# Main function to create and execute the batch file
def main():
    create_bat_file()
    run_bat_file()

if __name__ == "__main__":
    main()
