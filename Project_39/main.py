import re
from collections import Counter
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+'
    r'(?P<level>INFO|ERROR|WARNING|DEBUG)\s+'
    r'(?P<message>.+?)\s+'
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
)

class LogAnalyzer:
    def __init__(self, logfile):
        self.logfile = logfile
        self.levels = Counter()
        self.ips = Counter()
        self.errors = []
        self.malformed = 0

    def parse_log(self):
        with open(self.logfile, "r", encoding="utf-8", errors="ignore") as file:
            for line_no, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                match = LOG_PATTERN.match(line)
                if not match:
                    self.malformed += 1
                    continue

                data = match.groupdict()
                level = data["level"]
                ip = data["ip"]
                timestamp = datetime.strptime(
                    data["timestamp"], "%Y-%m-%d %H:%M:%S"
                )

                self.levels[level] += 1
                self.ips[ip] += 1

                if level == "ERROR":
                    self.errors.append({
                        "time": timestamp,
                        "ip": ip,
                        "message": data["message"]
                    })

    def report(self):
        print("\n====== LOG ANALYSIS REPORT ======\n")

        print("Log Level Summary:")
        for level, count in self.levels.items():
            print(f"  {level}: {count}")

        print("\nTop IP Addresses:")
        for ip, count in self.ips.most_common(5):
            print(f"  {ip}: {count}")

        print(f"\nTotal ERRORs: {len(self.errors)}")
        print(f"Malformed log lines: {self.malformed}")

    def save_report(self, filename="report.txt"):
        with open(filename, "w") as f:
            f.write("LOG ANALYSIS REPORT\n\n")

            f.write("Log Levels:\n")
            for level, count in self.levels.items():
                f.write(f"{level}: {count}\n")

            f.write("\nTop IPs:\n")
            for ip, count in self.ips.most_common():
                f.write(f"{ip}: {count}\n")

            f.write("\nErrors:\n")
            for err in self.errors:
                f.write(
                    f"{err['time']} | {err['ip']} | {err['message']}\n"
                )

            f.write(f"\nMalformed lines: {self.malformed}\n")


if __name__ == "__main__":
    analyzer = LogAnalyzer("system.log")
    analyzer.parse_log()
    analyzer.report()
    analyzer.save_report()
