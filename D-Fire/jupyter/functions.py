import matplotlib.pyplot as plt


def checkLabel(path, label=0):
    """
    return image index if *.txt has content with label 0
    args:
        path(str): *.txt path
        label(int): target label
    return:
        imageIndex(str): image index if there is label 0
        None: if threr is no label 0
    """
    imageIndex = path.split('/')[-1].split('.')[0]
    with open(path, 'r') as f:
        labelRead = [x.strip() for x in f.readlines()]

    if len(labelRead) != 0:
        for line in labelRead:
            targetLabel = int(line[0])
            if targetLabel == 0:
                return imageIndex
    else:
        return None


def checkCoordinate(bbox, pascalFormat=False, imageWidth=None, imageHeight=None):
    """
    return bbox if bbox is wrong
    args:
        bbox(array):[xmin, ymin, xmax, ymax]
        pascalFormat (bool): use pascal format bbox else yolo format
        imageWidth(int):image width in pascal format
        imageHeight(int):image height in pascal format
    return:
        bbox(array): if bbox is wrong
        None: if bbox is right
    """

    
    # yolo format
    if pascalFormat == False:
        xcenter = bbox[0]
        ycenter = bbox[1]
        bboxWidth = bbox[2]
        bboxHeight = bbox[3]
        xmin = xcenter - bboxWidth / 2.0
        xmax = xcenter + bboxWidth / 2.0
        ymin = ycenter - bboxHeight / 2.0
        ymax = ycenter + bboxHeight / 2.0
        imageWidth = 1
        imageHeight = 1
    # pascal format
    else:
        xmin = bbox[0]
        ymin = bbox[1]
        xmax = bbox[2]
        ymax = bbox[3]
    # coordinate check
    if xmin < 0 or ymin < 0:
        print('xmin < 0 or ymin < 0')
        return bbox
    elif xmax > imageWidth or ymax > imageHeight:
        print('xmax > imageWidth or ymax > imageHeight')
        return bbox
    elif xmin >= xmax or ymin >= ymax:
        print('xmin >= xmax or ymin >= ymax')
        return bbox
    else:
        return None


def yolo_to_pascal(bbox, imageWidth, imageHeight):
    """
    bounding box transform: yolo -> pascal
    args:
        bbox(array): [x_center, y_center, width, height], normalized
        imageWidth(int): image width
        imageHeight(int): image height
    return:
        bbox(array): [xmin, ymin, xmax, ymax]
    """


    # yolo -> pascal normalized
    xcenter = bbox[0]
    ycenter = bbox[1]
    bboxWidth = bbox[2]
    bboxHeight = bbox[3]
    
    xmin = xcenter - bboxWidth / 2.0
    if xmin < 0:
        xmin = 0
    xmax = xcenter + bboxWidth / 2.0
    if xmax > 1:
        xmax = 1
    ymin = ycenter - bboxHeight / 2.0
    if ymin < 0:
        ymin = 0
    ymax = ycenter + bboxHeight / 2.0
    if ymax > 1:
        ymax = 1
    
    bbox[0] = xmin * imageWidth
    bbox[1] = ymin * imageHeight
    bbox[2] = xmax * imageWidth
    bbox[3] = ymax * imageHeight

    return bbox


def bbox_to_rect(bbox, color):
    return plt.Rectangle(xy=(bbox[0], bbox[1]), width=bbox[2]-bbox[0], height=bbox[3]-bbox[1], 
                         fill=False, edgecolor = color, linewidth = 1)