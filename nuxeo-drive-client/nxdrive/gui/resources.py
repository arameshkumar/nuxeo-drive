"""Helper to lookup UI resources from package"""

import os
from nxdrive.logging_config import get_logger
from nxdrive.utils import find_resource_dir

log = get_logger(__name__)


def find_icon(icon_filename):
    """Find the FS path of an icon in various OS binary packages"""
    import nxdrive
    nxdrive_path = os.path.dirname(nxdrive.__file__)
    icons_path = os.path.join(nxdrive_path, 'data', 'icons')
    icons_dir = find_resource_dir('icons', icons_path)

    if icons_dir is None:
        log.warning("Could not find icon file %s as icons directory"
                    " could not be found",
                    icon_filename)
        return None

    icon_filepath = os.path.join(icons_dir, icon_filename)
    if not os.path.exists(icon_filepath):
        log.warning("Could not find icon file: %s", icon_filepath)
        return None

    return icon_filepath
