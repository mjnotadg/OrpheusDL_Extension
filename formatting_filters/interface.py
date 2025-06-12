from utils.models import ExtensionInformation
from .formatting_filters import OrpheusExtension

extension_settings = ExtensionInformation(
    extension_type="formatting",
    settings={
        "enabled": True,
        "source_subdirectories": True,
        "disc_subdirectories": False,
        "disc_format": "Disc {disc_number}",
        "cd_format": "CD {disc_number}",
        "remove_collectors_editions": False,
        "remove_live_recordings": True,
        "strict_artist_match": True,
        "ignore_different_artists": False
    }
) 