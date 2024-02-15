# Messys-Blender-Scripts
Sometimes I want to do a repetitive task in blender like 100 times and I can't find an addon to do it for me so I make a script instead, I'll post those scripts here for ya'll to use.
Whenever I make a new one I'll update this. These scripts should all work with multiple objects selected and it will complete the action on every mesh selected one at a time.

## applyShapeKey.py
Takes the current shape key configuration and applied it to the mesh, deletes all shape keys after

## cleanWeights.py
* First cleans vertex bone weights below .01 (customizable) so long as a vertex has other associated bone weights
* Then normalizes in order to keep weights as close to the intended weight as possible
* Then limits bone vertex groups to 4
* Then does a final normalization to ensure weights all add to 1.0

## keepNormalMerge.py
Makes a duplicate of a mesh, then merges vertices by distance (removes doubles). Data transfers the old normals back then applies and deletes the duplicate

# There might be issues with these scripts. Feel free to make an issue, no guarantee I'll come back to it though
