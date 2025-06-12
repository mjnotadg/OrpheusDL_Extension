# Strict Quality Download Extension

This extension provides strict quality control and logging for OrpheusDL downloads, ensuring that only tracks meeting the specified quality requirements are downloaded and logging quality issues to album folders.

## Features

### 🎵 Quality Validation
- **Strict quality checking**: Validates track quality against requested quality
- **Quality hierarchy**: Supports lossless, high, medium, and low quality levels
- **Flexible configuration**: Enable/disable strict quality control
- **Dynamic control**: Change settings during runtime

### 📝 Quality Error Logging
- **Album folder logging**: Logs quality errors to `strict_quality_error.txt` in album folders
- **Clear error messages**: Provides descriptive error messages for quality mismatches
- **Configurable logging**: Enable/disable quality error logging independently
- **Centralized logging**: Fallback to global log file when album folder not available

### 🔍 Quality Levels
- **Lossless**: FLAC, ALAC, WAV formats
- **High**: 320kbps MP3 and equivalent
- **Medium**: 192kbps MP3 and equivalent  
- **Low**: 128kbps MP3 and equivalent

## Configuration

Add the following to your `config/settings.json` in the `extensions` section:

```json
{
    "extensions": {
        "quality": {
            "strict_quality": {
                "enabled": true,
                "strict_quality_download": true,
                "log_quality_errors": true,
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
| `strict_quality_download` | boolean | `true` | Enable strict quality validation |
| `log_quality_errors` | boolean | `true` | Enable quality error logging |
| `album_folder_logging` | boolean | `true` | Log errors to album folders |
| `clear_error_messages` | boolean | `true` | Use clear error messages |

## Usage Examples

### Basic Setup with Logging
```json
{
    "strict_quality": {
        "enabled": true,
        "strict_quality_download": true,
        "log_quality_errors": true,
        "album_folder_logging": true
    }
}
```

### Strict Quality Only (No Logging)
```json
{
    "strict_quality": {
        "enabled": true,
        "strict_quality_download": true,
        "log_quality_errors": false
    }
}
```

### Logging Only (No Quality Filtering)
```json
{
    "strict_quality": {
        "enabled": true,
        "strict_quality_download": false,
        "log_quality_errors": true,
        "album_folder_logging": true
    }
}
```

## Quality Validation Process

### How It Works

1. **Track Quality Check**: Extension examines track quality information
2. **Quality Comparison**: Compares track quality with requested quality level
3. **Decision Making**: Allows or blocks download based on quality match
4. **Error Logging**: Logs quality issues to album folder if enabled
5. **Feedback**: Provides clear reason for quality rejection

### Quality Hierarchy

```
Lossless Quality:
├── FLAC (Free Lossless Audio Codec)
├── ALAC (Apple Lossless Audio Codec)
└── WAV (Waveform Audio File Format)

High Quality:
├── 320kbps MP3
├── 320k MP3
└── 320kbps

Medium Quality:
├── 192kbps MP3
├── 192k MP3
└── 192kbps

Low Quality:
├── 128kbps MP3
├── 128k MP3
└── 128kbps
```

## Logging System

### Log File Locations

- **Album folder**: `{album_path}/strict_quality_error.txt`
- **Global fallback**: `strict_quality_errors.log` (when album folder not available)

### Log Message Format

```
Not meet quality requirements: Artist Name [12345]/Album Name [67890]/Track Name [track_id]
```

### Logging Examples

```
# Example log entry in strict_quality_error.txt:
Not meet quality requirements: Pink Floyd [12345]/Dark Side of the Moon [67890]/Time [track_123]
```

## Integration with Core

### Extension Methods

1. **`validate_track_quality()`** - Main quality validation method
2. **`should_skip_low_quality_track()`** - Check if track should be skipped
3. **`log_strict_quality_error()`** - Log quality errors to album folder
4. **`is_strict_quality_enabled()`** - Check if strict quality is active
5. **`set_strict_quality()`** - Dynamically change settings

### Core Integration Points

The extension integrates with OrpheusDL's download process:

1. **Before track download**: Quality validation occurs
2. **Quality mismatch**: Track is skipped and error is logged
3. **Quality match**: Track proceeds to download
4. **No quality info**: Track is allowed (graceful degradation)

## Benefits

1. **Quality Assurance**: Ensures consistent download quality
2. **Bandwidth Efficiency**: Avoids downloading low-quality tracks
3. **Storage Optimization**: Prevents storing unwanted quality levels
4. **Error Tracking**: Logs quality issues for review and analysis
5. **Flexible Control**: Easy to enable/disable as needed
6. **Clear Feedback**: Detailed quality rejection reasons

## Examples

### Strict Lossless Download with Logging
```python
# Request: lossless quality
# Track quality: 320kbps MP3
# Result: SKIPPED and LOGGED
# Log: "Not meet quality requirements: Artist/Album/Track [track_id]"
```

### High Quality Download
```python
# Request: high quality  
# Track quality: 320kbps MP3
# Result: ALLOWED - Quality matches requirements
```

### Unknown Quality
```python
# Request: lossless quality
# Track quality: None (no quality info)
# Result: ALLOWED - No quality info available, allow download
```

## Troubleshooting

### Extension Not Working
- Check that `enabled` is set to `true`
- Verify the extension is properly loaded
- Check logs for any error messages

### Unexpected Quality Rejections
- Review the quality hierarchy to understand requirements
- Check if track quality information is available
- Temporarily disable strict quality to identify issues

### Logging Issues
- Ensure `log_quality_errors` is enabled
- Check that `album_folder_logging` is enabled for album-specific logs
- Verify write permissions for the album folder

### Quality Information Missing
- Some tracks may not have quality information
- Extension allows downloads when quality info is unavailable
- This provides graceful degradation

## Advanced Usage

### Dynamic Quality Control
```python
# Change strict quality setting during runtime
extension.set_strict_quality(False)  # Disable strict quality
extension.set_strict_quality(True)   # Enable strict quality
```

### Quality Information
```python
# Get current quality settings
info = extension.get_quality_info()
print(f"Enabled: {info['enabled']}")
print(f"Strict Quality: {info['strict_quality_download']}")
print(f"Log Quality Errors: {info['log_quality_errors']}")
```

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

- **Enhanced Logging Extension**: Handles unavailable track logging
- **Formatting Filters Extension**: Quality filtering happens before other filters
- **Core OrpheusDL**: Integrates with existing quality settings

## Best Practices

1. **Enable for Quality Control**: Use when you want consistent quality
2. **Enable Logging for Analysis**: Log quality issues to identify patterns
3. **Monitor Logs**: Check quality rejection reasons for insights
4. **Test Settings**: Verify behavior with different quality levels
5. **Combine with Other Extensions**: Use with enhanced logging for comprehensive tracking

## Error Handling

The extension provides robust error handling:

- **Missing Quality Info**: Gracefully allows downloads
- **Unknown Quality Levels**: Defaults to allowing downloads
- **Invalid Settings**: Uses sensible defaults
- **Extension Errors**: Fails safely without breaking downloads
- **Logging Errors**: Continues operation even if logging fails

This ensures the extension is reliable and doesn't interfere with normal operation when issues occur. 