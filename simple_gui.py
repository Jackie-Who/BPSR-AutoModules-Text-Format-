"""
BPSR Module Exporter - Simplified GUI
Only captures modules and exports to text file automatically.
"""

import customtkinter as ctk
from tkinter import messagebox
import threading
from typing import List, Optional

from logging_config import setup_logging, get_logger
from network_interface_util import get_network_interfaces
from module_parser import ModuleParser
from module_types import ModuleInfo
from packet_capture import PacketCapture
from module_exporter import export_modules_to_file

# Setup logging
setup_logging()
logger = get_logger(__name__)

# Theme settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SimpleMonitor:
    """Simplified monitor that captures modules and auto-exports."""
    
    def __init__(self, interface_name: str, on_export_callback=None):
        self.interface_name = interface_name
        self.on_export_callback = on_export_callback
        self.packet_capture = PacketCapture(interface_name)
        self.module_parser = ModuleParser()
        self.captured_modules: Optional[List[ModuleInfo]] = None
        self.is_running = False
        
    def start(self):
        """Start monitoring."""
        self.is_running = True
        self.captured_modules = None
        self.packet_capture.start_capture(self._on_data_captured)
        
    def stop(self):
        """Stop monitoring."""
        self.is_running = False
        self.packet_capture.stop_capture()
        
    def _on_data_captured(self, data):
        """Callback when data is captured - auto exports."""
        if self.captured_modules is not None:
            return  # Already captured
            
        try:
            v_data = data.get('v_data')
            if v_data:
                modules = self.module_parser.parse_module_info(v_data)
                if modules:
                    self.captured_modules = modules
                    # Auto-export
                    filepath = export_modules_to_file(modules)
                    logger.info(f"Exported {len(modules)} modules to: {filepath}")
                    
                    if self.on_export_callback:
                        self.on_export_callback(len(modules), filepath)
                        
        except Exception as e:
            logger.error(f"Error processing data: {e}")


class App(ctk.CTk):
    """Simplified BPSR Module Exporter GUI."""
    
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.title("BPSR Module Exporter")
        self.geometry("450x300")
        self.resizable(False, False)
        
        # Variables
        self.monitor: Optional[SimpleMonitor] = None
        self.interfaces = get_network_interfaces()
        self.interface_names = [f"{i['name']} ({i['addresses'][0]['addr']})" 
                                for i in self.interfaces if i['addresses']]
        
        # Build UI
        self._create_widgets()
        
    def _create_widgets(self):
        """Create all UI widgets."""
        # Main container
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ctk.CTkLabel(
            main_frame, 
            text="BPSR Module Exporter",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=(0, 20))
        
        # Network interface dropdown
        interface_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        interface_frame.pack(fill="x", pady=10)
        
        interface_label = ctk.CTkLabel(
            interface_frame, 
            text="Network Interface:",
            font=ctk.CTkFont(size=14)
        )
        interface_label.pack(anchor="w")
        
        self.interface_dropdown = ctk.CTkComboBox(
            interface_frame,
            values=self.interface_names if self.interface_names else ["No interfaces found"],
            width=400,
            state="readonly"
        )
        self.interface_dropdown.pack(fill="x", pady=(5, 0))
        if self.interface_names:
            self.interface_dropdown.set(self.interface_names[0])
        
        # Status label
        self.status_label = ctk.CTkLabel(
            main_frame,
            text="Ready - Select interface and click Start",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.status_label.pack(pady=20)
        
        # Buttons frame
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=10)
        
        # Start button
        self.start_button = ctk.CTkButton(
            button_frame,
            text="▶ Start Monitoring",
            command=self.start_monitoring,
            width=180,
            height=40,
            font=ctk.CTkFont(size=14),
            fg_color="#28a745"
        )
        self.start_button.pack(side="left", padx=5)
        
        # Stop button
        self.stop_button = ctk.CTkButton(
            button_frame,
            text="⏹ Stop Monitoring",
            command=self.stop_monitoring,
            width=180,
            height=40,
            font=ctk.CTkFont(size=14),
            fg_color="#dc3545",
            state="disabled"
        )
        self.stop_button.pack(side="left", padx=5)
        
        # Instructions
        instructions = ctk.CTkLabel(
            main_frame,
            text="After starting, change channel in-game.\nModules will be exported to your Desktop automatically.",
            font=ctk.CTkFont(size=11),
            text_color="gray",
            justify="center"
        )
        instructions.pack(pady=(20, 0))
        
    def start_monitoring(self):
        """Start the monitoring process."""
        if not self.interface_names:
            messagebox.showerror("Error", "No network interfaces available!")
            return
            
        # Get selected interface
        selected_idx = self.interface_dropdown.current() if hasattr(self.interface_dropdown, 'current') else 0
        try:
            selected_text = self.interface_dropdown.get()
            selected_idx = self.interface_names.index(selected_text)
        except (ValueError, AttributeError):
            selected_idx = 0
            
        interface_name = self.interfaces[selected_idx]['name']
        
        # Create and start monitor
        self.monitor = SimpleMonitor(
            interface_name=interface_name,
            on_export_callback=self._on_export_complete
        )
        self.monitor.start()
        
        # Update UI
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.interface_dropdown.configure(state="disabled")
        self.status_label.configure(
            text="⏳ Monitoring... Change channel in-game",
            text_color="#ffc107"
        )
        
        logger.info(f"Started monitoring on interface: {interface_name}")
        
    def stop_monitoring(self):
        """Stop the monitoring process."""
        if self.monitor:
            self.monitor.stop()
            self.monitor = None
            
        # Update UI
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.interface_dropdown.configure(state="readonly")
        self.status_label.configure(
            text="Stopped - Ready to start again",
            text_color="gray"
        )
        
        logger.info("Monitoring stopped")
        
    def _on_export_complete(self, count: int, filepath: str):
        """Callback when export is complete."""
        # Update UI from main thread
        self.after(0, lambda: self._show_export_success(count, filepath))
        
    def _show_export_success(self, count: int, filepath: str):
        """Show export success message."""
        self.status_label.configure(
            text=f"✅ Exported {count} modules!",
            text_color="#28a745"
        )
        
        # Stop monitoring automatically
        self.stop_monitoring()
        
        # Show success message
        messagebox.showinfo(
            "Export Complete",
            f"Successfully exported {count} modules!\n\nFile saved to:\n{filepath}"
        )


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
