from use_case.view_result.view_result_interactor import ViewResultInteractor


class ViewResultController:
    """Controller for the view_result use case
    """
    view_result_interactor: ViewResultInteractor

    def __init__(self, file_name: str):
        self.view_result_interactor = ViewResultInteractor(file_name)

    def get_past_data_from_interactor(self):
        return self.view_result_interactor.get_past_data()