import { FormattedDataEntry, RawDataEntry } from "./types";

const SERVER_URL = process.env.VITE_SERVER_URL;

export async function getPastDataAPICall(filterFactor: string) {
    const endpoint = `${SERVER_URL}/getPastData`;

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ filtering_factor: filterFactor }),
        });

        if (!response.ok) {
            throw new Error("Error in response: " + response.statusText);
        }

        const data: RawDataEntry[] = await response.json();

        // Turns the ISO dates into JavaScript date objects   
        const formattedData: FormattedDataEntry[] = data.map(
            (entry) => ({
                date: new Date(entry.date),
                value: entry.value,
            })
        );

        return formattedData      

    } catch (error) {
        console.error("Error:", error);
    }
}


export async function getPastDataUnbiasedAPICall(filterFactor: string) {
    const endpoint = `${SERVER_URL}/getPastDataUnbiased`;

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ filtering_factor: filterFactor }),
        });

        if (!response.ok) {
            throw new Error("Error in response: " + response.statusText);
        }

        const data: RawDataEntry[] = await response.json();

        // Turns the ISO dates into JavaScript date objects   
        const formattedData: FormattedDataEntry[] = data.map(
            (entry) => ({
                date: new Date(entry.date),
                value: entry.value,
            })
        );

        return formattedData      

    } catch (error) {
        console.error("Error:", error);
    }
}