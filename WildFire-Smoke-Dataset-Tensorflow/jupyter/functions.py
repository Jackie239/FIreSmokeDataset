import matplotlib.pyplot as plt


def bbox_to_rect(bbox, color):
    return plt.Rectangle(xy=(bbox[0], bbox[1]), width=bbox[2]-bbox[0], height=bbox[3]-bbox[1], 
                         fill=False, edgecolor = color, linewidth = 1)