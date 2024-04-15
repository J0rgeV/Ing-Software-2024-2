import React from "react";

import Card from '../../UI/Card';
import './Pelicula.css';

const Pelicula = (props) => {
    return (
        <Card className='pelicula'>
            <div className="pelicula__description">
                <h2>{props.titulo}</h2>
                <h2>{props.genero}</h2>
                <h2>{props.duracion} min</h2>
                <h2>{props.inventario}</h2>
            </div>
        </Card>
    );
}

export default Pelicula