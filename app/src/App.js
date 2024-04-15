/*import logo from './logo.svg';*/
import './App.css';
import React, { useState } from "react";
import Clientes from "./components/Clientes/Clientes";
import Peliculas from "./components/Peliculas/Peliculas";
import Rentas from "./components/Rentas/Rentas";
import Card from './components/UI/Card';

function App() {
  const [rentas, setRentas] = useState([
    { idUsuario: "3423", idPelicula: "3", fechainicial: "12/03/2024", fechafinal: "27/03/2024" },
    { idUsuario: "234", idPelicula: "7", fechainicial: "30/01/2024", fechafinal: "13/02/2024" },
    { idUsuario: "12", idPelicula: "28", fechainicial: "02/04/2024", fechafinal: "17/04/2024" },
  ]);

  const [peliculas, setPeliculas] = useState([
    { titulo: "Spiderman", genero: "acción", duracion: "120", inventario: 3 },
    { titulo: "Batman", genero: "acción", duracion: "95", inventario: 7 },
    { titulo: "Inception", genero: "ficción", duracion: "100", inventario: 4 },
  ]);

  const [clientes, setClientes] = useState([
    {
      nombre: "Fernando",
      apellidoPaterno: "Fong",
      apellidoMaterno: "Garcia",
      password: "1234",
      correo: "edrfcr@hohotmail.com",
      superusuario: 0,
    },
    {
      nombre: "Daniel",
      apellidoPaterno: "Garcia",
      apellidoMaterno: "Landa",
      password: "1234",
      correo: "cvferw@gotmail.com",
      superusuario: 0,
    },
    {
      nombre: "Erick",
      apellidoPaterno: "Martinez",
      apellidoMaterno: "Garcia",
      password: "1234",
      correo: "qwe@ggmail.com",
      superusuario: 1,
    },
  ]);

  const agregarCliente = (cliente) => {
    const nuevoCliente = [cliente, ...clientes];
    setClientes(nuevoCliente);
    console.log(nuevoCliente);
  };

  const agregarPelicula = (pelicula) => {
    const nuevaPelicula = [pelicula, ...peliculas];
    setPeliculas(nuevaPelicula);
    console.log(nuevaPelicula);
  };

  const agregarRenta = (renta) => {
    const nuevaRenta = [renta, ...rentas];
    setRentas(nuevaRenta);
    console.log(nuevaRenta);
  };

  const eliminarCliente = (nombre) => {
    const nuevoCliente = clientes.filter((cliente) => cliente.nombre !== nombre);
    setClientes(nuevoCliente);
    console.log(nuevoCliente);
  }

  const eliminarPelicula = (nombre) => {
    const nuevaPelicula = clientes.filter((pelicula) => pelicula.nombre !== nombre);
    setPeliculas(nuevaPelicula);
    console.log(nuevaPelicula);
  }

  const eliminarRenta = (nombre) => {
    const nuevoCliente = clientes.filter((renta) => renta.nombre !== nombre);
    setRentas(nuevoCliente);
    console.log(nuevoCliente);
  }

  return (
    <div className="App">
      <Card className='clientes'><h2>Eliga la acción a realizar</h2></Card>
      <br></br>
      <Card className='clientes'><h2>Clientes</h2></Card>
      <Clientes onAgregarCliente={agregarCliente} onEliminarCliente={eliminarCliente} clientes={clientes} />

      <Card className='clientes'><h2>Películas</h2></Card>
      <Peliculas onAgregarPelicula={agregarPelicula} onEliminarPelicula={eliminarPelicula} peliculas={peliculas} />

      <Card className='clientes'><h2>Rentas</h2></Card>
      <Rentas onAgregarRenta={agregarRenta} onEliminarRenta={eliminarRenta} rentas={rentas}/>
    </div>
  );
}

export default App;
