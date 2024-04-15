import React from "react";

import Card from '../UI/Card';
import Renta from "./Renta/Renta";
import './Rentas.css';
import RentaForm from "./RentaForm/RentaForm";

const Rentas = (props) => {

    const guardaRentaHandler = (rentaIngresada) => {
        const rentas = { 
            ...rentaIngresada
        };
        props.onAgregarRenta(rentas);
    };

    return (
        <div>
            <div className="nuevo-renta">
                <RentaForm onGuardarRenta={guardaRentaHandler} />
            </div>
            <h2>Últimas 2 rentas añadidas</h2>
            <Card className='rentas'>
                <Renta
                    idUsuario={props.rentas[0].idUsuario}
                    idPelicula={props.rentas[0].idPelicula}
                    fechainicial={props.rentas[0].fechainicial}
                    fechafinal={props.rentas[0].fechafinal}
                />
                <Renta
                    idUsuario={props.rentas[1].idUsuario}
                    idPelicula={props.rentas[1].idPelicula}
                    fechainicial={props.rentas[1].fechainicial}
                    fechafinal={props.rentas[1].fechafinal}
                />
            </Card>
        </div>
    )
};

export default Rentas;