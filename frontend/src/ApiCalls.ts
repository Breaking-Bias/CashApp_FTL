import { FormattedDataEntry, RawDataEntry } from "./types";

const SERVER_URL = process.env.VITE_SERVER_URL;

async function genericPostCall(endpoint: string, params: object) {
    const fullEndpoint = `${SERVER_URL}${endpoint}`;

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

        const data: [RawDataEntry[], never] = await response.json();
        const rawData = data[0];

        // Turns the ISO dates into JavaScript date objects   
        const formattedData: FormattedDataEntry[] = rawData.map(
            (entry) => ({
                date: new Date(entry.date),
                value: entry.num_transactions,
            })
        );

        return formattedData      

    } catch (error) {
        console.error("Error:", error);
    }
}

export async function getPastDataAPICall(filterFactor: string) {
    return await genericPostCall("/getPastData", { filtering_factor: filterFactor })
}

export async function getPastDataUnbiasedAPICall(filterFactor: string) {
    return await genericPostCall("/getPastDataUnbiased", { filtering_factor: filterFactor })
}

export async function predictDataAPICall(filterFactor: string, numPoints: number) {
    return await genericPostCall("/predictData", { filtering_factor: filterFactor, num_points: numPoints })
}

export async function predictDataUnbiasedAPICall(filterFactor: string, numPoints: number) {
    return await genericPostCall("/predictDataUnbiased", { filtering_factor: filterFactor, num_points: numPoints })
}