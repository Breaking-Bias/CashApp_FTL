export function formatNumberForDisplay(num: number): string {
    if (num >= 1_000_000_000) {
      const billions = num / 1_000_000_000;
      return billions >= 100
        ? `${Math.round(billions)}B`
        : `${billions.toFixed(1).replace(/\.0$/, "")}B`;
    } else if (num >= 1_000_000) {
      const millions = num / 1_000_000;
      return millions >= 100
        ? `${Math.round(millions)}M`
        : `${millions.toFixed(1).replace(/\.0$/, "")}M`;
    } else if (num >= 1_000) {
      const thousands = num / 1_000;
      return thousands >= 100
        ? `${Math.round(thousands)}K`
        : `${thousands.toFixed(1).replace(/\.0$/, "")}K`;
    } else {
      return num.toString();
    }
  }