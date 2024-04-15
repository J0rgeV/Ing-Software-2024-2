import React, { useState } from "react";

import "./ClienteForm.css";

const ClienteForm = (props) => {
  const [nombreIngresado, setNombreIngresado] = useState("");
  const [apellidoPatIngresado, setApellidoPatIngresado] = useState("");
  const [apellidoMatIngresado, setApellidoMatIngresado] = useState("");
  const [passIngresado, setPassIngresado] = useState("");
  const [correoIngresado, setCorreoIngresado] = useState("");
  const [superUsrIngresado, setSuperusuarioIngresado] = useState("");


  const cambioNombreHandler = (event) => {
    setNombreIngresado(event.target.value);
  };

  const cambioApellidoPatHandler = (event) => {
    setApellidoPatIngresado(event.target.value);
  };

  const cambioApellidoMatHandler = (event) => {
    setApellidoMatIngresado(event.target.value);
  };

  const cambioPassHandler = (event) => {
    setPassIngresado(event.target.value);
  };

  const cambioCorreoHandler = (event) => {
    setCorreoIngresado(event.target.value);
  };

  const cambioSuperUsrHandler = (event) => {
    setSuperusuarioIngresado(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const cliente = {
      nombre: nombreIngresado,
      apellidoPaterno: apellidoPatIngresado,
      apellidoMaterno: apellidoMatIngresado,
      password: passIngresado,
      correo: correoIngresado,
      superusuario: superUsrIngresado,
    };
    if (
      nombreIngresado === "" ||
      apellidoPatIngresado === "" ||
      apellidoMatIngresado === "" ||
      passIngresado === "" ||
      correoIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarCliente(cliente);
    setNombreIngresado("");
    setApellidoPatIngresado("");
    setApellidoMatIngresado("");
    setPassIngresado("");
    setCorreoIngresado("");
    setSuperusuarioIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="cliente">Cliente nuevo</div>
      <div className="nuevo-cliente__controls">
        <div className="nuevo-cliente__control">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
          />
        </div>
        <div className="nuevo-cliente__control">
          <label>Apellido Paterno: </label>
          <input
            type="text"
            value={apellidoPatIngresado}
            onChange={cambioApellidoPatHandler}
          />
        </div>
        <div className="nuevo-cliente__control">
          <label>Apellido Materno: </label>
          <input
            type="text"
            value={apellidoMatIngresado}
            onChange={cambioApellidoMatHandler}
          />
        </div>
        <div className="nuevo-cliente__control">
          <label>Contraseña: </label>
          <input
            type="password"
            value={passIngresado}
            onChange={cambioPassHandler}
          />
        </div>
        <div className="nuevo-cliente__control">
          <label>Correo electrónico: </label>
          <input
            type="email"
            value={correoIngresado}
            onChange={cambioCorreoHandler}
          />
        </div>
        <div className="nuevo-cliente__control">
          <label>Superusuario: </label>
          {/* <input
            type="int"
            value={superUsrIngresado}
            onChange={cambioSuperUsrHandler}
          /> */}
          <input min="0" max="1" value={superUsrIngresado} onChange={cambioSuperUsrHandler}/>
        </div>
        <div className="nuevo-cliente__actions">
          <button className="nuevo-cliente__actions" type="submit">Agregar cliente</button>
        </div>
      </div>
    </form>
  );
};

export default ClienteForm;
