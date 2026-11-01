import argparse
from cybernova.config import load_scope
from cybernova.scanner import scan_host
from cybernova.report import write_report, print_summary

def main():
    parser = argparse.ArgumentParser(description="Cybernova authorised attack-surface monitor")
    parser.add_argument("--scope", default="scope.json")
    args = parser.parse_args()
    scope = load_scope(args.scope)
    targets = scope.get("authorized_domains", []) + scope.get("authorized_hosts", [])
    results = [scan_host(host, scope) for host in targets]
    print_summary(results)
    print("Report saved:", write_report(results))

if __name__ == "__main__":
    main()
