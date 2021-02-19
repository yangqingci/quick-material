import bpy
from bpy.props import *
from bpy.types import Operator


class ObjectMoveX(Operator):
    """My Object Moving X Script"""      # 将此用作菜单项和按钮的工具提示.
    bl_idname = "object.move_x"
    bl_label = "Move X by One"
    bl_description = ""
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0

        return{'FINISHED'}


class ObjectMoveY(Operator):
    """My Object Moving Y Script"""      # 将此用作菜单项和按钮的工具提示.
    bl_idname = "object.move_y"
    bl_label = "Move Y by One"
    bl_description = ""
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
        scene = context.scene
        for obj in scene.objects:
            obj.location.y += 1.0

        return{'FINISHED'}