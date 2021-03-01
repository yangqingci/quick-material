import bpy
from . import(ui_panel)
from .ui_panel import *

def register():
    bpy.utils.register_class(QuickMat_PT_view3d)


def unregister():
    pass