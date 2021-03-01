import bpy
from bpy.types import Panel, Menu, UIList, PropertyGroup
from quick_material import op


class QuickMat_PT_view3d(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QuickMat'
    bl_idname = 'Quick_Mat'
    bl_label = 'Quick Material'
    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.label(text="你好UI",icon="ACTION")
        layout.operator("object.move_x", text="X轴移动")