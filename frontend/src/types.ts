export interface RawDataEntry {
    date: string;
    value: number;
  }

export interface FormattedDataEntry {
    date: Date;
    value: number;
  }
  
export interface DataSeries {
    name: string;
    color: string;
    data: { date: Date; value: number }[];
  }