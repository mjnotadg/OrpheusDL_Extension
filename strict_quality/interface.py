from utils.models import ExtensionInformation
from .strict_quality import OrpheusExtension

extension_settings = ExtensionInformation(
    extension_type="quality",
    settings={
        "enabled": True,
        "strict_quality_download": True,
        "log_quality_errors": True,
        "album_folder_logging": True,
        "clear_error_messages": True
    }
) 