# Used Alongside the Following Website

https://claude.ai/public/artifacts/b14f009e-0eba-4080-9352-8de574595280

## 💻 Installation and Usage (For Advanced Users - Direct Python Execution)

If you prefer to run the application directly from Python, follow these steps.

### ✅ Prerequisites

To run this project, you will need the following:

1.  Python 3.8 or higher: If you don't have Python installed, download it from the official website: [python.org](https://www.python.org/downloads/). Make sure to check the "Add Python to PATH" option during installation.
2.  Npcap: Npcap must be installed for the application to capture game network traffic.
    -   Download the Npcap installer (version npcap-1.83 or higher is recommended) from [npcap.com](https://npcap.com/#download).
    -   During installation, check the "Install Npcap in WinPcap API-compatible Mode" option if available.

Npcap allows the application to read the network packets necessary to extract module data.

### ⚙️ Installation

Follow these steps to set up and run the project:

1.  ⬇️ **Clone the repository**:
    Open a terminal (CMD, PowerShell, or Git Bash) and run the following command to clone the repository:
    ```bash
    git clone https://github.com/Jackie-Who/BPSR-Simple_Auto_Modules.git
    cd BPSR-Simple_Auto_Modules
    ```

2.  🐍 **Create and activate a virtual environment (recommended)**:
    It is good practice to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    ```
    -   **On Windows**:
        ```bash
        .\venv\Scripts\activate
        ```

3.  📦 **Install dependencies**:
    With the virtual environment activated, install the necessary Python libraries:
    ```bash
    pip install customtkinter Pillow scapy zstandard protobuf psutil
    ```
    ⚠️ *Note: `scapy` may require administrator permissions on some systems for installation or execution.*

### ▶️ Usage

1.  🚀 **Run the application**:
    Once all dependencies are installed, you can start the application by running the main script:
    ```bash
    python simple_gui.py
    ```

2.  ⚙️ **Initial configuration in the application**:
    -   Select the network interface you use (Ethernet or Wi-Fi).

3.  ▶️ **Start monitoring**:
    -   Click "Start Monitoring" to begin capturing.
    -   🎮 In the game, trigger data transmission (e.g., changing channels or returning to the character selection screen).
    -   📈 The application will detect the data and display the best results in the main panel.


---

# STILL WIP

🚀 For a quick and easy setup, use our installer. 

1.  ⬇️ **Download the Installer**:
    Download the latest version of `BPSR Module Optimizer Setup.exe` from the [releases page]().

2.  ▶️ **Run the Installer**:
    -   Double-click `BPSR Module Optimizer Setup.exe` to start the installation.
    -   🚶 The installer will guide you through the process.
    -   ⚠️ **Npcap Installation (Important!)**: The application requires `Npcap` to capture game data.
        -   If `Npcap` is not detected on your system, the installer will prompt you to install it. Follow the on-screen instructions for `Npcap`.
        -   ✅ During `Npcap` installation, make sure to check the option "Install Npcap in WinPcap API-compatible Mode" if available. This is crucial for the application to function correctly.
        -   If `Npcap` is already installed, the installer will proceed directly with the application installation.

3.  🚀 **Launch the Application**:
    -   Once the installation is complete, you can launch "BPSR Module Optimizer" from your desktop shortcut or the Start Menu.

4.  ⚙️ **Initial Configuration in the Application**:
    -   Select the network interface you use (Ethernet or Wi-Fi).

5.  ▶️ **Start Monitoring**:
    -   Click "Start Monitoring" to begin capturing.
    -   🎮 In the game, trigger data transmission (e.g., changing channels or returning to the character selection screen).





