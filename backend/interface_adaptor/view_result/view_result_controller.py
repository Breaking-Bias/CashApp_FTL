import pandas as pd
import os
from data_reader import DataReader
from data_access.data_access_object import DataAccessObject


class ViewResultController:
    """Controller for the view_result use case
    """
    view_result_use_case = ViewResultUseCase


        
    def execute(self):
        """executes the view_result use case
        """
        view_result_use_case