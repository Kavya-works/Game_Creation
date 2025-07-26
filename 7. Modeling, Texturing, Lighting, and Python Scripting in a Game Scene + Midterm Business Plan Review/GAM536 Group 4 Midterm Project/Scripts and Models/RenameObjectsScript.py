import bpy

# Prefix to add to selected objects
new_name_prefix = "Lantern"

# Loop through selected objects and rename
for i, obj in enumerate(bpy.context.selected_objects, start=1):
    obj.name = f"{new_name_prefix}_{i:03}"