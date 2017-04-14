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
    polylines = [entity for entity in entities if entity.dxftype == 'POLYLINE']
    xy_points_list = []
    for polyline in polylines:
        xy_points = [list(point[0:2]) for point in polyline.points]
        xy_points_list.append(xy_points)

    return xy_points_list


if __name__ == '__main__':
    file = './data/cat.dxf'
    points = get_xy_points(file)
    print(points)
