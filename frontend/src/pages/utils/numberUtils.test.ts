import { formatNumberForDisplay } from "./numberUtils";

describe("formatNumberForDisplay", () => {
    it("Formats a number in the millions", () => {

        const result = formatNumberForDisplay(21_410_000)
        expect(result).toEqual("21.4M")
    });

    it("Formats a number in the thousands", () => {

        const result = formatNumberForDisplay(4_190)
        expect(result).toEqual("4.2K")
    });

    it("Formats a number in the billions", () => {

        const result = formatNumberForDisplay(150_000_000_000)
        expect(result).toEqual("150B")
    });
});
