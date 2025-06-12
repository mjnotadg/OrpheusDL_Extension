# Formatting and Filtering Extension

This extension provides enhanced formatting and filtering capabilities for OrpheusDL, including configurable disc/CD subdirectories, source subdirectories, and intelligent filtering of albums and tracks.

## Features

### 🎵 Disc/CD Subdirectories
- **Configurable naming**: Choose between "Disc N" or "CD N" format
- **Smart detection**: Only creates subdirectories for multi-disc albums
- **Flexible formatting**: Customizable format strings with placeholders

### 📁 Source Subdirectories
- **Service-based organization**: Automatically organize downloads by service (Deezer, Spotify, etc.)
- **Clean structure**: Keep different sources separated in your download directory

### 🔍 Intelligent Filtering
- **Collector editions**: Filter out deluxe, expanded, bonus, and special editions
- **Live recordings**: Skip live albums, concerts, and acoustic performances
- **Artist matching**: Strict artist name matching to avoid wrong albums
- **Track filtering**: Skip tracks by different artists within albums

## Configuration

Add the following to your `config/settings.json` in the `extensions` section:

```json
{
    "extensions": {
        "formatting_filters": {
            "enabled": true,
            "source_subdirectories": true,
            "disc_subdirectories": false,
            "disc_format": "Disc {disc_number}",
            "cd_format": "CD {disc_number}",
            "remove_collectors_editions": false,
            "remove_live_recordings": true,
            "strict_artist_match": true,
            "ignore_different_artists": false
        }
    }
}
```

### Settings Explained

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `enabled` | boolean | `true` | Enable/disable the extension |
| `source_subdirectories` | boolean | `true` | Create subdirectories for each service |
| `disc_subdirectories` | boolean | `false` | Create subdirectories for multi-disc albums |
| `disc_format` | string | `"Disc {disc_number}"` | Format for disc 1 subdirectories |
| `cd_format` | string | `"CD {disc_number}"` | Format for additional discs |
| `remove_collectors_editions` | boolean | `false` | Skip collector/deluxe editions |
| `remove_live_recordings` | boolean | `true` | Skip live albums and recordings |
| `strict_artist_match` | boolean | `true` | Only download albums by exact artist match |
| `ignore_different_artists` | boolean | `false` | Skip tracks by different artists |

## Usage Examples

### Basic Setup
```json
{
    "formatting_filters": {
        "enabled": true,
        "source_subdirectories": true,
        "disc_subdirectories": true,
        "disc_format": "Disc {disc_number}",
        "cd_format": "CD {disc_number}"
    }
}
```

### Aggressive Filtering
```json
{
    "formatting_filters": {
        "enabled": true,
        "remove_collectors_editions": true,
        "remove_live_recordings": true,
        "strict_artist_match": true,
        "ignore_different_artists": true
    }
}
```

### Minimal Filtering
```json
{
    "formatting_filters": {
        "enabled": true,
        "source_subdirectories": true,
        "remove_collectors_editions": false,
        "remove_live_recordings": false,
        "strict_artist_match": false
    }
}
```

## Directory Structure Examples

### With Source Subdirectories
```
downloads/
├── deezer/
│   ├── Artist Name [12345]/
│   │   └── Album Name [67890]/
│   │       ├── 01. Track Name.flac
│   │       └── 02. Track Name.flac
└── spotify/
    └── Artist Name [12345]/
        └── Album Name [67890]/
            ├── 01. Track Name.flac
            └── 02. Track Name.flac
```

### With Disc Subdirectories
```
downloads/
└── Artist Name [12345]/
    └── Album Name [67890]/
        ├── Disc 1/
        │   ├── 01. Track Name.flac
        │   └── 02. Track Name.flac
        └── CD 2/
            ├── 01. Track Name.flac
            └── 02. Track Name.flac
```

## Filtering Keywords

### Collector Editions
- collector, deluxe, expanded, bonus, special
- anniversary, remastered, reissue, limited

### Live Recordings
- live, concert, performance, stage, tour
- acoustic, unplugged, mtv, bbc, radio, session

## Benefits

1. **Organized Downloads**: Clean directory structure with service separation
2. **Multi-disc Support**: Proper handling of albums with multiple discs
3. **Quality Control**: Filter out unwanted album types and editions
4. **Artist Accuracy**: Ensure downloads match the intended artist
5. **Flexible Configuration**: Customize behavior to your preferences

## Troubleshooting

### Extension Not Working
- Check that `enabled` is set to `true`
- Verify the extension is properly loaded in the extensions directory
- Check the logs for any error messages

### Unexpected Filtering
- Review the filtering keywords to ensure they match your expectations
- Temporarily disable specific filters to identify which one is causing issues
- Use `strict_artist_match: false` if you want more flexible artist matching

### Directory Structure Issues
- Ensure `source_subdirectories` is enabled for service-based organization
- Enable `disc_subdirectories` only if you want multi-disc albums separated
- Check that the format strings are valid and contain the required placeholders

## Integration

This extension integrates seamlessly with the existing OrpheusDL framework and works alongside other extensions like the Enhanced Logging extension. It provides hooks for:

- Album processing and filtering
- Track processing and filtering
- Directory structure creation
- Path formatting and organization

The extension is designed to be non-intrusive and can be enabled/disabled without affecting other functionality. 