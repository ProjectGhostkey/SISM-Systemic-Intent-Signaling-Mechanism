from datetime import datetime

class SISMViolation(Exception):
    pass

class SISM:
    def __init__(self):
        self.log = []

    def intercept(self, intent):
        required_fields = ["action", "scope", "reversibility", "description"]

        for field in required_fields:
            if field not in intent:
                raise SISMViolation(f"Missing intent field: {field}")

        self.log_intent(intent)
        return True

    def log_intent(self, intent):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "intent": intent
        }
        self.log.append(entry)
        print("SISM LOGGED:", entry)

def dangerous_action():
    print("⚠️ ACTION EXECUTED")

sism = SISM()

intent = {
    "action": "run_dangerous_action",
    "scope": "local_test",
    "reversibility": "reversible",
    "description": "Testing SISM interception before execution"
}

try:
    if sism.intercept(intent):
        dangerous_action()
except SISMViolation as e:
    print("SISM BLOCKED ACTION:", e)
