import os
from typing import Optional
from utils.models import TrackInfo


class OrpheusExtension:
    """Enhanced Logging Extension for OrpheusDL"""
    
    def __init__(self, settings: dict):
        self.settings = settings
        self.enabled = settings.get("enabled", True)
        self.log_unavailable_tracks = settings.get("log_unavailable_tracks", True)
        self.album_folder_logging = settings.get("album_folder_logging", True)
        self.clear_error_messages = settings.get("clear_error_messages", True)
        
    def log_unavailable_track(self, track_id: str, track_info: TrackInfo, album_path: str):
        """Log unavailable tracks to error.txt in the album folder"""
        if not self.log_unavailable_tracks or not self.enabled:
            return
            
        error_msg = f'Unavailable: {track_info.artists[0] if track_info.artists else "Unknown"} [{track_info.artist_id}]/{track_info.album} [{track_info.album_id}]/{track_info.name} [{track_id}]'
        
        # Create error.txt in the album folder
        if self.album_folder_logging and album_path:
            error_file = os.path.join(album_path, 'error.txt')
        else:
            error_file = 'unavailable_tracks.log'
            
        with open(error_file, 'a', encoding='utf-8') as logf:
            logf.write(f'{error_msg}\n')
            
    def get_extension_info(self):
        """Return information about this extension"""
        return {
            "name": "Enhanced Logging",
            "version": "1.0.0",
            "description": "Provides enhanced logging functionality for tracking unavailable tracks",
            "author": "OrpheusDL Extension System",
            "features": [
                "Separate log files for unavailable tracks",
                "Album-specific logging",
                "Clear error messages",
                "Configurable settings"
            ]
        } 