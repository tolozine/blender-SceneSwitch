import bpy
class SCENE_OT_Switch(bpy.types.Operator):
    """切换场景操作"""
    bl_idname = "scene.switch"
    bl_label = "切换场景"
    
    scene_name: bpy.props.StringProperty()
    
    def execute(self, context):
        if self.scene_name in bpy.data.scenes:
            context.window.scene = bpy.data.scenes[self.scene_name]
            return {'FINISHED'}
        self.report({'ERROR'}, "场景不存在")
        return {'CANCELLED'}
class SCENE_MT_SwitchMenu(bpy.types.Menu):
    """场景切换菜单"""
    bl_idname = "SCENE_MT_switch_menu"
    bl_label = "选择场景"
    
    def draw(self, context):
        layout = self.layout
        for scene in bpy.data.scenes:
            op = layout.operator(SCENE_OT_Switch.bl_idname, text=scene.name)
            op.scene_name = scene.name
class SCENE_OT_OpenSceneMenu(bpy.types.Operator):
    """打开场景菜单"""
    bl_idname = "scene.open_scene_menu"
    bl_label = "打开场景菜单"
    
    def execute(self, context):
        bpy.ops.wm.call_menu(name=SCENE_MT_SwitchMenu.bl_idname)
        return {'FINISHED'}
# 快捷键注册
addon_keymaps = []
def register():
    bpy.utils.register_class(SCENE_OT_Switch)
    bpy.utils.register_class(SCENE_MT_SwitchMenu)
    bpy.utils.register_class(SCENE_OT_OpenSceneMenu)
    
    # 配置快捷键
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new(
            SCENE_OT_OpenSceneMenu.bl_idname, 
            'S', 
            'PRESS', 
            ctrl=True, 
            shift=True
        )
        addon_keymaps.append((km, kmi))
def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    bpy.utils.unregister_class(SCENE_OT_OpenSceneMenu)
    bpy.utils.unregister_class(SCENE_MT_SwitchMenu)
    bpy.utils.unregister_class(SCENE_OT_Switch)
if __name__ == "__main__":
    register()
# 使用说明：
# 1. 将脚本粘贴到Blender文本编辑器中并运行
# 2. 使用 Ctrl + Shift + S 打开场景菜单
# 3. 从列表中选择需要切换的场景
