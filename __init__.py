"""Node registration (Clean version)."""

# Import mappings from sub-packages in the nodes directory
from .nodes.main import NODE_CLASS_MAPPINGS as MAIN_CLASS, NODE_DISPLAY_NAME_MAPPINGS as MAIN_DISPLAY
from .nodes.blender import NODE_CLASS_MAPPINGS as BLENDER_CLASS, NODE_DISPLAY_NAME_MAPPINGS as BLENDER_DISPLAY
from .nodes.gpu import NODE_CLASS_MAPPINGS as GPU_CLASS, NODE_DISPLAY_NAME_MAPPINGS as GPU_DISPLAY

# Combine all mappings using dictionary unpacking
# (Order matters: later keys override earlier ones if there are duplicates)
NODE_CLASS_MAPPINGS = {
    **MAIN_CLASS,
    **BLENDER_CLASS,
    **GPU_CLASS,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **MAIN_DISPLAY,
    **BLENDER_DISPLAY,
    **GPU_DISPLAY,
}

# Optional helper: write mappings for JS frontend (comfy-dynamic-widgets)
try:
    from comfy_dynamic_widgets import write_mappings
    write_mappings(NODE_CLASS_MAPPINGS, __file__)
except ImportError:
    pass

# Custom nodes in ComfyUI use WEB_DIRECTORY to serve static files
WEB_DIRECTORY = "./web"

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]
