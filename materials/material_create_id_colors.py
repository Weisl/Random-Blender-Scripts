"""creates ID color materials """

fakeUser = True

import bpy


def makeMaterial(name, diffuse):
    b_mat_exists = False
    for mat in bpy.data.materials:
        if mat.name == name:
            b_mat_exists = True

    if b_mat_exists == False:
        mat = bpy.data.materials.new(name)
        mat.diffuse_color = diffuse
        if fakeUser == True:
            mat.use_fake_user = True
    return mat


def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)


def run():
    # Create two materials
    red = makeMaterial('ID_Red', (1, 0, 0, 1))
    blue = makeMaterial('ID_Blue', (0, 0, 1, 1))
    green = makeMaterial('ID_Green', (0, 1, 0, 1))
    yellow = makeMaterial('ID_Yeldalow', (1, 1, 0, 1))
    cyan = makeMaterial('ID_Cyan', (0, 1, 1, 1))
    magenta = makeMaterial('ID_Magenta', (1, 0, 1, 1))
    rosa = makeMaterial('ID_Rosa', (1, 0.5, 0.5, 1))
    lightgreen = makeMaterial('ID_Lightgreen', (0.5, 1, 0.5, 1))
    orange = makeMaterial('ID_Orange', (1, 0.5, 0, 1))
    pink = makeMaterial('ID_Pink', (1, 0, 0.5, 1))
    shinygreen = makeMaterial('ID_Shyinigreen', (0.5, 1, 0, 1))
    bluegreen = makeMaterial('ID_Bluegreen', (0, 1, 0.5, 1))
    deepblue = makeMaterial('ID_Deepblue', (0, 0.5, 1, 1))
    violet = makeMaterial('ID_Violet', (0.5, 0, 1, 1))
    white = makeMaterial('ID_White', (1, 1, 1, 1))
    grey = makeMaterial('ID_Grey', (0.5, 0.5, 0.5, 1))
    darkgrey = makeMaterial('ID_Lightgrey', (0.75, 0.75, 0.75, 1))
    darkgrey = makeMaterial('ID_DarkGrey', (0.25, 0.25, 0.25, 1))


if __name__ == "__main__":
    run()
