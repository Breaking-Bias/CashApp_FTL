export interface PastData {
    frequency_graph: {
      past_biased_line: AlmostFormattedDataEntry[]
    }
    revenue_graph: {
      past_biased_line: AlmostFormattedDataEntry[]
    }  
  }

export interface FormattedDataEntry {
    date: Date;
    value: number;
  }
  
export interface DataSeries {
    name: string;
    color: string;
    data: FormattedDataEntry[];
  }

export interface AlmostFormattedDataEntry {
    date: string;
    value: number;
  }

export interface BigGraphData {
  frequency_graph: {
    average_difference: number
    total_difference: number
    past_biased_line: AlmostFormattedDataEntry[]
    past_unbiased_line: AlmostFormattedDataEntry[]
    predicted_biased_line: AlmostFormattedDataEntry[]
    predicted_unbiased_line: AlmostFormattedDataEntry[]
  },
  revenue_graph: {
    average_difference: number
    total_difference: number
    past_biased_line: AlmostFormattedDataEntry[]
    past_unbiased_line: AlmostFormattedDataEntry[]
    predicted_biased_line: AlmostFormattedDataEntry[]
    predicted_unbiased_line: AlmostFormattedDataEntry[]
  }
}

export interface OneModeGraphData {
    average_difference: number
    total_difference: number
    past_biased_line: FormattedDataEntry[]
    past_unbiased_line: FormattedDataEntry[]
    predicted_biased_line: FormattedDataEntry[]
    predicted_unbiased_line: FormattedDataEntry[]
}

export interface FormattedBigGraphData {
  frequency_graph: OneModeGraphData,
  revenue_graph: OneModeGraphData
}
