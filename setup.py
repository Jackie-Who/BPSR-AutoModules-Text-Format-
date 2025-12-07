import sys
from cx_Freeze import setup, Executable

# Dependencias adicionales que cx_Freeze podría no detectar automáticamente
build_exe_options = {
    "packages": ["tkinter", "customtkinter", "PIL", "scapy", "logging", "os", "json", "webbrowser", "threading", "queue", "sys"],
    "includes": [
        "network_interface_util",
        "star_resonance_monitor_core",
        "logging_config",
        "module_optimizer",
        "module_parser",
        "module_types",
        "packet_capture",
        "star_railway_monitor",
        "BlueProtobuf_pb2",
        "module_exporter",
    ],
    "include_files": [
        "icon.ico",
        "LICENSE", # Incluir la licencia
        "README.md", # Incluir el README
    ],
    "excludes": [],
    "optimize": 0,
}

# Base para ocultar la consola en Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="BPSR Module Optimizer",
    version="1.0",
    description="BPSR Module Optimizer by: Jackie",
    options={"build_exe": build_exe_options},
    executables=[Executable("simple_gui.py", base=base, icon="icon.ico")],
)

