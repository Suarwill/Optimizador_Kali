# Optimizador_Kali
Conjunto de script y herramientas para optimizar Linux Kali
**Fraustech Toolkit v2.1** es una solución integral desarrollada en Python para la optimización, mantenimiento y diagnóstico de sistemas Kali Linux. Este script automatiza tareas críticas para mejorar el rendimiento del sistema, gestionar el consumo de recursos y prolongar la salud del hardware.

## 🚀 Funcionalidades Principales

El toolkit se organiza en cuatro pilares fundamentales de mantenimiento:

### 1. Diagnóstico de Salud y Hardware
*   **S.M.A.R.T. Check:** Monitoreo de la salud física del disco duro y escaneo de sectores dañados.
*   **Gestión Térmica:** Supervisión de la temperatura y frecuencia del CPU en tiempo real.
*   **Diagnóstico de Batería:** Informe detallado sobre el estado y capacidad de la batería para notebooks.
*   **Info del Sistema:** Extracción de metadatos del procesador y fabricante mediante `dmidecode`.

### 2. Limpieza Profunda del Sistema
*   **Mantenimiento de Paquetes:** Automatización de `apt clean`, eliminación de huérfanos con `deborphan` y limpieza de caché de usuario.
*   **Gestión de Logs:** Reducción dinámica del tamaño de logs del sistema (`journalctl`) para liberar espacio en disco.
*   **Docker Purge:** Limpieza exhaustiva de imágenes, contenedores, redes y volúmenes huérfanos o no utilizados.

### 3. Optimización de Performance
*   **ZRAM Swap:** Configuración de ZRAM con algoritmo `lz4` al 60% de la RAM para mejorar la multitarea sin depender del disco.
*   **Ajuste de Swappiness:** Configuración persistente de `vm.swappiness=10` para priorizar el uso de memoria física.

### 4. Orquestación de Servicios
*   **Control de Arranque:** Desactivación de servicios pesados (`Docker`, `VirtualBox`, `Containerd`) del inicio del sistema para reducir el tiempo de booteo.
*   **Modo Trabajo:** Scripting para activar el entorno de virtualización bajo demanda.

## 🛠️ Requisitos y Dependencias

El script cuenta con un sistema de verificación automática que instalará las siguientes dependencias si no están presentes:
*   `smartmontools` (Diagnóstico de disco)
*   `deborphan` (Limpieza de librerías)
*   `zram-tools` (Optimización de RAM)
*   `dmidecode` (Información de hardware)
*   `docker.io` (Gestión de contenedores)

**Requisito de Software:** Python 3.10+ (utiliza la sintaxis `match-case`).

## 📦 Instalación y Uso

1.  Clona este repositorio:
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd Optimizador_Kali
    ```

2.  Ejecuta el toolkit con privilegios de superusuario:
    ```bash
    sudo python3 main.py
    ```

## 📊 Resumen del Menú

El toolkit presenta una interfaz interactiva de consola:
*   **[1-2] INFO:** Características de CPU y Salud S.M.A.R.T.
*   **[3-4] LIMPIEZA:** Purga de Apt, huérfanos y rotación de logs.
*   **[5] OPTIMIZAR:** Despliegue de ZRAM y optimización de Swap.
*   **[6-7] SERVICIOS:** Gestión de carga para entornos de virtualización.
*   **[8-9] ESTADO:** Monitor de RAM actual y purga total de Docker.
*   **[12-14] SALUD:** Sensores de temperatura, diagnóstico de batería y test de sectores.

---

## 📄 Licencia
Este proyecto es de uso personal y educativo para la optimización de entornos de Ciberseguridad.
Desarrollado por **Fraustech**.
