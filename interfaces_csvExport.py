import re
import csv

# Define a regex pattern that captures interface details. It considers multi-line information for each interface.
interface_regex = re.compile(
    r"Interface (\S+)(?: \"(\S+)?\"), is (\S+).*?\n"
    r"(.*\n)*?"
    r"(?:\s+IP address (\d+\.\d+\.\d+\.\d+), subnet mask (\d+\.\d+\.\d+\.\d+))?"
    r"(.*\n)*?"
    r"(?:\s+VLAN identifier (\d+))?"
    r"(.*\n)*?"
    r"(?:\s+Description: ([^\n]+))?", re.MULTILINE | re.DOTALL)

# Open the text file containing the interface data
with open('interfaces_info.txt', 'r') as file:
    data = file.read()

# Open the CSV file for writing the results
with open('interfaces.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Define the column headers for the CSV
    fieldnames = [
        'Interface', 'Status', 'Name', 'IP Address', 'Subnet Mask', 'VLAN', 'Type', 'Description'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Process each match from the regex search
    for match in interface_regex.finditer(data):
        # Extract relevant data from the regex match object
        interface = match.group(1)
        name = match.group(2) or ''
        status = 'up' if match.group(3) == 'up' else 'down'
        ip = match.group(5) or ''
        mask = match.group(6) or ''
        vlan = match.group(8) or ''
        description = match.group(10) or ''

        # Write the interface info to the CSV file
        writer.writerow({
            'Interface': interface,
            'Status': status,
            'Name': name,
            'IP Address': ip,
            'Subnet Mask': mask,
            'VLAN': vlan,
            'Type': '',  # Type information is not explicitly available in the provided text sample
            'Description': description
        })

print("CSV file 'interfaces.csv' has been created.")
