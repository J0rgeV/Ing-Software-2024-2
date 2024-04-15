import React, { useState } from "react";

import "./RentaForm.css";

const RentaForm = (props) => {
  const [idUsrIngresado, setIdUsrIngresado] = useState("");
  const [idPeliIngresado, setIdPeliIngresado] = useState("");


  const cambioIdUsrHandler = (event) => {
    setIdUsrIngresado(event.target.value);
  };

  const cambioIdPeliHandler = (event) => {
    setIdPeliIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const renta = {
      IdUsuario: idUsrIngresado,
      idPelicula: idPeliIngresado,
      fechainicial: "13/03/2024",
      fechafinal: "28/03/2024",
    };
    if (
      idUsrIngresado === "" ||
      idPeliIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarRenta(renta);
    setIdUsrIngresado("");
    setIdPeliIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="renta">Renta nueva</div>
      <div className="nuevo-renta__controls">
        <div className="nuevo-renta__control">
          <label>Id del Usuario: </label>
          <input
            type="text"
            value={idUsrIngresado}
            onChange={cambioIdUsrHandler}
          />
        </div>
        <div className="nuevo-renta__control">
          <label>Id de la Película: </label>
          <input
            type="text"
            value={idPeliIngresado}
            onChange={cambioIdPeliHandler}
          />
        </div>
        <div className="nuevo-renta__actions">
          <button type="submit">Agregar renta</button>
        </div>
      </div>
    </form>
  );
};

export default RentaForm;
