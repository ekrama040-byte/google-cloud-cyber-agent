@echo off
echo [!] Executing Automated Defense Rule...
netsh advfirewall firewall add rule name="Block Attacker IP" dir=in action=block remoteip=203.0.113.5
echo [+] Malicious IP blocked successfully.
pause
