import pandas as pd
from flask import Flask, jsonify, request
from difference_calculator import DifferenceCalculator
from graph_adapter import GraphAdapter
from data_formatter import DataFormatter
from model_interactor import ModelInteractor


class UseCaseInteractor:
    app: Flask
    dataset: pd.DataFrame

    def __init__(self, app: Flask, dataset: pd.DataFrame):
        """app should be mutated by CORS() before calling this method."""
        self.app = app
        self.dataset = dataset

    def get_graph_data(self):
        filter_gender = request.get_json()['filtering_factor'][0]
        filter_race = request.get_json()['filtering_factor'][1]
        forecast_steps = request.get_json()['num_points']

        # initialize biased data
        formatted_past_data = (DataFormatter(self.dataset)
                               .filter_by(filter_gender, filter_race)
                               .filter_invalid_transactions())

        frequency_past_data_biased = formatted_past_data.get_frequency_data()
        revenue_past_data_biased = formatted_past_data.get_revenue_data()

        frequency_predicted_data_biased, revenue_predicted_data_biased = (
            ModelInteractor((frequency_past_data_biased,
                             revenue_past_data_biased))
            .execute(forecast_steps))

        # initialize unbiased  data
        formatted_past_data_unbiased = (DataFormatter(self.dataset)
                                        .filter_by(filter_gender, filter_race)
                                        .unbias()
                                        .filter_invalid_transactions())

        frequency_past_data_unbiased = formatted_past_data_unbiased.get_frequency_data()
        revenue_past_data_unbiased = formatted_past_data_unbiased.get_revenue_data()

        frequency_predicted_data_unbiased, revenue_predicted_data_unbiased = (
            ModelInteractor((frequency_past_data_unbiased,
                             revenue_past_data_unbiased))
            .execute(forecast_steps))

        # Calculate difference between biased and unbiased data
        revenue_difference_calculator_past = DifferenceCalculator(
            revenue_past_data_unbiased, revenue_past_data_biased)
        revenue_difference_calculator_predicted = DifferenceCalculator(
            revenue_predicted_data_unbiased, revenue_predicted_data_biased)

        frequency_difference_calculator_past = DifferenceCalculator(
            frequency_past_data_unbiased, frequency_past_data_biased)
        frequency_difference_calculator_predicted = DifferenceCalculator(
            frequency_predicted_data_unbiased, frequency_predicted_data_biased)

        # Collect all the data
        revenue_graph = GraphAdapter(revenue_past_data_biased,
                                     revenue_predicted_data_biased,
                                     revenue_past_data_unbiased,
                                     revenue_predicted_data_unbiased)

        frequency_graph = GraphAdapter(frequency_past_data_biased,
                                       frequency_predicted_data_biased,
                                       frequency_past_data_unbiased,
                                       frequency_predicted_data_unbiased)

        revenue_graph = {
            "past_biased_line": revenue_graph.getPastBiasedLine(),
            "predicted_biased_line": revenue_graph.getPredictedBiasedLine(),
            "past_unbiased_line": revenue_graph.getPastUnbiasedLine(),
            "predicted_unbiased_line": revenue_graph.getPredictedUnbiasedLine(),

            "total_difference":
                revenue_difference_calculator_past.volume_difference() +
                revenue_difference_calculator_predicted.volume_difference(),
            "average_difference":
                revenue_difference_calculator_past.average_difference() +
                revenue_difference_calculator_predicted.average_difference(),
        }

        frequency_graph = {
            "past_biased_line": frequency_graph.getPastBiasedLine(),
            "predicted_biased_line": frequency_graph.getPredictedBiasedLine(),
            "past_unbiased_line": frequency_graph.getPastUnbiasedLine(),
            "predicted_unbiased_line": frequency_graph.getPredictedUnbiasedLine(),

            "total_difference":
                frequency_difference_calculator_past.volume_difference() +
                frequency_difference_calculator_predicted.volume_difference(),
            "average_difference":
                frequency_difference_calculator_past.average_difference() +
                frequency_difference_calculator_predicted.average_difference(),
        }

        result = {
            "revenue_graph": revenue_graph,
            "frequency_graph": frequency_graph
        }
        return jsonify(result)

    def get_past_data(self):
        formatted_past_data = (DataFormatter(self.dataset)
                               .filter_invalid_transactions())

        frequency_past_data_biased = formatted_past_data.get_frequency_data()
        revenue_past_data_biased = formatted_past_data.get_revenue_data()

        # Collect all the data
        revenue_graph = GraphAdapter(revenue_past_data_biased)

        frequency_graph = GraphAdapter(frequency_past_data_biased)

        revenue_graph = {
            "past_biased_line": revenue_graph.getPastBiasedLine()
        }

        frequency_graph = {
            "past_biased_line": frequency_graph.getPastBiasedLine()
        }

        result = {
            "revenue_graph": revenue_graph,
            "frequency_graph": frequency_graph
        }


        return jsonify(result)
