import dxfgrabber

file = './data/cat.dxf'
dxf = dxfgrabber.readfile(file)


entities = dxf.entities
blocks = dxf.blocks
headers = dxf.header

polylines = [entity for entity in entities if entity.dxftype == 'POLYLINE']
for polyline in polylines:
    print(polyline.points)



