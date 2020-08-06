import json
import os
def load_json_from_file(filename):
    with open(filename, "r") as f:
        content = f.read()
        return json.loads(content)

def get_os_info():
    with open("/etc/issue", "r") as f:
        content = f.read()
        return content.split("\n")[0]