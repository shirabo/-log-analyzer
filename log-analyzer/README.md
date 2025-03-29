# Log File Analyzer for Suspicious Activity

A lightweight Python script that scans system log files (e.g., Linux `auth.log`) and identifies suspicious login patterns like failed SSH login attempts.

## Features
- Detects failed login attempts and extracts IPs and timestamps.
- Saves suspicious entries to a clean CSV file.
- Works on raw `.log` or `.txt` files from Linux systems.
- Simple command-line interface with flexible options.

## Requirements
- Python 3.6+
- No external packages required

## Usage
```bash
python log_analyzer.py -f sample_logs/auth.log -o suspicious_activity.csv
```

### Arguments:
- `-f` / `--file`: Path to the log file to analyze
- `-o` / `--output`: Output CSV file (optional, default is `suspicious_output.csv`)

## Example Output (CSV)
```
timestamp,ip_address,event
Mar 30 12:12:12,192.168.1.100,Failed Login
Mar 30 12:13:45,10.0.0.23,Failed Login
```

## Project Structure
```
log-analyzer/
├── log_analyzer.py
├── sample_logs/
│   └── auth.log
└── README.md
```

## Optional Enhancements (Ideas for Improvement)
- More detection types (e.g., successful logins, sudo usage, service restarts)
- Support for additional log formats (e.g., Apache, Nginx, Windows Event logs)
- Summary report or simple chart (e.g., top 5 attacking IPs)
- Flag known malicious IPs using threat intelligence APIs

## License
This project is released under the MIT License.
