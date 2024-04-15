import React, { useState } from "react";

import "./PeliculaForm.css";

const PeliculaForm = (props) => {
  const [tituloIngresado, setTituloIngresado] = useState("");
  const [generoIngresado, setGeneroIngresado] = useState("");
  const [duracionIngresada, setDuracionIngresada] = useState("");
  const [inventarioIngresado, setInventarioIngresado] = useState("");


  const cambioTituloHandler = (event) => {
    setTituloIngresado(event.target.value);
  };

  const cambioGeneroHandler = (event) => {
    setGeneroIngresado(event.target.value);
  };

  const cambioDuracionHandler = (event) => {
    setDuracionIngresada(event.target.value);
  };

  const cambioInventarioHandler = (event) => {
    setInventarioIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const pelicula = {
      titulo: tituloIngresado,
      genero: generoIngresado,
      duracion: duracionIngresada,
      inventario: inventarioIngresado,
    };
    if (
      tituloIngresado === "" ||
      generoIngresado === "" ||
      duracionIngresada === "" ||
      inventarioIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarPelicula(pelicula);
    setTituloIngresado("");
    setGeneroIngresado("");
    setDuracionIngresada("");
    setInventarioIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="pelicula">Pelicula nueva</div>
      <div className="nuevo-pelicula__controls">
        <div className="nuevo-pelicula__control">
          <label>Título: </label>
          <input
            type="text"
            value={tituloIngresado}
            onChange={cambioTituloHandler}
          />
        </div>
        <div className="nuevo-pelicula__control">
          <label>Género: </label>
          <input
            type="text"
            value={generoIngresado}
            onChange={cambioGeneroHandler}
          />
        </div>
        <div className="nuevo-pelicula__control">
          <label>Duración: </label>
          <input
            type="text"
            value={duracionIngresada}
            onChange={cambioDuracionHandler}
          />
        </div>
        <div className="nuevo-pelicula__control">
          <label>Inventario: </label>
          <input
            type="password"
            value={inventarioIngresado}
            onChange={cambioInventarioHandler}
          />
        </div>
        <div className="nuevo-pelicula__actions">
          <button type="submit">Agregar película</button>
        </div>
      </div>
    </form>
  );
};

export default PeliculaForm;
