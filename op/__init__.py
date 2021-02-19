import bpy



from .op_action import *


classes = (
ObjectMoveX,
ObjectMoveY
)


def register():
	for cls in classes:
		bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.register_class(cls)
