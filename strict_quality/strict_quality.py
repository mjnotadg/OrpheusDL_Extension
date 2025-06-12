import os
from typing import Optional, Dict, Any
from utils.models import TrackInfo, AlbumInfo, QualityEnum, CodecEnum


class OrpheusExtension:
    """Strict Quality Download Extension for OrpheusDL"""
    
    def __init__(self, settings: dict):
        self.settings = settings
        self.enabled = settings.get("enabled", True)
        self.strict_quality_download = settings.get("strict_quality_download", True)
        self.log_quality_errors = settings.get("log_quality_errors", True)
        self.album_folder_logging = settings.get("album_folder_logging", True)
        self.clear_error_messages = settings.get("clear_error_messages", True)
        
    def validate_track_quality(self, track_info: TrackInfo, requested_quality: str) -> tuple[bool, str]:
        """Validate if track meets quality requirements"""
        if not self.enabled or not self.strict_quality_download:
            return True, ""
            
        # Get track quality
        track_quality = getattr(track_info, 'quality', None)
        if not track_quality:
            return True, ""  # No quality info available, allow download
            
        # Quality hierarchy (highest to lowest)
        quality_hierarchy = {
            'lossless': ['flac', 'alac', 'wav'],
            'high': ['320', '320kbps', '320k'],
            'medium': ['192', '192kbps', '192k'],
            'low': ['128', '128kbps', '128k']
        }
        
        # Check if track quality meets requested quality
        requested_qualities = quality_hierarchy.get(requested_quality.lower(), [])
        if not requested_qualities:
            return True, ""  # Unknown quality, allow download
            
        # Check if track quality is acceptable
        track_quality_lower = track_quality.lower()
        quality_acceptable = False
        
        for quality in requested_qualities:
            if quality in track_quality_lower:
                quality_acceptable = True
                break
                
        if not quality_acceptable:
            return False, f"Track quality '{track_quality}' does not meet requested quality '{requested_quality}'"
            
        return True, ""
        
    def should_skip_low_quality_track(self, track_info: TrackInfo, requested_quality: str) -> tuple[bool, str]:
        """Check if track should be skipped due to quality issues"""
        return self.validate_track_quality(track_info, requested_quality)
        
    def log_strict_quality_error(self, track_id: str, track_info: TrackInfo, album_path: str, 
                                requested_quality: str, codec: CodecEnum, bitrate: Optional[int], 
                                bit_depth: Optional[int], sample_rate: Optional[float]):
        """Log strict quality errors to strict_quality_error.txt in the album folder"""
        if not self.log_quality_errors or not self.enabled:
            return
            
        error_msg = f'Not meet quality requirements: {track_info.artists[0] if track_info.artists else "Unknown"} [{track_info.artist_id}]/{track_info.album} [{track_info.album_id}]/{track_info.name} [{track_id}]'
        
        # Create strict_quality_error.txt in the album folder
        if self.album_folder_logging and album_path:
            error_file = os.path.join(album_path, 'strict_quality_error.txt')
        else:
            error_file = 'strict_quality_errors.log'
            
        with open(error_file, 'a', encoding='utf-8') as logf:
            logf.write(f'{error_msg}\n')
        
    def get_quality_info(self) -> dict:
        """Get information about current quality settings"""
        return {
            "enabled": self.enabled,
            "strict_quality_download": self.strict_quality_download,
            "log_quality_errors": self.log_quality_errors,
            "album_folder_logging": self.album_folder_logging
        }
        
    def set_strict_quality(self, strict: bool) -> None:
        """Dynamically change strict quality setting"""
        self.strict_quality_download = strict
        
    def is_strict_quality_enabled(self) -> bool:
        """Check if strict quality download is enabled"""
        return self.enabled and self.strict_quality_download
        
    def get_extension_info(self):
        """Return information about this extension"""
        return {
            "name": "Strict Quality Download",
            "version": "1.0.0",
            "description": "Provides strict quality control and logging for downloads",
            "author": "OrpheusDL Extension System",
            "features": [
                "Strict quality validation",
                "Quality error logging to album folders",
                "Configurable quality requirements",
                "Quality hierarchy support",
                "Dynamic quality control"
            ]
        } 