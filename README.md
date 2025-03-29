# Log File Analyzer for Suspicious Activity

This project is a lightweight Python tool that analyzes system log files — such as `auth.log` on Linux — to detect suspicious login behavior. It scans for failed SSH login attempts and outputs the results to a CSV file for further review.

---

## Features

- Detects failed SSH login attempts using regex
- Extracts IP addresses and timestamps of suspicious events
- Exports findings to a structured `.csv` file
- Works on `.log` and `.txt` formats
- Simple and user-friendly CLI interface

---

## Requirements

- Python 3.6 or higher
- No external libraries required

---

## Usage

```bash
python log_analyzer.py -f sample_logs/auth.log -o suspicious_output.csv


Arguments:
-f, --file: Path to the log file you want to scan (required)

-o, --output: Name of the output CSV file (optional, default: suspicious_output.csv)

Example Output
timestamp,ip_address,event
Mar 30 12:12:12,192.168.1.100,Failed Login
Mar 30 12:13:45,10.0.0.23,Failed Login

Folder Structure
log-analyzer/
├── log_analyzer.py
├── README.md
└── sample_logs/
    └── auth.log

Sample Log Format
The tool currently supports lines like the following, typical of Linux SSH login attempts:
Mar 30 12:12:12 server sshd[1234]: Failed password for invalid user root from 192.168.1.100 port 22 ssh2



