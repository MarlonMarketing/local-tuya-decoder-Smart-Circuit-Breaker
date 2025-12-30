# Local Tuya Decoder for Smart Circuit Breaker

Local Tuya Decoder for Smart Circuit Breaker is a custom component for Home Assistant that decodes sensor data from Local Tuya Smart Circuit Breaker and presents them as separate sensors for voltage, current, and power.

## Features

- Decodes Smart Circuit Breaker sensor data in base64 format
- Creates three separate sensors: voltage, current, and power
- Supports value correction for improved accuracy
- Configuration via Home Assistant user interface
- Localization support (English and Italian)
- Designed specifically for Local Tuya integration

## Prerequisites

**⚠️ Important Requirement**: This component requires the [Local Tuya integration](https://github.com/rospogrigio/localtuya) to be **installed and fully functional** in your Home Assistant instance.

### Before Installing This Component

1. **Install Local Tuya first** - Follow the official [Local Tuya installation guide](https://github.com/rospogrigio/localtuya/wiki/Installation)
2. **Configure your Smart Circuit Breaker** - Make sure your Smart Circuit Breaker is properly configured and working in Local Tuya
3. **Verify base64 data** - Ensure your Local Tuya sensor is providing data in base64 format
4. **Test Local Tuya integration** - Confirm that your Local Tuya devices are responsive and sending data

### What Local Tuya Provides

- Device discovery and communication
- Base64 sensor data from your Smart Circuit Breaker
- Entity creation for raw sensor data

This integration **builds upon** Local Tuya by decoding the base64 data into meaningful voltage, current, and power values.

## Installation

### Method 1: Manual Installation

**⚠️ Prerequisite Check**: Make sure Local Tuya is installed and working before proceeding.

- Download the latest version of the component from the [Releases](https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker/releases) section
- Extract the contents of the archive to the custom_components directory of Home Assistant:
  `/config/custom_components/tuya_decoder_manager/`
- Restart Home Assistant

### Method 2: Installation via HACS

**⚠️ Prerequisite Check**: Make sure Local Tuya is installed and working before proceeding.

- Open HACS in Home Assistant
- Go to "Integrations"
- Click the button with three dots in the top right corner
- Select "Customize repository"
- Add the repository: [https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker](https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker)
- Search for "Local Tuya Decoder for Smart Circuit Breaker" and install the integration
- Restart Home Assistant

## Configuration

**📋 Prerequisites**: Your Local Tuya integration must be fully configured and your Smart Circuit Breaker must be providing data before proceeding.

- Go to "Settings" -> "Devices and Services" in Home Assistant
- Click the "Add Integration" button
- Search for "Local Tuya Decoder for Smart Circuit Breaker" and select it
- Fill in the following fields:
  - **Name**: Name of the integration (e.g., "Smart Circuit Breaker Decoder")
  - **Choose sensor or entity**: Select the Local Tuya sensor entity that provides data in base64 format (this entity should be created by your Local Tuya integration)
  - **Voltage correction value (V)**: Correction value for voltage (default: 0)
  - **Current correction value (A)**: Correction value for current (default: 0)
  - **Power correction (W)**: Correction value for power (default: 0)
- Click "Submit" to complete the configuration

**💡 Tip**: If you don't see your sensor in the dropdown list, go back to your Local Tuya configuration and ensure your Smart Circuit Breaker is properly configured and providing data.

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

### Local Tuya Related Issues

- **🔍 Check Local Tuya Installation**: Make sure Local Tuya integration is properly installed and enabled
- **📡 Verify Device Connection**: Ensure your Smart Circuit Breaker is connected to Local Tuya and responding
- **📊 Check Raw Data**: Verify that the Local Tuya sensor provides data in base64 format
- **🔄 Test Local Tuya Entity**: Confirm that your Local Tuya entity is updating with new data in Developer Tools

### Integration Issues

- **📋 Check Configuration**: Ensure that the integration has been configured correctly
- **🔍 Select Correct Entity**: Make sure you selected the right Local Tuya entity during configuration
- **📝 Check Home Assistant Logs**: Look for any errors in the Home Assistant logs related to this integration
- **🔄 Restart Home Assistant**: Try restarting Home Assistant after configuration changes

### Common Problems

- **No entity available in dropdown**: This usually means Local Tuya is not configured or the device is not providing data
- **Sensors show unavailable**: Check if Local Tuya device is online and connected
- **Incorrect values**: Verify the correction values and ensure your device is the expected Smart Circuit Breaker model
- **Integration not found**: Make sure the custom component files are in the correct directory

### Getting Help

- Check the [Local Tuya documentation](https://github.com/rospogrigio/localtuya/wiki) for device setup
- Open an issue on this repository with your Home Assistant logs
- Verify that your Local Tuya setup works before configuring this decoder

## Contributing

Contributions are welcome! Feel free to open issues or pull requests on the GitHub repository.

## License

This project is distributed under the MIT License. See the [LICENSE](https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker/blob/main/LICENSE) file for details.
