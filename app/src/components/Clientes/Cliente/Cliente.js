import React from "react";

import Card from '../../UI/Card';
import './Cliente.css';

const Cliente = (props) => {
    return (
        <Card className='cliente'>
            <div className="cliente__description">
                <h2>{props.nombre}</h2>
                <h2>{props.apellidoPat}</h2>
                <h2>{props.apellidoMat}</h2>
                <h2>{props.pass}</h2>
                <h2>{props.correo}</h2>
                <h2>{props.superUsr}</h2>
            </div>
        </Card>
    );
}

export default Cliente