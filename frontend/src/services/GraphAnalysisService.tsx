export class GraphAnalysisService {
    static getMetricType(mode: string): string {
      return mode === "0" ? "transactions" : "revenue";
    }
  
    static calculatePercentageChange(
      predictedBiasedLine: Array<{ value: number }>, 
      predictedUnbiasedLine: Array<{ value: number }>
    ): string {
      const latestBiased = predictedBiasedLine[predictedBiasedLine.length - 1]?.value || 0;
      const latestUnbiased = predictedUnbiasedLine[predictedUnbiasedLine.length - 1]?.value || 0;
      
      if (latestBiased === 0) return "0";
      
      return ((latestUnbiased - latestBiased) / latestBiased * 100).toFixed(1);
    }
  
    static formatFilterDescription(filterGender: string, filterRace: string): string {
      if (filterGender === "NoFilter" && filterRace === "NoFilter") {
        return "with no filters applied";
      }
  
      const genderPart = filterGender !== "NoFilter" 
        ? `filtered by Gender: ${filterGender}` 
        : '';
  
      const racePart = filterRace !== "NoFilter"
        ? `${filterGender !== "NoFilter" ? ' and' : ''} filtered by Race: ${filterRace}`
        : '';
  
      return genderPart + racePart;
    }
  }