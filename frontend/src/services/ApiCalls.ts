import { AlmostFormattedDataEntry, BigGraphData, FormattedBigGraphData, FormattedDataEntry, PastData } from "../types";

const SERVER_URL = process.env.VITE_SERVER_URL;

export async function getPastDataAPICall(params: object, mode: string) {
    const fullEndpoint = `${SERVER_URL}/getPastData`;
    
    try {
        const response = await fetch(fullEndpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(params),
        });
        
        if (!response.ok) {
            throw new Error("Error in response: " + response.statusText);
        }

        const data: PastData = await response.json();
        const rawData = mode === "0" ? data.frequency_graph.past_biased_line : data.revenue_graph.past_biased_line;
        
        // Turns the ISO dates into JavaScript date objects   
        const formattedData: FormattedDataEntry[] = rawData.map(
            (entry: { date: string; value: number }) => ({
                date: new Date(entry.date),
                value: entry.value,
            })
        );

        return formattedData      

    } catch (error) {
        console.error("Error:", error);
    }
}

const formatLineData = (line: AlmostFormattedDataEntry[]): FormattedDataEntry[] => {
    return line.map(entry => ({
      date: new Date(entry.date), // Convert the date string to a Date object
      value: entry.value,         // Copy the value as is
    }));
  };

export async function getGraphDataAPICall(params: object) {
    const fullEndpoint = `${SERVER_URL}/getGraphData`;
    
    try {
        const response = await fetch(fullEndpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(params),
        });
        
        if (!response.ok) {
            throw new Error("Error in response: " + response.statusText);
        }

        const rawData: BigGraphData = await response.json();
        
        // Turns the ISO dates into JavaScript date objects   
        const formattedData: FormattedBigGraphData = {
            frequency_graph: {
              average_difference: rawData.frequency_graph.average_difference,
              total_difference: rawData.frequency_graph.total_difference,
              past_biased_line: formatLineData(rawData.frequency_graph.past_biased_line),
              past_unbiased_line: formatLineData(rawData.frequency_graph.past_unbiased_line),
              predicted_biased_line: formatLineData(rawData.frequency_graph.predicted_biased_line),
              predicted_unbiased_line: formatLineData(rawData.frequency_graph.predicted_unbiased_line),
            },
            revenue_graph: {
              average_difference: rawData.revenue_graph.average_difference,
              total_difference: rawData.revenue_graph.total_difference,
              past_biased_line: formatLineData(rawData.revenue_graph.past_biased_line),
              past_unbiased_line: formatLineData(rawData.revenue_graph.past_unbiased_line),
              predicted_biased_line: formatLineData(rawData.revenue_graph.predicted_biased_line),
              predicted_unbiased_line: formatLineData(rawData.revenue_graph.predicted_unbiased_line),
            },
          };

        return formattedData      

    } catch (error) {
        console.error("Error:", error);
    }
}
