"""
Module Exporter for BPSR-AutoModules
Exports captured modules to a text file format compatible with the web optimizer.

Add this file to the BPSR-AutoModules project folder, then:
1. Import it in gui_app.py: from module_exporter import export_modules_to_file
2. Call it when you have captured modules: export_modules_to_file(captured_modules)

Or add an "Export" button to the GUI that calls this function.
"""

import os
from datetime import datetime
from typing import List, Optional
from module_types import ModuleInfo

# Attribute name to abbreviation mapping
ATTR_ABBREVIATIONS = {
    "Strength Boost": "SB",
    "Agility Boost": "AB",
    "Intellect Boost": "IB",
    "Special Attack": "SA",
    "Elite Strike": "ES",
    "Healing Boost": "HB",
    "Healing Enhance": "HE",
    "Cast Focus": "CaF",
    "Attack SPD": "AS",
    "Crit Focus": "CF",
    "Luck Focus": "LF",
    "Resistance": "R",
    "Armor": "A",
    "DMG Stack": "DS",
    "Agile": "AG",
    "Life Condense": "LC",
    "First Aid": "FA",
    "Life Wave": "LW",
    "Life Steal": "LS",
    "Team Luck & Crit": "TLC",
    "Final Protection": "FP",
}


def export_modules_to_file(
    modules: List[ModuleInfo],
    filename: Optional[str] = None,
    output_dir: Optional[str] = None
) -> str:
    """
    Export modules to a text file in the format: moduleN = [STAT:level, STAT:level, ...]
    
    Args:
        modules: List of ModuleInfo objects from the parser
        filename: Optional custom filename (default: modules_YYYYMMDD_HHMMSS.txt)
        output_dir: Optional output directory (default: current directory)
    
    Returns:
        Full path to the created file
    """
    if not modules:
        raise ValueError("No modules to export")
    
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"modules_{timestamp}.txt"
    
    # Determine output path
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, filename)
    else:
        filepath = filename
    
    # Build module strings
    lines = []
    for i, module in enumerate(modules, 1):
        parts = []
        for part in module.parts:
            # Convert full name to abbreviation
            abbrev = ATTR_ABBREVIATIONS.get(part.name, part.name)
            parts.append(f"{abbrev}:{part.value}")
        
        module_str = f"module{i} = [{', '.join(parts)}]"
        lines.append(module_str)
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    return os.path.abspath(filepath)


def get_modules_as_text(modules: List[ModuleInfo]) -> str:
    """
    Get modules as a formatted string (for clipboard copy).
    
    Args:
        modules: List of ModuleInfo objects
    
    Returns:
        Formatted string of all modules
    """
    if not modules:
        return ""
    
    lines = []
    for i, module in enumerate(modules, 1):
        parts = []
        for part in module.parts:
            abbrev = ATTR_ABBREVIATIONS.get(part.name, part.name)
            parts.append(f"{abbrev}:{part.value}")
        
        module_str = f"module{i} = [{', '.join(parts)}]"
        lines.append(module_str)
    
    return '\n'.join(lines)


# Example usage / test
if __name__ == "__main__":
    print("Module Exporter Utility")
    print("-" * 40)
    print("This module provides two functions:")
    print()
    print("1. export_modules_to_file(modules)")
    print("   - Exports modules to a timestamped .txt file")
    print("   - Returns the full path to the created file")
    print()
    print("2. get_modules_as_text(modules)")
    print("   - Returns modules as a string for clipboard")
    print()
    print("Import in gui_app.py:")
    print("  from module_exporter import export_modules_to_file")
    print()
    print("Then call when modules are captured:")
    print("  filepath = export_modules_to_file(captured_modules)")
