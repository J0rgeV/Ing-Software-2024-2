import React from "react";

import Card from '../../UI/Card';
import './Renta.css';

const Renta = (props) => {
    return (
        <Card className='renta'>
            <div className="renta__description">
                <h2>{props.idUsuario}</h2>
                <h2>{props.idPelicula}</h2>
                <h2>{props.fechainicial}</h2>
                <h2>{props.fechafinal}</h2>
            </div>
        </Card>
    );
}

export default Renta