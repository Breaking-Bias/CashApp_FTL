import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import {ToggleButton, ToggleButtonGroup} from "@mui/material";

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 800,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

const style_subheading = {
    // fontWeight: "bold",
    marginBottom: 0.5,
    textAlign: "left",
};

interface Props {
    open: boolean;
    setOpen: (open: boolean) => void;
}

export default function HelpModal({open, setOpen}: Props) {
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    return (
        <div>
            <Button color="success"
                    variant="contained"
                    onClick={handleOpen}>Help</Button>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-instructions"
                aria-describedby="modal-intructions-description"
            >
                <Box sx={style}>
                    <Typography id="instructions-title" variant="h3"
                                component="h1" color="success"
                                fontWeight={"bold"} marginBottom={3}>
                        How to Use the App
                    </Typography>
                    <Typography id="working-with-the-graph" variant="h5"
                                component="h2" sx={style_subheading}>
                        Use the button at the top of this page to switch views:
                    </Typography>
                    <Box display="flex" justifyContent={"center"}>
                    <ToggleButtonGroup
                        color="success"
                        disabled
                        exclusive
                        aria-label="Graph type"
                    >
                        <ToggleButton value="1">Revenue</ToggleButton>
                        <ToggleButton value="0">Frequency</ToggleButton>
                    </ToggleButtonGroup>
                    </Box>
                    <Typography id="customizing-the-graph" variant="h5"
                                component="h2" sx={style_subheading}>
                        Customizing Your Graph:
                    </Typography>
                    <Typography id="actions" variant="body1" component="div">
                        <strong>Filter</strong>: Customize data views using filters.
                        <br />
                        <strong>Prediction Size</strong>: Adjust the slider to define prediction size.
                    </Typography>
                    <Typography id="actions" variant="h5" component="h2"
                                sx={style_subheading}>
                        Actions:
                    </Typography>
                    <Typography id="actions" variant="body1" component="div">
                        Click <strong>Make Forecast</strong> to visualize data.
                        <br />
                        Click <strong>Export Graph</strong> to download a PDF version.
                    </Typography>
                </Box>
            </Modal>
        </div>
    );
}
