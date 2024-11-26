import { getPastDataAPICall, getGraphDataAPICall } from "./ApiCalls";

jest.mock("./ApiCalls", () => ({
    getPastDataAPICall: jest.fn(),
    getGraphDataAPICall: jest.fn(),
}));

describe("getPastDataAPICall", () => {
    it("should handle API response correctly", async () => {
        const mockResponse = [ 
            {date: Date(), value: 40}, 
            {date: Date(), value: 24}, 
            {date: Date(), value: 33}
        ];

        (getPastDataAPICall as jest.Mock).mockResolvedValue(mockResponse);

        const params = {
            filtering_factor: ["Male", "Asian"],
            num_points: 30,
        };

        const result = await getPastDataAPICall(params, "0");
        
        expect(result).toEqual(mockResponse);
        expect(getPastDataAPICall).toHaveBeenCalledWith(params, "0");        
    });
});

describe("getGraphDataAPICall", () => {
    it("should handle API response correctly", async () => {
        const mockResponse = {
            frequency_graph: {
                average_difference: 51,
                total_difference: 295,
                past_biased_line: [ {date: Date(), value: 40}, {date: Date(), value: 33} ],
                past_unbiased_line: [ {date: Date(), value: 43}, {date: Date(), value: 55} ],
                predicted_biased_line: [ {date: Date(), value: 26}, {date: Date(), value: 23} ],
                predicted_unbiased_line: [ {date: Date(), value: 39}, {date: Date(), value: 29} ],
            },
            revenue_graph: {                
                average_difference: 63,
                total_difference: 325,
                past_biased_line: [ {date: Date(), value: 10}, {date: Date(), value: 20} ],
                past_unbiased_line: [ {date: Date(), value: 14}, {date: Date(), value: 21} ],
                predicted_biased_line: [ {date: Date(), value: 11}, {date: Date(), value: 23} ],
                predicted_unbiased_line: [ {date: Date(), value: 19}, {date: Date(), value: 13} ],
            },
        };
        

        (getGraphDataAPICall as jest.Mock).mockResolvedValue(mockResponse);

        const params = {
            filtering_factor: ["Male", "Asian"],
            num_points: 30,
        };

        const result = await getGraphDataAPICall(params);
        
        expect(result).toEqual(mockResponse);
        expect(getGraphDataAPICall).toHaveBeenCalledWith(params);
    });
});
