export interface DataEntry {
    date: string; // THIS CAN BE CHANGED GUYS
    value: number;
  }
  
export interface DataSeries {
    name: string;
    color: string;
    data: { date: Date; value: number }[];
  }