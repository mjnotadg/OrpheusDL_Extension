from utils.models import ExtensionInformation
from .enhanced_logging import OrpheusExtension

extension_settings = ExtensionInformation(
    extension_type="logging",
    settings={
        "enabled": True,
        "log_unavailable_tracks": True,
        "album_folder_logging": True,
        "clear_error_messages": True
    }
) 