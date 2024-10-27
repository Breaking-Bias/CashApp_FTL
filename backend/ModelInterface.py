import pandas as pd
from DataConnectInterface import dataset_combined

class ModelInterface:
    '''
    This interface aims to streamline the process of generating predictions from given dataset.
    Note that this interface only serves as a data panel, and the model running logic is refactored to other modules.
    '''
    original: pd | None

    def __init__(self):
        '''self.original initialized as None.'''
        self.original = None
    
    def upload_dataset(self, dataset_combined: pd) -> bool:
        '''
        Return true if the dataset is successfully uploaded.
        Note that the design idea for now is that the dataset would NOT be updated once submitted.
        '''
        if self.original is None:
            try:
                self.original = dataset_combined
                return True
            except:
                return False
        else:
            return True
    
    # All methods below have a common precondition: self.original is not None
    
    def get_model_weights(self) -> pd:
        ...
        return ...
    
    def get_predictions(self) -> pd:
        '''Return a Pd that contains both original data and predictions. The resulting dataset should be ready for graphing.'''
        ...
        # Note that this method should not contain too much computational logic. Those should be refactored out.
        return ...

if __name__ != '__main__':
    model_interface = ModelInterface()
    if not model_interface.upload_dataset(dataset_combined):
        ...
    else:
        prediction = model_interface.get_predictions()

# prediction is to be exported to DataFull.