from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ReportBuilderConfig(AppConfig):
    name = 'report_builder'
    verbose_name = _('Reports')