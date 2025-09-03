from report.utils import sample_util
from report.src import *
from src.query_base import Employee, Team
from src.mixins import LoggerMixin, log_calls

class DashboardBase:
    def render(self):
        raise NotImplementedError

class EmployeeDashboard(DashboardBase):
    def render(self):
        return "Employee Dashboard"

class TeamDashboard(DashboardBase):
    def render(self):
        return "Team Dashboard"
