"""
GestaltBoardで作成したプロッターをDXFファイルの図通りに動かすためのプログラム。
このプログラムはFabAcademy2017のMachine Designの課題のために作成

Author : Mio Kato @ FabLab Kamakura 
Date : 2017/04/07
"""
import dxfgrabber


def get_xy_points(file):
    """
    DXF形式で頂点のある図形のデータを渡すと、頂点のx,y座標をタプルで格納したリストを返す
    :param file: dxf file
    :return: tuple's list of vertices(x,y,z) 
    """
    dxf = dxfgrabber.readfile(file)
    entities = dxf.entities
    # list of x,y,z coodinates
    xyz_points = [entity.points for entity in entities]
    # list of x,y coodinates
    # list_of_vertices[0] == ２次元配列のうち利用するのは最初の一つだけ。
    xy_points = [vertex[0:2] for vertex in xyz_points[0]]

    return xy_points


