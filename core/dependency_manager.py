# dependency_manager.py
import sys, importlib, platform, subprocess, logging

def is_virtual_env():
    return sys.prefix != sys.base_prefix

def run_command(command, description):
    print(f"\n[+] {description}...")
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"[!] Falló la ejecución de: {description}")
        return False

def setup_dependencies(libraries, update_status_callback=None):
    total = len(libraries)
    for index, entry in enumerate(libraries):
        if isinstance(entry, tuple):
            lib_name = entry[0]
            pip_pkg = entry[1]
        else:
            lib_name = pip_pkg = entry
        
        progress = int(((index + 1) / total) * 100)
        
        try:
            importlib.import_module(lib_name)
            if update_status_callback:
                update_status_callback(f"Librería '{lib_name}' lista.", progress)
        except ImportError:
            if update_status_callback:
                update_status_callback(f"Instalando '{pip_pkg}'...", progress)

            pip_command = [sys.executable, '-m', 'pip', 'install', pip_pkg]
            
            # Solución para PEP 668 en Kali/Debian (externally-managed-environment)
            if platform.system() == 'Linux' and not is_virtual_env():
                pip_command.append('--break-system-packages')

            try:
                subprocess.check_call(pip_command)
            except subprocess.CalledProcessError as e:
                logging.error(f"Error instalando {pip_pkg}: {e}")