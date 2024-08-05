import xml.etree.ElementTree as ET


def init_xml(xmlPath, datasetFolder, imageName, database, imageWidth, imageHeight, imageDepth=3):
    """
    init xml
    args:
        xmlPath(str): xml path
        datasetFolder(str): dataset folder name
        imageName(str): image name
        database(str): database name
        imageWidth(int): image width
        imageHeight(int): image height
        depth(int): image depth
    """
    # init xml
    annotation = ET.Element('annotation')
    folder = ET.SubElement(annotation,'folder')
    folder.text = str(datasetFolder)
    filename = ET.SubElement(annotation, 'filename')
    filename.text = '{}.jpg'.format(imageName)
    source = ET.SubElement(annotation, 'source')
    database = ET.SubElement(source, 'database')
    database.text = database
    author = ET.SubElement(annotation, 'author')
    author.text = 'fengguohao@mail.shiep.edu.cn'
    size = ET.SubElement(annotation, 'size')
    width = ET.SubElement(size, 'width')
    width.text = str(imageWidth)
    height = ET.SubElement(size, 'height')
    height.text = str(imageHeight)
    depth = ET.SubElement(size, 'depth')
    depth.text = str(imageDepth)        
    tree = ET.ElementTree(annotation)
    tree.write(xmlPath)
    

def add_object(tree, bbox, className):
    """
    add object in xml file
    args:
        tree: output of parse
        bbox(array): [xmin, ymin, xmax, ymax]
        className(str): object class
    """
    annotation = tree.getroot()
    object = ET.SubElement(annotation, 'object')
    name = ET.SubElement(object, 'name')
    name.text = className
    difficult = ET.SubElement(object, 'difficult')
    difficult.text = '0'
    bndbox = ET.SubElement(object, 'bndbox')
    xmin = ET.SubElement(bndbox, 'xmin')
    xmin.text = str(bbox[0])
    ymin = ET.SubElement(bndbox, 'ymin')
    ymin.text = str(bbox[1])
    xmax = ET.SubElement(bndbox, 'xmax')
    xmax.text = str(bbox[2])
    ymax = ET.SubElement(bndbox, 'ymax')
    ymax.text = str(bbox[3])


def prettyXml(element, indent, newline, level = 0): 
    """
    elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行   
    """
    # 判断element是否有子元素
    if element:
        # 如果element的text没有内容      
        if element.text == None or element.text.isspace():     
            element.text = newline + indent * (level + 1)      
        else:    
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)    
    # 此处两行如果把注释去掉，Element的text也会另起一行 
    #else:     
        #element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level    
    temp = list(element) # 将elemnt转成list    
    for subelement in temp:    
        # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
        if temp.index(subelement) < (len(temp) - 1):     
            subelement.tail = newline + indent * (level + 1)    
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个    
            subelement.tail = newline + indent * level   
        # 对子元素进行递归操作 
        prettyXml(subelement, indent, newline, level = level + 1) 
