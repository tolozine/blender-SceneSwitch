![113091740103590_ pic](https://github.com/user-attachments/assets/f457132a-62d5-4180-b315-36d05fef7c94)

本脚本使用Deepseek进行创建,经过blender4.2.5验证.可以正常运行.其他版本未经过验证.


# 使用说明：
 1. 将脚本粘贴到Blender文本编辑器中并运行
 2. 使用 Ctrl + Shift + S 打开场景菜单
 3. 从列表中选择需要切换的场景



# 功能说明：
1. 注册了三个组件：
  ○ SCENE_OT_Switch：实际执行场景切换的操作符
  ○ SCENE_MT_SwitchMenu：显示所有场景列表的菜单
  ○ SCENE_OT_OpenSceneMenu：触发菜单显示的操作符
2. 快捷键设置为 Ctrl + Shift + S，按下后会弹出场景选择菜单
3. 菜单会列出当前文件中所有可用场景，点击即可切换
注意事项：
4. 如果快捷键冲突，可以在Blender的键位设置中搜索"打开场景菜单"进行修改
5. 菜单会自动包含所有场景（包括新建/删除的场景）
6. 需要保持脚本在Blender中运行（可以保存为插件方便长期使用）
要使用这个功能，只需在Blender中运行该脚本，然后使用 Ctrl + Shift + S 快捷键即可调出场景切换菜单。
