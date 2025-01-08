import os
import tarfile

def install_requirements(libs):
    os.system(f'pip install {libs}')
    os.system("pip freeze > requirements.txt")

def show_requirements():
    with open("requirements.txt", "r") as file:
        print(f'\nCurrent libs:\n{file.read()}')

def venv_to_tar():
    current_venv = os.environ["VIRTUAL_ENV"]
    archive_name = "backup_venv.tar.gz"
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(current_venv, archive_name)
        print("Backup success")

if __name__ == "__main__":
    try:
        if os.environ["VIRTUAL_ENV"].endswith("belbysha"):
            libs_install = "Beautifulsoup4 pytest"
            install_requirements(libs_install)
            show_requirements()
            venv_to_tar()

    except KeyError:
        print("Error: current venv not defined")