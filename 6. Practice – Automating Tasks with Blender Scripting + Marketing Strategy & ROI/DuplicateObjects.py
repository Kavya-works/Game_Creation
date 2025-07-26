import bpy
import math

# Parameters
collection_name = "Lantern"
number_of_lanterns = 8
radius = 6

# Get original collection
original_collection = bpy.data.collections.get(collection_name)

if not original_collection:
    print(f"Collection '{collection_name}' not found.")
else:
    for i in range(number_of_lanterns):
        angle = (2 * math.pi / number_of_lanterns) * i
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius

        # Duplicate all objects in the collection
        new_objs = []
        for obj in original_collection.objects:
            new_obj = obj.copy()
            new_obj.data = obj.data.copy()
            new_obj.location.x += x
            new_obj.location.y += y
            bpy.context.collection.objects.link(new_obj)
            new_objs.append(new_obj)