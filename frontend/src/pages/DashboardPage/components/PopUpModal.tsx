import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};


 
export default function BasicModal() {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  
  const PopUpModal: React.FC = ( ) => {
  return (
    <div>
      <Button onClick={handleOpen}>Open modal</Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
          How to Use the App
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
          <h1>Working with Graphs</h1>
          <p>Use the button at the top of this page to switch views in:</p>          <ul>
            <p><strong>Transaction Value</strong></p>
            <p><strong>Transaction Frequency</strong></p>
          </ul>
          
          <h1>Customizing Your Graph</h1>
          <ul>
            <p><strong>Filter</strong>: Customize data views using filters.</p>
            <p><strong>Prediction Size</strong>: Adjust the slider to define prediction size.</p>
          </ul>

          <h1>Actions</h1>
          <p>Click <strong>Make Forecast</strong> to visualize data.</p>
          <p>Click <strong>Export Graph</strong> to download a PDF version.</p>
          
          </Typography>
        </Box>
      </Modal>
    </div>
  );
}
}

export default PopUpModal;
