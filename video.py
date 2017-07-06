
"""
Video related utility functions
"""

import numpy as np
import settings
import blosc


def write_blp(data, file_name):
    file_name += '.blp'
    print('Saving %s' % file_name)
    bytes_array = data.tostring()
    packed = blosc.compress(bytes_array)
    with open(file_name, 'wb') as fd:
        fd.write(packed)


def read_blp(file_name, shape):
    with open(file_name, 'rb') as fd:
        bytes_array = fd.read()
        unpacked = blosc.decompress(bytes_array)
    return np.frombuffer(unpacked, dtype=np.uint8).reshape((shape))


def write_data(vid, file_name):
    write_blp(vid, file_name)


def clip(image, min_bound, max_bound):
    image[image > max_bound] = max_bound
    image[image < min_bound] = min_bound


def normalize(image, min_bound, max_bound):
    image = np.float32(image)
    image = (image - min_bound) / (max_bound - min_bound)
    assert image[image > 1].sum() == 0
    assert image[image < 0].sum() == 0
    image *= 255
    return np.uint8(np.rint(image))


def copy_to_frame(video, frame_shape):
    in_shape = video.shape
    out_shape = frame_shape
    frame = np.zeros(out_shape, dtype=video.dtype)
    for idx in range(3):
        assert in_shape[idx] <= out_shape[idx]
    starts = [(out_shape[i] - in_shape[i]) // 2 for i in range(3)]
    ends = [starts[i] + in_shape[i] for i in range(3)]
    frame[starts[0]:ends[0], starts[1]:ends[1], starts[2]:ends[2]] = video
    return frame
