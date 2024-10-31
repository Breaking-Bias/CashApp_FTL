import React from 'react';

//const Button: React.FC = () => {
    //return (<button style={{ color: 'black' , backgroundColor:'green', padding: '10px 20px'}}>
        //Dashboard Button
        //</button>
    //);
//};

type ButtonProps = {
    backgroundColor : string;
    fontSize: number;
};

export default function Button({
}: ButtonProps) {
    return <button> 
        Dashboard Button 
    </button>
}
