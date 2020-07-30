# Script for Blender, run this in the Blender console under the scripting tab
# This script should remove the blur on the glTF models
# If this script  did not work then replace “baseColorTexture.tex_img” with “Image Texture”

import bpy

for i in bpy.data.materials:
    try:
        i.node_tree.nodes["baseColorTexture.tex_img"].interpolation = “Closest”
    except:
        pass