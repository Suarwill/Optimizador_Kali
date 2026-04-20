import os
import shutil
from .core.dependency_manager import setup_dependencies, run_command

# --- CONFIGURACIÓN DE DEPENDENCIAS ---
DEPENDENCIAS_SISTEMA = {
    "smartctl": "smartmontools",
    "deborphan": "deborphan",
    "zramctl": "zram-tools",
    "dmidecode": "dmidecode",
    "docker": "docker.io"
}

def install_system_tools():
    print("[*] Verificando herramientas de sistema...")
    for comando, paquete in DEPENDENCIAS_SISTEMA.items():
        if shutil.which(comando) is None:
            run_command(f"sudo apt update && sudo apt install -y {paquete}", f"Instalando {paquete}")
        else:
            print(f"[OK] {comando} ya está instalado.")

def setup_zram():
    print("\n--- Configuración de ZRAM ---")
    zram_config = "ALGO=lz4\nPERCENT=60\nPRIORITY=100\n"
    # Encadenamos comandos usando la utilidad del core
    run_command(f"echo '{zram_config}' | sudo tee /etc/default/zramswap", "Escribiendo configuración")
    run_command("sudo modprobe zram && sudo systemctl restart zramswap", "Activando ZRAM")

def docker_purge():
    print("\n--- Limpieza Profunda de Docker ---")
    # Verificación rápida de estado
    import subprocess
    status = subprocess.run("systemctl is-active docker", shell=True, capture_output=True, text=True)
    
    cmd = "sudo docker system prune -a --volumes -f"
    if "active" in status.stdout:
        run_command(cmd, "Eliminando recursos de Docker")
    else:
        run_command(f"sudo systemctl start docker && {cmd} && sudo systemctl stop docker", "Limpieza temporal")

def main():
    # Inicialización
    install_system_tools()
    
    while True:
        print("\n" + "═"*55)
        print("      FRAUSTECH TOOLKIT v2.3 - CORE REFACTOR")
        print("═"*55)
        print(" 1. [INFO] Hardware/CPU          8. [ESTADO] RAM/ZRAM")
        print(" 2. [INFO] Salud Disco           9. [DOCKER] Purga Total")
        print(" 3. [LIMPIEZA] Apt/Huérfanos    12. [SALUD] Temp/Reloj")
        print(" 4. [LIMPIEZA] Logs Systemd     13. [SALUD] Batería")
        print(" 5. [OPTIMIZAR] ZRAM/Swap       14. [SEGURIDAD] SMART Test")
        print(" 0. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        match opcion:
            case "1":
                os.system("lscpu | grep -E 'Model name|CPU\(s\)|Thread'")
                run_command("sudo dmidecode -s system-product-name", "Modelo")
            case "2":
                run_command("sudo smartctl -H /dev/sda", "Salud HDD")
            case "3":
                run_command("sudo apt clean && sudo apt autoremove --purge -y $(deborphan)", "Limpieza APT")
                run_command("rm -rf ~/.cache/*", "Limpieza Caché Usuario")
            case "4":
                run_command("sudo journalctl --vacuum-size=200M", "Rotación de Logs")
            case "5":
                setup_zram()
                run_command("echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf && sudo sysctl -p", "Swappiness")
            case "6":
                run_command("sudo systemctl disable virtualbox docker docker.socket", "Desactivar servicios")
            case "7":
                run_command("sudo systemctl start docker virtualbox", "Activar servicios")
            case "8":
                os.system("free -h && swapon --show && zramctl")
            case "9":
                docker_purge()
            case "12":
                run_command("sensors", "Temperatura")
            case "13":
                run_command("upower -i /org/freedesktop/UPower/devices/battery_BAT0", "Batería")
            case "14":
                run_command("sudo smartctl -t short /dev/sda", "Smart Test")
            case "0":
                break

if __name__ == "__main__":
    main()