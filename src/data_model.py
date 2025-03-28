"""Data models for the camera and user specification."""
from dataclasses import dataclass

@dataclass
class Camera:
    """
    Data model for a simple pinhole camera.

    
    References: 
    - https://github.com/colmap/colmap/blob/3f75f71310fdec803ab06be84a16cee5032d8e0d/src/colmap/sensor/models.h#L220
    - https://en.wikipedia.org/wiki/Pinhole_camera_model
    """
    def __init__(self,
                 fx:float, 
                 fy:float,
                 cx:float, 
                 cy:float, 
                 sensor_size_x_mm:float, 
                 sensor_size_y_mm:float, 
                 image_size_x_px:int, 
                 image_size_y_px:int):
        self.fx = fx
        self.fy = fy
        self.cx = cx
        self.cy = cy
        self.sensor_size_x_mm = sensor_size_x_mm
        self.sensor_size_y_mm = sensor_size_y_mm
        self.image_size_x_px = image_size_x_px
        self.image_size_y_px = image_size_y_px    

@dataclass
class DatasetSpec:
    """
    Data model for specifications of an image dataset.
    """
    pass


@dataclass
class Waypoint:
    """
    Waypoints are positions where the drone should fly to and capture a photo.
    """
    pass