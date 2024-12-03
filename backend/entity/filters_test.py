import pytest
import pandas as pd
from entity.filters import FilterManager, GenderFilter, RaceFilter


# Sample data for testing
data = pd.DataFrame({
    'Age': [15, 22, 25, 70, 35],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Race': ['White', 'Black', 'Asian', 'Hispanic', 'Mixed'],
    'State': ['CA', 'NY', 'TX', 'FL', 'CA']
})


# Test GenderFilter class
def test_gender_filter_valid():
    filter_obj = GenderFilter('Male')
    assert filter_obj.valid_filter() is True
    filtered_data = filter_obj.apply_filter(data)
    expected_data = data[data['Gender'] == 'Male']
    assert filtered_data.equals(expected_data)


def test_gender_filter_invalid():
    filter_obj = GenderFilter('Hello World')
    assert filter_obj.valid_filter() is False


# Test RaceFilter class
def test_race_filter_valid():
    filter_obj = RaceFilter('Black')
    assert filter_obj.valid_filter() is True
    filtered_data = filter_obj.apply_filter(data)
    expected_data = data[data['Race'] == 'Black']
    assert filtered_data.equals(expected_data)


def test_race_filter_invalid():
    filter_obj = RaceFilter('Wookie')
    assert filter_obj.valid_filter() is False


# Test FilterManager class
def test_filter_manager_initialization():
    filters = [GenderFilter('Male')]
    filter_manager = FilterManager(data, filters)
    assert filter_manager._df.equals(data)
    assert filter_manager.filters == filters


def test_apply_filters_single_valid_filter():
    filters = [GenderFilter('Male')]
    filter_manager = FilterManager(data, filters)
    filtered_df = filter_manager.apply_filters()
    expected_df = data[data['Gender'] == 'Male']
    assert filtered_df.equals(expected_df)


def test_apply_filters_multiple_valid_filters():
    filters = [GenderFilter('Male'), RaceFilter('Black')]
    filter_manager = FilterManager(data, filters)
    filtered_df = filter_manager.apply_filters()
    expected_df = data[(data['Gender'] == 'Male') &
                       (data['Race'] == 'Black')]
    assert filtered_df.equals(expected_df)


def test_apply_filters_no_valid_filters():
    filters = [GenderFilter('Hello World')]
    filter_manager = FilterManager(data, filters)
    filtered_df = filter_manager.apply_filters()
    assert filtered_df.equals(data)


def test_apply_filters_mixed_validity_filters():
    filters = [GenderFilter('Male'), RaceFilter('Alien')]
    filter_manager = FilterManager(data, filters)
    filtered_df = filter_manager.apply_filters()
    expected_df = data[data['Gender'] == 'Male']
    assert filtered_df.equals(expected_df)


if __name__ == "__main__":
    pytest.main()
