from use_case.view_result.view_result_interactor import ViewResultInteractor
from flask import jsonify


class ViewResultController:
    """Controller for the view result use case"""
    view_result_interactor: ViewResultInteractor

    def __init__(self):
        self.view_result_interactor = ViewResultInteractor()

    def execute(self, file_name: str):
        """Executes the view result use case via view_result_interactor"""
        self.view_result_interactor = ViewResultInteractor(file_name=file_name)
        result = self.view_result_interactor.make_graph_only_past()
        return jsonify(result)
