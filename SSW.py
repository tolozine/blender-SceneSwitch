
bl_info = {
    "name": "Blender Switch Scene",
    "blender": (3, 0, 0),
    "category": "Render",
    "version": (1, 0),
    "author": "tolozine",
    "description": "通过shift+alt+S 调出场景列表菜单,进行快速切换",
}


import bpy

# 操作符：执行场景切换
class SCENE_OT_Switch(bpy.types.Operator):
    bl_idname = "scene.switch"
    bl_label = "Switch Scene"
    scene_name: bpy.props.StringProperty()

    def execute(self, context):
        scene = bpy.data.scenes.get(self.scene_name)
        if scene:
            context.window.scene = scene
        return {'FINISHED'}

# 菜单类：显示所有场景
class SCENE_MT_SwitchMenu(bpy.types.Menu):
    bl_idname = "SCENE_MT_switch_menu"
    bl_label = "Switch Scene"

    def draw(self, context):
        layout = self.layout
        for scene in bpy.data.scenes:
            layout.operator("scene.switch", text=scene.name).scene_name = scene.name

# 操作符：触发场景菜单显示
class SCENE_OT_OpenSceneMenu(bpy.types.Operator):
    bl_idname = "scene.open_scene_menu"
    bl_label = "Open Scene Menu"
    bl_description = "Open a menu to switch scenes"

    def execute(self, context):
        bpy.ops.wm.call_menu(name=SCENE_MT_SwitchMenu.bl_idname)
        return {'FINISHED'}

# 注册快捷键
def register_keymap():
    wm = bpy.context.window_manager
    keymap = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
    keymap_items = keymap.keymap_items.new(SCENE_OT_OpenSceneMenu.bl_idname, 'S', 'PRESS', shift=True, alt=True)
    return keymap, keymap_items

# 注销快捷键
def unregister_keymap():
    wm = bpy.context.window_manager
    keymap = wm.keyconfigs.addon.keymaps.get('Window')
    if keymap:
        for kmi in keymap.keymap_items:
            if kmi.idname == SCENE_OT_OpenSceneMenu.bl_idname:
                keymap.keymap_items.remove(kmi)
                break

# 注册/注销类和快捷键
classes = (
    SCENE_OT_Switch,
    SCENE_MT_SwitchMenu,
    SCENE_OT_OpenSceneMenu,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # 注册快捷键
    register_keymap()

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    # 注销快捷键
    unregister_keymap()

if __name__ == "__main__":
    register()
