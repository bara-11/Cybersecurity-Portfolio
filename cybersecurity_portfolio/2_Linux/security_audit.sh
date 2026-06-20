#!/bin/bash
echo "Security Audit Log - $(date)" > ~/cybersecurity_portfolio/2_Linux/audit_report.txt
echo "--- Listening Ports ---" >> ~/cybersecurity_portfolio/2_Linux/audit_report.txt
ss -tulpn >> ~/cybersecurity_portfolio/2_Linux/audit_report.txt
echo "--- Top CPU Processes ---" >> ~/cybersecurity_portfolio/2_Linux/audit_report.txt
ps aux --sort=-%cpu | head -5 >> ~/cybersecurity_portfolio/2_Linux/audit_report.txt
