import bpy
import os

current_dir = os.path.dirname(bpy.data.filepath)

blend_file_path = os.path.join(current_dir, "Lantern.blend")
collection_name = "Lantern"

collection_folder = os.path.join(blend_file_path, "Collection")
collection_path = os.path.join(collection_folder, collection_name)

bpy.ops.wm.append(
    filepath=collection_path,
    directory=collection_folder,
    filename=collection_name
)