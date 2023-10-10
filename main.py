bl_info = {
    "name": "Simple Node Tooltip",
    "description": "Display tooltip for selected node in the Node Editor.",
    "author": "Vincent",
    "version": (1, 1),
    "blender": (2, 93, 0),
    "location": "Node Editor > Right-Click Menu",
    "category": "Node"
}


import bpy

class SimpleNodeTooltipAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    enable_addon: bpy.props.BoolProperty(
        name="Enable addon",
        default=True,
    )
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "enable_addon")

class SimpleNodeTooltipOperator(bpy.types.Operator):
    """Display tooltip for selected node in the Node Editor."""
    bl_idname = "node.simple_tooltip"
    bl_label = "Simple Node Tooltip"

    @classmethod
    def description(cls, context, properties):
        node = context.space_data.edit_tree.nodes.active
        if node is not None and node.bl_description:
            return node.bl_description
        return "No description available"

    def execute(self, context):
        node = context.space_data.edit_tree.nodes.active
        if node is not None:
            tooltip_text = node.bl_label + ": " + node.bl_description + self.description(context, self.properties)
            self.report({'INFO'}, tooltip_text)
            print(node.bl_description)
            print(tooltip_text)
            print('hello')
        return {'FINISHED'}



def simple_node_tooltip_menu(self, context):
    layout = self.layout
    layout.operator(SimpleNodeTooltipOperator.bl_idname)

def register():
    bpy.utils.register_class(SimpleNodeTooltipOperator)
    bpy.utils.register_class(SimpleNodeTooltipAddonPreferences)
    bpy.types.NODE_MT_context_menu.append(simple_node_tooltip_menu)

def unregister():
    bpy.utils.unregister_class(SimpleNodeTooltipOperator)
    bpy.utils.unregister_class(SimpleNodeTooltipAddonPreferences)
    bpy.types.NODE_MT_context_menu.remove(simple_node_tooltip_menu)

if __name__ == "__main__":
    register()