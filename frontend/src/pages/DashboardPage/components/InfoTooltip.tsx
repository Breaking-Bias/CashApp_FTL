import { IconButton, Tooltip } from "@mui/material";
import HelpIcon from "@mui/icons-material/Help";

interface Props {
  title: string;
  ariaLabel: string;
}

export default function InfoTooltip({ title, ariaLabel }: Props) {
  return (
    <Tooltip title={<span style={{ fontSize: "16px" }}>{title}</span>}>
      <IconButton
        aria-label={ariaLabel}
        style={{ fontSize: "30px", padding: "4px", marginLeft: "4px" }}
      >
        <HelpIcon style={{ fontSize: "30px" }} />
      </IconButton>
    </Tooltip>
  );
}
