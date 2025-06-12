# Enhanced Logging Extension

This extension provides enhanced logging functionality for OrpheusDL, specifically focused on tracking unavailable tracks and providing clear error messages in album folders.

## Features

### 📝 Unavailable Track Logging
- **Separate log files**: Creates dedicated `error.txt` files for unavailable tracks
- **Album-specific logging**: Logs errors directly in album folders for easy access
- **Clear error messages**: Provides descriptive error messages for unavailable tracks
- **Configurable settings**: Enable/disable logging features independently

### 🔍 Error Tracking
- **Track identification**: Logs full track information including artist, album, and track IDs
- **Structured format**: Consistent error message format for easy parsing
- **Fallback logging**: Global log file when album folder is not available

## Configuration

Add the following to your `config/settings.json` in the `extensions` section:

```json
{
    "extensions": {
        "logging": {
            "enhanced_logging": {
                "enabled": true,
                "log_unavailable_tracks": true,
                "album_folder_logging": true,
                "clear_error_messages": true
            }
        }
    }
}
```

### Settings Explained

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `true` | Enable/disable the extension |
| `log_unavailable_tracks` | boolean | `true` | Enable unavailable track logging |
| `album_folder_logging` | boolean | `true` | Log errors to album folders |
| `clear_error_messages` | boolean | `true` | Use clear error messages |

## Usage Examples

### Basic Setup
```json
{
    "enhanced_logging": {
        "enabled": true,
        "log_unavailable_tracks": true,
        "album_folder_logging": true,
        "clear_error_messages": true
    }
}
```

### Disable Album Folder Logging
```json
{
    "enhanced_logging": {
        "enabled": true,
        "log_unavailable_tracks": true,
        "album_folder_logging": false,
        "clear_error_messages": true
    }
}
```

### Disable Extension
```json
{
    "enhanced_logging": {
        "enabled": false,
        "log_unavailable_tracks": true,
        "album_folder_logging": true,
        "clear_error_messages": true
    }
}
```

## Logging System

### Log File Locations

- **Album folder**: `{album_path}/error.txt`
- **Global fallback**: `unavailable_tracks.log` (when album folder not available)

### Log Message Format

```
Unavailable: Artist Name [12345]/Album Name [67890]/Track Name [track_id]
```

### Logging Examples

```
# Example log entry in error.txt:
Unavailable: Pink Floyd [12345]/Dark Side of the Moon [67890]/Time [track_123]
```

## Integration with Core

### Extension Methods

1. **`log_unavailable_track()`** - Log unavailable tracks to album folder
2. **`get_extension_info()`** - Get extension information

### Core Integration Points

The extension integrates with OrpheusDL's download process:

1. **Track availability check**: When a track is unavailable
2. **Error logging**: Logs the unavailable track with full details
3. **Album folder creation**: Creates log file in the album directory
4. **Fallback handling**: Uses global log if album folder unavailable

## Benefits

1. **Error Tracking**: Keep track of unavailable tracks for review
2. **Album Organization**: Logs are stored with the relevant album
3. **Clear Information**: Detailed error messages with track identification
4. **Easy Access**: Log files are easily accessible in album folders
5. **Configurable**: Enable/disable features as needed

## Examples

### Unavailable Track Logging
```python
# Track: "Time" by Pink Floyd from "Dark Side of the Moon"
# Status: Unavailable
# Result: LOGGED
# Log: "Unavailable: Pink Floyd [12345]/Dark Side of the Moon [67890]/Time [track_123]"
```

### Album Folder Structure
```
downloads/
└── Pink Floyd [12345]/
    └── Dark Side of the Moon [67890]/
        ├── 01. Speak to Me.flac
        ├── 02. Breathe.flac
        ├── error.txt  # Contains unavailable track logs
        └── ...
```

## Troubleshooting

### Extension Not Working
- Check that `enabled` is set to `true`
- Verify the extension is properly loaded
- Check logs for any error messages

### Logging Issues
- Ensure `log_unavailable_tracks` is enabled
- Check that `album_folder_logging` is enabled for album-specific logs
- Verify write permissions for the album folder

### Missing Log Files
- Check if album folder exists and is writable
- Verify that tracks are actually being marked as unavailable
- Check global log file for fallback logging

## Advanced Usage

### Extension Information
```python
# Get extension details
info = extension.get_extension_info()
print(f"Name: {info['name']}")
print(f"Version: {info['version']}")
print(f"Description: {info['description']}")
```

## Integration with Other Extensions

This extension works seamlessly with:

- **Strict Quality Extension**: Handles quality error logging
- **Formatting Filters Extension**: Works alongside filtering functionality
- **Core OrpheusDL**: Integrates with existing download process

## Best Practices

1. **Enable for Error Tracking**: Use when you want to track unavailable tracks
2. **Monitor Logs**: Check error logs to identify availability patterns
3. **Album Organization**: Keep logs with relevant albums for easy access
4. **Combine with Other Extensions**: Use with strict quality extension for comprehensive tracking

## Error Handling

The extension provides robust error handling:

- **Missing Album Folder**: Falls back to global logging
- **Write Permission Issues**: Continues operation without logging
- **Invalid Settings**: Uses sensible defaults
- **Extension Errors**: Fails safely without breaking downloads

This ensures the extension is reliable and doesn't interfere with normal operation when issues occur.

## Note on Quality Logging

**Quality error logging has been moved to the Strict Quality Download Extension** for better organization and separation of concerns. This extension now focuses exclusively on unavailable track logging, while quality-related logging is handled by the dedicated quality extension. 