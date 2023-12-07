# ciscoIOS_toCSV
command "show interface summary" to a csv spreadsheet.

## Current Functionality

The script processes an input text file (`interfaces_info.txt`) and extracts the following information for each interface:

- Interface Name
- Status (up/down/administratively down)
- Alias (if available)
- IP Address (if available)
- Subnet Mask (if available)
- VLAN (if available)
- Description (if available)

This information is then written to a CSV file (`interfaces_parsed.csv`) with corresponding headers.

## Known Issues

- **IP Address Extraction**: The script is currently having issues with consistently pulling out the IP address from the provided interface information. The regex pattern may need to be adjusted depending on the specific format of the IP address lines in the input file.

## Usage

To use the script, place your output file (default name expected is `interfaces_info.txt`) in the same directory as the script and run the script with Python.
