import os
from pytest_html import extras
import tempfile
#set a fake key before pytest import anything from the app
os.environ["OPENAI_API_KEY"] = "fake-key-for-testing"



def pytest_html_report_title(report):
    report.title = "Piggyback Learning Test Report"

def pytest_configure(config):
    config._metadata = {}
    
#must happen before any app imports read settings
temp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
os.environ["SQLITE_PATH"] = temp.name

def pytest_sessionfinish(session,exitstatus):
    path = os.environ.get("SQLITE_PATH")
    if path and "tmp" in path:
        os.unlink(path)