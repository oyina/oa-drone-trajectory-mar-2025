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
    fx:float 
    fy:float
    cx:float 
    cy:float 
    sensor_size_x_mm:float 
    sensor_size_y_mm:float 
    image_size_x_px:int 
    image_size_y_px:int
     
@dataclass
class DatasetSpec:
    """
    Data model for specifications of an image dataset.

    Args:
        overlap: (float) Ratio (0 to 1) of scene shared between two consecutive images
        sidelap: (float)  Ratio (0 to 1) of scene shared between two images in adjacent rows
        height: (float)  Height of the scan above the ground (in meters)
        scan_dimension_x: (int)  Horizontal size of the rectangle to be scanned (in meters)
        scan_dimension_y: (int)  Vertical size of the rectangle to be scanned (in meters)
        exposure_time_ms: (int)  Exposure time for each image (in milliseconds)
    """
    overlap: float
    sidelap: float
    height: float
    scan_dimension_x: int
    scan_dimension_y: int
    exposure_time_ms: int



@dataclass
class Waypoint:
    """
    Waypoints are positions where the drone should fly to and capture a photo.

    Args:
        x: (float) X coordinate of the waypoint
        y: (float) Y coordinate of the waypoint
        speeed: (float) Speed of the drone at the waypoint
    """
    x: float
    y: float
    speed: float