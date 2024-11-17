import pandas as pd
from graphing_data import GraphingData

class GraphAdapter:
    def __init__(self, revenue_past_biased_data: GraphingData, revenue_predicted_biased_data: GraphingData, revenue_past_unbiased_data: GraphingData ,revenue_predicted_unbiased_data: GraphingData):
        self.revenue_past_biased_data = revenue_past_biased_data
        self.revenue_past_unbiased_data = revenue_past_unbiased_data
        self.revenue_predicted_biased_data = revenue_predicted_biased_data
        self.revenue_predicted_unbiased_data = revenue_predicted_unbiased_data
    
    
    

        
    



