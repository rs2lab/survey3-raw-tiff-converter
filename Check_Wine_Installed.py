import subprocess


def check_wine_installed() -> bool:
    try:
        subprocess.run(["wine", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False