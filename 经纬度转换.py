from pyproj import Transformer

if __name__ == '__main__':
    transformer = Transformer.from_crs("epsg:4326", "epsg:2361")
    # 北半球经纬度 （纬度，经度）
    # 南半球经纬度 （经度，纬度）
    x3, y3 = transformer.transform(30, 120)
    print("%.3f  %.3f" % (x3, y3))
