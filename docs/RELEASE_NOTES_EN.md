# Tuya Decoder Manager - Release Notes

## Version 1.0.2

### New Features
- Added the ability to correct voltage, current, and power values through configurable parameters
- Implemented decoding of data in base64 format
- Created three separate sensors for voltage, current, and power
- Added support for localization (English and Italian)
- Configuration through Home Assistant's user interface

### Bug Fixes
- Fixed the issue with negative power calculation
- Corrected the algorithm for extracting current from base64 data
- Fix to ensure sensor values are not negative

### Improvements
- Added complete documentation in Italian and English
- Improved error handling
- Optimized code for better efficiency
- Added the ability to modify correction values without restarting Home Assistant

## Version 1.0.1

### Bug Fixes
- Fixed an issue with base64 data decoding
- Corrected sensor definitions in the manifest.json file

### Improvements
- Added initial documentation

## Version 1.0.0

### Initial Features
- Implemented decoding of Tuya sensor data
- Created sensors for voltage, current, and power
- Initial configuration through configuration file
