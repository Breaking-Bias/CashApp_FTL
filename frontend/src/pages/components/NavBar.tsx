
import { AppBar, Toolbar, Typography, Button } from "@mui/material";
import { Link } from "react-router-dom"

const Navbar = () => {
    return (
        <AppBar position='sticky' sx={{backgroundColor:'green', zIndex:1}} >
            <Toolbar>
                <Typography variant="h6" sx={{flexgrow:1}}>
                Breaking Bias
                </Typography>
                <Button
                    component= {Link}
                    to="/"
                    color="inherit"
                    sx = {{textTransform:'none'}}
                    >
                        Home
                </Button>
                <Button 
                component = {Link}
                to="/graph"
                color="inherit"
                sx ={{textTransform: "none"}}
                > Results </Button>


            </Toolbar>

        </AppBar>
           
        );
    };

export default Navbar