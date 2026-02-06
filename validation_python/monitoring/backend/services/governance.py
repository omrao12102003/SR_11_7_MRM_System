import csv
from datetime import datetime
import os

BASE_DIR = "/mnt/c/Users/omira/OneDrive/Desktop/SR11_7_MRM_System"
AUDIT_FILE = f"{BASE_DIR}/governance/audit_log.csv"
MODEL_FILE = f"{BASE_DIR}/governance/model_inventory.csv"
APPROVALS_FILE = f"{BASE_DIR}/governance/approvals.csv"

def log_action(user, action, entity, details):
    with open(AUDIT_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), user, action, entity, details])

def load_models():
    try:
        with open(MODEL_FILE, newline="") as f:
            return list(csv.DictReader(f))
    except:
        return []

def load_approvals():
    try:
        with open(APPROVALS_FILE, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)
            rows = []
            for row in reader:
                row_dict = dict(zip(headers, row))
                rows.append(row_dict)
            return rows
    except:
        return []

print("Approvals:", load_approvals())
