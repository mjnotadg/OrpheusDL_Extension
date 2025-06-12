import os
import re
from typing import Optional, List
from utils.models import TrackInfo, AlbumInfo, ArtistInfo


class OrpheusExtension:
    """Formatting and Filtering Extension for OrpheusDL"""
    
    def __init__(self, settings: dict):
        self.settings = settings
        self.enabled = settings.get("enabled", True)
        self.source_subdirectories = settings.get("source_subdirectories", True)
        self.disc_subdirectories = settings.get("disc_subdirectories", False)
        self.disc_format = settings.get("disc_format", "Disc {disc_number}")
        self.cd_format = settings.get("cd_format", "CD {disc_number}")
        self.remove_collectors_editions = settings.get("remove_collectors_editions", False)
        self.remove_live_recordings = settings.get("remove_live_recordings", True)
        self.strict_artist_match = settings.get("strict_artist_match", True)
        self.ignore_different_artists = settings.get("ignore_different_artists", False)
        
    def apply_source_subdirectories(self, base_path: str, service_name: str) -> str:
        """Apply source subdirectories to the base path"""
        if not self.source_subdirectories or not self.enabled:
            return base_path
            
        return os.path.join(base_path, service_name)
        
    def create_disc_subdirectory(self, album_path: str, disc_number: int, total_discs: int) -> str:
        """Create disc subdirectory path if enabled"""
        if not self.disc_subdirectories or not self.enabled or total_discs <= 1:
            return album_path
            
        # Choose format based on disc number
        if disc_number == 1:
            format_template = self.disc_format
        else:
            format_template = self.cd_format
            
        disc_folder = format_template.format(disc_number=disc_number)
        return os.path.join(album_path, disc_folder)
        
    def should_skip_album(self, album_info: AlbumInfo, artist_name: str = "") -> tuple[bool, str]:
        """Check if album should be skipped based on filtering rules"""
        if not self.enabled:
            return False, ""
            
        album_name = album_info.name.lower()
        
        # Remove collector's editions
        if self.remove_collectors_editions:
            collectors_keywords = ['collector', 'deluxe', 'expanded', 'bonus', 'special', 'anniversary', 'remastered', 'reissue', 'limited']
            if any(keyword in album_name for keyword in collectors_keywords):
                return True, f"Collector edition: {album_info.name}"
        
        # Remove live recordings
        if self.remove_live_recordings:
            live_keywords = ['live', 'concert', 'performance', 'stage', 'tour', 'acoustic', 'unplugged', 'mtv', 'bbc', 'radio', 'session']
            if any(keyword in album_name for keyword in live_keywords):
                return True, f"Live recording: {album_info.name}"
        
        # Strict artist match
        if self.strict_artist_match and artist_name:
            if album_info.artist.strip().lower() != artist_name.strip().lower():
                return True, f"Different artist: {album_info.name} (by {album_info.artist})"
        
        return False, ""
        
    def should_skip_track(self, track_info: TrackInfo, main_artist: str = "") -> tuple[bool, str]:
        """Check if track should be skipped based on filtering rules"""
        if not self.enabled or not main_artist:
            return False, ""
            
        # Ignore different artists within albums
        if self.ignore_different_artists:
            if main_artist.lower() not in [artist.lower() for artist in track_info.artists]:
                return True, f"Track by different artist: {track_info.name} (by {', '.join(track_info.artists)})"
        
        return False, ""
        
    def format_track_filename(self, track_info: TrackInfo, album_path: str) -> str:
        """Format track filename with proper disc subdirectories"""
        if not self.enabled:
            return album_path
            
        # Create disc subdirectory if needed
        if hasattr(track_info, 'disc_number') and hasattr(track_info, 'total_discs'):
            album_path = self.create_disc_subdirectory(
                album_path, 
                track_info.disc_number, 
                track_info.total_discs
            )
            
        return album_path
        
    def get_filtering_info(self) -> dict:
        """Get information about current filtering settings"""
        return {
            "source_subdirectories": self.source_subdirectories,
            "disc_subdirectories": self.disc_subdirectories,
            "disc_format": self.disc_format,
            "cd_format": self.cd_format,
            "remove_collectors_editions": self.remove_collectors_editions,
            "remove_live_recordings": self.remove_live_recordings,
            "strict_artist_match": self.strict_artist_match,
            "ignore_different_artists": self.ignore_different_artists
        }
        
    def get_extension_info(self):
        """Return information about this extension"""
        return {
            "name": "Formatting and Filtering",
            "version": "1.0.0",
            "description": "Provides configurable disc/CD formatting, source subdirectories, and filtering functionality",
            "author": "OrpheusDL Extension System",
            "features": [
                "Configurable disc/CD subdirectories",
                "Source subdirectories support",
                "Album filtering (collector editions, live recordings)",
                "Artist matching filters",
                "Track filtering within albums"
            ]
        } 