"""ENVLESSComfyUI-GeometryPack Prestartup Script (Clean version)."""

import os
import sys
import shutil
from pathlib import Path

# Try to import comfy_3d_viewers (optional helper)
try:
    from comfy_3d_viewers import copy_viewer
except ImportError:
    copy_viewer = None

SCRIPT_DIR = Path(__file__).resolve().parent
# COMFYUI_DIR is usually two levels up from custom_nodes/folder/
COMFYUI_DIR = SCRIPT_DIR.parent.parent

def copy_assets():
    """Copy assets from repo to ComfyUI input directory."""
    src = SCRIPT_DIR / "assets"
    dst = COMFYUI_DIR / "input" / "3d"
    
    if src.exists():
        dst.mkdir(parents=True, exist_ok=True)
        # Use glob to find all files and copy them recursively
        for item in src.rglob("*"):
            if item.is_file():
                relative_path = item.relative_to(src)
                target_path = dst / relative_path
                target_path.parent.mkdir(parents=True, exist_ok=True)
                if not target_path.exists() or item.stat().st_mtime > target_path.stat().st_mtime:
                    shutil.copy2(item, target_path)
        print(f"Copied assets from {src} to {dst}")

def setup_viewers():
    """Copy 3D viewers if the helper package is available."""
    if copy_viewer is None:
        return

    viewers = [
        "viewer", "vtk", "vtk_batch", "vtk_textured", "pointcloud_vtk",
        "multi", "dual", "dual_slider", "dual_textured",
        "uv", "pbr", "gaussian",
        "fbx", "fbx_debug", "fbx_compare",
        "bvh", "fbx_animation", "compare_smpl_bvh",
        "text_report",
    ]
    for viewer in viewers:
        try:
            copy_viewer(viewer, SCRIPT_DIR / "web")
        except Exception as e:
            # Silent fail for individual viewers is okay
            pass

def setup_dynamic_widgets():
    """Copy dynamic widgets JS if available."""
    try:
        from comfy_dynamic_widgets import get_js_path
        src = Path(get_js_path())
        if src.exists():
            dst = SCRIPT_DIR / "web" / "js" / "dynamic_widgets.js"
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime:
                shutil.copy2(src, dst)
    except ImportError:
        pass

if __name__ == "__main__":
    copy_assets()
    setup_viewers()
    setup_dynamic_widgets()
