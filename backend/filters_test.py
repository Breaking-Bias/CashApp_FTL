# import pytest
# import pandas as pd
# from filters import GenderFilter, RaceFilter, FilterManager
#
# # Sample DataFrame to test the filters
# data = pd.DataFrame({
#     'Age': [15, 22, 45, 70, 25],
#     'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
#     'Race': ['White', 'Black', 'Asian', 'Hispanic', 'Mixed'],
#     'State': ['CA', 'NY', 'TX', 'FL', 'CA']
# })
#
# # Test Age filter
# @pytest.mark.parametrize("filtering_factor, expected_output", [
#     ('15', [15]),     # Should return records for Age 0-18
#     ('25', [22, 25]), # Should return records for Age 18-35
#     ('70', [70]),     # Should return records for Age 65+
# ])
# # def test_age_filter(filtering_factor, expected_output):
# #     filter_obj = AgeFilter(data)
# #     filtered_data = filter_obj.apply_filter(filtering_factor)
# #     filtered_ages = filtered_data['Age'].tolist()
# #     assert filtered_ages == expected_output
#
# # Test Gender filter
# @pytest.mark.parametrize("filtering_factor, expected_output", [
#     ('Male', [15, 45, 25]),     # Should return records where Gender is Male
#     ('Female', [22, 70]),       # Should return records where Gender is Female
# ])
# def test_gender_filter(filtering_factor, expected_output):
#     filter_obj = GenderFilter(data)
#     filtered_data = filter_obj.apply_filter(filtering_factor)
#     filtered_ages = filtered_data['Age'].tolist()
#     assert filtered_ages == expected_output
#
# # Test Race filter
# @pytest.mark.parametrize("filtering_factor, expected_output", [
#     ('Asian', [45]),     # Should return records where Race is Asian
#     ('Hispanic', [70]),  # Should return records where Race is Hispanic
# ])
# def test_race_filter(filtering_factor, expected_output):
#     race_filter = RaceFilter(data)
#     filtered_data = race_filter.apply_filter(filtering_factor)
#     filtered_ages = filtered_data['Age'].tolist()
#     assert filtered_ages == expected_output
#
# # Test State filter
# # @pytest.mark.parametrize("filtering_factor, expected_output", [
# #     ('CA', [15, 25]),   # Should return records where State is CA
# #     ('NY', [22]),       # Should return records where State is NY
# # ])
#
# # def test_state_filter(filtering_factor, expected_output):
# #     filter_obj = StateFilter(data)
# #     filtered_data = filter_obj.apply_filter(filtering_factor)
# #     filtered_ages = filtered_data['Age'].tolist()
# #     assert filtered_ages == expected_output
