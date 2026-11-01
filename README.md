# Cybernova ASM – PS-011

A scope-bound prototype for authorised attack-surface inventory and change monitoring.

## Features
- Exact allowlist scope guard (maximum 20 domains and 10 hosts).
- DNS A/AAAA plus optional CNAME/MX/TXT inventory.
- TCP connection checks against the configured port list.
- TLS certificate expiry inspection on port 443.
- SQLite historical snapshots and basic change comparison.
- JSON report and local HTML report viewer.

## Safety boundaries
Use only domains/hosts you own or have written permission to assess. The scanner refuses targets outside `scope.json`. It performs non-exploitative DNS lookups, TLS handshakes and TCP connection attempts; it does not exploit vulnerabilities, brute-force credentials, crawl websites, or scan arbitrary IP ranges. Review the scope and port list before every run.

## Setup (Windows / VS Code)
1. Install Python 3.10+.
2. Extract the ZIP and open the `Cybernova_ASM` folder in VS Code.
3. Open Terminal and run: `py -m venv .venv`
4. Activate: PowerShell `.\.venv\Scripts\Activate.ps1`
5. Install: `pip install -r requirements.txt`
6. Edit `scope.json`. Replace `example.com` with an authorised domain.
7. Run: `python main.py`

## View report
Open `dashboard.html` in a browser and select `outputs/latest_report.json`.

## Project structure
- `main.py`: command-line entry point
- `scope.json`: authorised targets and port policy
- `cybernova/config.py`: configuration loader and limits
- `cybernova/scope_guard.py`: allowlist enforcement
- `cybernova/dns_check.py`: DNS inventory
- `cybernova/tls_check.py`: TLS certificate inspection
- `cybernova/port_check.py`: configured TCP port checks
- `cybernova/database.py`: SQLite snapshot storage
- `cybernova/change_detect.py`: baseline comparison
- `cybernova/scanner.py`: scan orchestration
- `cybernova/report.py`: report output
- `dashboard.html`: local JSON report viewer

## Limitations
This is a starter implementation, not a production-grade ASM platform. It currently checks only configured hosts, uses a simple previous-snapshot comparison, and checks TLS on port 443. DNS resolver consensus, SAN-chain validation, asynchronous scanning, richer cloud-provider dangling-record verification, authentication, and a live SOC dashboard are not implemented in this prototype. A failed DNS or TCP check is not proof that an asset is vulnerable.

## Troubleshooting
- `ModuleNotFoundError: dns`: run `pip install -r requirements.txt`.
- Empty results: check DNS resolution, firewall rules and whether the service is reachable.
- `Blocked by ScopeGuard`: add the exact authorised domain/host to `scope.json`.
- Do not add wildcard domains, IP ranges or third-party targets without explicit authorisation.
