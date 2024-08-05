import matplotlib.pyplot as plt
import numpy as np
import math

def bbox_to_rect(bbox, color):
    return plt.Rectangle(xy=(bbox[0], bbox[1]), width=bbox[2]-bbox[0], height=bbox[3]-bbox[1], 
                         fill=False, edgecolor = color, linewidth = 1)


def bbox_resize(bbox, widthRatio, heightRatio):
    """
    resize bounding bbox
    args:
        bbox(array): [xmin, ymin, xmax, ymax]
        widthRatio(float): newWidth / oldWidth
        heightRatio(float): newHeight / oldHeight
    return:
        bboxResized(array): resized bbox
    """
    bboxResized = np.array([0, 0, 0, 0])
    bboxResized[0] = bbox[0] * widthRatio
    bboxResized[2] = bbox[2] * widthRatio
    bboxResized[1] = bbox[1] * heightRatio
    bboxResized[3] = bbox[3] * heightRatio

    return bboxResized


def caculate_area(bbox):
    """
    caculate area of bbox
    args:
        bbox(array): pascal format bounding box
    return:
        area(array): array of area of bounding box
    """
    area = (bbox[:,2] - bbox[:,0]) * (bbox[:,3] - bbox[:,1])

    return area


def get_iou(bb1, bb2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters:
    bb1 : dict
        Dictionary with keys: {'x1', 'y1', 'x2', 'y2'}
        (x1, y1) represents the top-left corner, and (x2, y2) represents the bottom-right corner.
    bb2 : dict
        Dictionary with keys: {'x1', 'y1', 'x2', 'y2'}
        (x1, y1) represents the top-left corner, and (x2, y2) represents the bottom-right corner.

    Returns:
    float
        IoU value in the range [0, 1].
    """
    assert bb1['x1'] < bb1['x2']
    assert bb1['y1'] < bb1['y2']
    assert bb2['x1'] < bb2['x2']
    assert bb2['y1'] < bb2['y2']

    # Calculate coordinates of the intersection rectangle
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])

    # If intersection is empty, return 0
    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # Calculate intersection area
    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    # Calculate areas of both bounding boxes
    bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
    bb2_area = (bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1'])

    # Calculate IoU
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    return iou


def filter_overlapping_boxes(bboxes, threshold=0):
    """
    select bbox with biggest area in repetitive bboxes.
    args：
    bboxes(array): shape: (N, 4) with pascal format
    threshold(float): bboxes ious larger than threshold with each other will be compared areas
    return：
    filtered_bboxes(array): bboxes with no repetition
    """
    # caculate areas of all bboxes
    areas = (bboxes[:, 2] - bboxes[:, 0]) * (bboxes[:, 3] - bboxes[:, 1])

    # mask
    keep_mask = np.ones(len(bboxes), dtype=bool)

    for i in range(len(bboxes)):
        if keep_mask[i]:
            for j in range(i + 1, len(bboxes)):
                if keep_mask[j]:
                    iou = get_iou(
                        {'x1': bboxes[i, 0], 'y1': bboxes[i, 1], 'x2': bboxes[i, 2], 'y2': bboxes[i, 3]},
                        {'x1': bboxes[j, 0], 'y1': bboxes[j, 1], 'x2': bboxes[j, 2], 'y2': bboxes[j, 3]}
                    )
                    # there is repetition
                    if iou > threshold:
                        # leave bbox with biggest area
                        if areas[j] > areas[i]:
                            keep_mask[i] = False
                        else:
                            keep_mask[j] = False

    filtered_bboxes = bboxes[keep_mask]
    return filtered_bboxes