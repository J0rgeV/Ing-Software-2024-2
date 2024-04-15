import React from "react";

import Card from '../UI/Card';
import Pelicula from "./Pelicula/Pelicula";
import './Peliculas.css';
import PeliculaForm from "./PeliculaForm/PeliculaForm";

const Peliculas = (props) => {
    const [peliculaEliminada, setPeliculaEliminada] = React.useState("");

    const guardaPeliculaHandler = (peliculaIngresada) => {
        const peliculas = { 
            ...peliculaIngresada
        };
        props.onAgregarPelicula(peliculas);
    };

    const peliculaEliminadaHandler = (event) => {
        //const nuevoCliente = props.clientes.filter((cliente) => cliente.nombre !== "Fernando");
        setPeliculaEliminada(event.target.value);
    };

    const submitHandler = (event) => {
        event.preventDefault();
        props.onEliminarPelicula(peliculaEliminada);
        setPeliculaEliminada("");
    };

    return (
        <div>
            <div className="nuevo-pelicula">
                <PeliculaForm onGuardarPelicula={guardaPeliculaHandler} />
            </div>
            <h2>Últimas 2 películas añadidas</h2>
            <Card className='peliculas'>
                <Pelicula
                    titulo={props.peliculas[0].titulo}
                    genero={props.peliculas[0].genero}
                    duracion={props.peliculas[0].duracion}
                    inventario={props.peliculas[0].inventario}
                />
                <Pelicula
                    titulo={props.peliculas[1].titulo}
                    genero={props.peliculas[1].genero}
                    duracion={props.peliculas[1].duracion}
                    inventario={props.peliculas[1].inventario}
                />
            </Card>
            <div className="nuevo-pelicula">
                <Card className='peliculas'>
                    <form onSubmit={submitHandler}>
                    <label>Ingrese el nombre de la película a eliminar: </label>
                        <input
                            type="text"
                            onChange={peliculaEliminadaHandler}
                            value={peliculaEliminada}
                        />
                        <button type="submit">Eliminar cliente</button>
                    </form>
                </Card>
            </div>
        </div>
    )
};

export default Peliculas;