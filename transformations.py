#   Rigid Body Transformations
import numpy as np

#   Translation function
def transl(x, y, z):
    """
    Returns a homogenoeous matrix given x, y, z
    ---
    Parameters
    ---
    x: x offset
    y: y offset
    z: z offset
    ---
    Returns
    ---
    transform: 4x4 transformation matrix
    """
    transform = np.eye(4)
    transform[0][3] = x
    transform[1][3] = y
    transform[2][3] = z

    return transform

#   Rotation function
def rotx(roll):
    """
    Returns rotation matrix given roll angle
    ...
    Parameters
    ...
    roll: roll angle
    ...
    Returns
    ...
    rotation: 3x3 rotation matrix
    """
    rotation = np.eye(3)
    rotation[1][1] = np.cos(roll)
    rotation[1][2] = -np.sin(roll)
    rotation[2][1] = np.sin(roll)
    rotation[2][2] = np.cos(roll)

    return rotation

#   Rotation function
def roty(pitch):
    """
    Returns rotation matrix given roll angle
    ...
    Parameters
    ...
    roll: roll angle
    ...
    Returns
    ...
    rotation: 3x3 rotation matrix
    """
    rotation = np.eye(3)
    rotation[0][0] = np.cos(pitch)
    rotation[0][2] = np.sin(pitch)
    rotation[2][0] = -np.sin(pitch)
    rotation[2][2] = np.cos(pitch)

    return rotation

#   Rotation function
def rotz(yaw):
    """
    Returns rotation matrix given roll angle
    ...
    Parameters
    ...
    roll: roll angle
    ...
    Returns
    ...
    rotation: 3x3 rotation matrix
    """
    rotation = np.eye(3)
    rotation[0][0] = np.cos(yaw)
    rotation[0][1] = -np.sin(yaw)
    rotation[1][0] = np.sin(yaw)
    rotation[1][1] = np.cos(yaw)

    return rotation

#   Function to convert roll pitch and yaw to transformation
def rpy2tr(roll, pitch, yaw):
    """
    Returns transformation matrix given
    roll pitch yaw
    ...
    Parameters:
    ...
    roll: roll angle
    pitch: pitch angle
    yaw: yaw angle
    ...
    Returns:
    ...
    transformation: 4x4 transformation matrix
    """

    rotation_z = rotz(yaw)
    rotation_y = roty(pitch)
    rotation_x = rotx(roll)

    rotation = rotation_z @ rotation_y @ rotation_x

    transformation = np.eye(4)
    transformation[:3,:3] = rotation

    return transformation

#   Function to convert transformation to roll pitch yaw
def tr2rpy(transformation):
    """
    Returns roll, pitch and yaw given
    transformation matrix
    ...
    Parameters:
    ...
    transformation: transformation matrix
    ...
    Returns:
    ...
    roll: roll angle
    pitch: pitch angle
    yaw: yaw angle
    """
    rotation = transformation[:3, :3]

    yaw   = np.arctan2(rotation[1][0], rotation[0][0])
    pitch = np.arctan2(-rotation[2][0],
            np.sqrt(rotation[2][1] ** 2 + rotation[2][2] ** 2))
    roll  = np.arctan2(rotation[2][1], rotation[2][2])

    return roll, pitch, yaw



