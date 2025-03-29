# log_analyzer.py
import argparse
import re
import csv
from datetime import datetime

def parse_log_line(line):
    match = re.search(r'(?P<datetime>\w{3} \d{1,2} \d{2}:\d{2}:\d{2}).*Failed password.*from (?P<ip>[\d\.]+)', line)
    if match:
        return {
            'timestamp': match.group('datetime'),
            'ip_address': match.group('ip'),
            'event': 'Failed Login'
        }
    return None

def analyze_log(file_path):
    suspicious_entries = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            result = parse_log_line(line)
            if result:
                suspicious_entries.append(result)
    return suspicious_entries

def write_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'ip_address', 'event']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(description="Simple Log File Analyzer for Suspicious Activity")
    parser.add_argument('-f', '--file', required=True, help='Path to the log file')
    parser.add_argument('-o', '--output', default='suspicious_output.csv', help='Output CSV file')
    args = parser.parse_args()

    print(f"Analyzing {args.file}...")
    suspicious = analyze_log(args.file)

    if suspicious:
        print(f"Found {len(suspicious)} suspicious entries. Saving to {args.output}...")
        write_to_csv(suspicious, args.output)
    else:
        print("No suspicious entries found.")

if __name__ == '__main__':
    main()
