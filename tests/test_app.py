import pytest
from src.query_base import Employee, Team
from src.mixins import LoggerMixin, log_calls
from src.dashboard import EmployeeDashboard

def test_employee_query():
    emp = Employee("John", 1)
    assert emp.query() == "Employee: John, ID: 1"

def test_team_query():
    emp1 = Employee("A", 2)
    emp2 = Employee("B", 3)
    team = Team("Alpha", [emp1, emp2])
    assert "Alpha" in team.query()

def test_logger_mixin(capsys):
    class Test(LoggerMixin): pass
    t = Test()
    t.log("Hello")
    out = capsys.readouterr().out
    assert "[LOG] Hello" in out

def test_log_calls_decorator(capsys):
    @log_calls
    def foo(): return 42
    foo()
    out = capsys.readouterr().out
    assert "Calling foo" in out

def test_dashboard_base():
    dash = EmployeeDashboard()
    assert dash.render() == "Employee Dashboard"
