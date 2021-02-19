bl_info = {
    "name": "Quick Meaterial",
    "author": "yangqingci",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "3D View > Property Shelf(N Key) > Tools > Quick Meaterial",
    "description": "Add materials to objects quickly",
    "warning": "",
    "wiki_url": "",
    "category": "3D View",
}

import bpy
import logging
from . import op
from . import ui


def register():
    op.register()
    ui.register()


def unregister():
    op.unregister()
    ui.unregister()

if __name__ == "__main__":
    register()