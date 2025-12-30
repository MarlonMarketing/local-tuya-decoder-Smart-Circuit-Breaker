# Local Tuya Decoder for Smart Circuit Breaker

Local Tuya Decoder for Smart Circuit Breaker is a custom component for Home Assistant that decodes sensor data from Local Tuya Smart Circuit Breaker and presents them as separate sensors for voltage, current, and power.

## Features

- Decodes Smart Circuit Breaker sensor data in base64 format
- Creates three separate sensors: voltage, current, and power
- Supports value correction for improved accuracy
- Configuration via Home Assistant user interface
- Localization support (English and Italian)
- Designed specifically for Local Tuya integration

## Installation

### Method 1: Manual Installation

- Download the latest version of the component from the [Releases](https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker/releases) section
- Extract the contents of the archive to the custom_components directory of Home Assistant:
  `/config/custom_components/tuya_decoder_manager/`
- Restart Home Assistant

### Method 2: Installation via HACS

- Open HACS in Home Assistant
- Go to "Integrations"
- Click the button with three dots in the top right corner
- Select "Customize repository"
- Add the repository: [https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker](https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker)
- Search for "Local Tuya Decoder for Smart Circuit Breaker" and install the integration
- Restart Home Assistant

## Configuration

- Go to "Settings" -> "Devices and Services" in Home Assistant
- Click the "Add Integration" button
- Search for "Local Tuya Decoder for Smart Circuit Breaker" and select it
- Fill in the following fields:
  - **Name**: Name of the integration (e.g., "Smart Circuit Breaker Decoder")
  - **Choose sensor or entity**: Select the Local Tuya sensor that provides data in base64 format
  - **Voltage correction value (V)**: Correction value for voltage (default: 0)
  - **Current correction value (A)**: Correction value for current (default: 0)
  - **Power correction (W)**: Correction value for power (default: 0)
- Click "Submit" to complete the configuration

## Usage

After configuration, the integration will automatically create three sensors:

- **Voltage**: Displays voltage in Volts (V)
- **Current**: Displays current in Amperes (A)
- **Power**: Displays power in Kilowatts (kW)

Values are calculated using the following algorithms:

### Voltage

- Decodes base64 data into bytes
- Extracts the first 2 bytes (big-endian)
- Divides by 10 to obtain the value in Volts
- Applies the configured correction

### Current

- Decodes base64 data into bytes
- Extracts the fifth byte (index 4)
- Multiplies by 0.00593 to obtain the value in Amperes
- Applies the configured correction
- Ensures the value is not negative

### Power

- Calculates voltage and current as described above
- Multiplies voltage by current to obtain power in Watts
- Applies the configured correction
- Ensures the value is not negative
- Converts to Kilowatts with 2 decimal places

## Advanced Configuration

You can modify correction values at any time:

- Go to "Settings" -> "Devices and Services"
- Find the "Local Tuya Decoder for Smart Circuit Breaker" integration
- Click the three dots in the top right corner
- Select "Options"
- Modify the correction values as needed
- Click "Submit" to save the changes

## Troubleshooting

If sensors are not created or do not display data:

- Verify that the Local Tuya sensor provides data in base64 format
- Check Home Assistant logs for any errors
- Ensure that the integration has been configured correctly
- Try restarting Home Assistant

## Contributing

Contributions are welcome! Feel free to open issues or pull requests on the GitHub repository.

## License

This project is distributed under the MIT License. See the [LICENSE](https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker/blob/main/LICENSE) file for details.
