import typing as T
import math

import numpy as np

from src.data_model import Camera, DatasetSpec, Waypoint
from src.camera_utils import compute_image_footprint_on_surface, compute_ground_sampling_distance


def compute_distance_between_images(camera: Camera, dataset_spec: DatasetSpec) -> np.ndarray:
    """Compute the distance between images in the horizontal and vertical directions for specified overlap and sidelap.
    

    Args:
        camera (Camera): Camera model used for image capture.
        dataset_spec (DatasetSpec): user specification for the dataset.

    Returns:
        float: The distance between images in the horizontal direction.
        float: The distance between images in the vertical direction.
    """
    [footprint_x, footprint_y] = compute_image_footprint_on_surface(camera, dataset_spec.height)
    vertical_overlap = (1 - dataset_spec.sidelap) * footprint_y
    horizontal_overlap = (1 - dataset_spec.overlap) * footprint_x
    return np.array([horizontal_overlap, vertical_overlap])


def compute_speed_during_photo_capture(camera: Camera, dataset_spec: DatasetSpec, allowed_movement_px: float = 1) -> float:
    """Compute the speed of drone during an active photo capture to prevent more than 1px of motion blur.

    Args:
        camera (Camera): Camera model used for image capture.
        dataset_spec (DatasetSpec): user specification for the dataset.
        allowed_movement_px (float, optional): The maximum allowed movement in pixels. Defaults to 1 px.

    Returns:
        float: The speed at which the drone should move during photo capture.
    """
    distance = compute_ground_sampling_distance(camera, dataset_spec.height) * allowed_movement_px
    #the exposure time is given in milliseconds, so we need to convert it to seconds
    time = dataset_spec.exposure_time_ms / 1000
    return distance / time


def generate_photo_plan_on_grid(camera: Camera, dataset_spec: DatasetSpec) -> T.List[Waypoint]:
    """Generate the complete photo plan as a list of waypoints in a lawn-mower pattern.

    Args:
        camera (Camera): Camera model used for image capture.
        dataset_spec (DatasetSpec): user specification for the dataset.

    Returns:
        List[Waypoint]: scan plan as a list of waypoints.

    """
    plan = []

    max_distance = compute_distance_between_images(camera, dataset_spec)
    speed = compute_speed_during_photo_capture(camera, dataset_spec)
   
    images_x_axis = math.ceil(dataset_spec.scan_dimension_x / max_distance[0])
    images_y_axis = math.ceil(dataset_spec.scan_dimension_y  / max_distance[1])

    x_increment = dataset_spec.scan_dimension_x / images_x_axis
    y_increment = dataset_spec.scan_dimension_y / images_y_axis


    for i in range(images_y_axis):

        if i % 2 == 0:  # If the outer loop iteration is even, count forwards   
            for j in range(images_x_axis+1):
                x = 0 + (x_increment*j)
                y = 0 + (y_increment*i)
                s = speed
                plan.append(Waypoint(x,y,speed))
        else:  # If the outer loop iteration is odd, count backwards
            for j in range(images_x_axis, -1, -1):
                x = 0 + (x_increment*j)
                y = 0 + (y_increment*i)
                s = speed
                plan.append(Waypoint(x,y,speed))

    return plan

