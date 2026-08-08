from app.export_intelligence.export_decision import export_decider
class ExportReport:
    def generate(self,data): return {'report':'NEXRA Export Report','decision':export_decider.evaluate(data)}
report_engine=ExportReport()
