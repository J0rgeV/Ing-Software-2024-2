import React from "react";

import Card from '../UI/Card';
import Cliente from "./Cliente/Cliente";
import './Clientes.css';
import ClienteForm from "./ClienteForm/ClienteForm";

const Clientes = (props) => {
    const [clienteEliminado, setClienteEliminado] = React.useState("");

    const guardaClienteHandler = (clienteIngresado) => {
        const clientes = { 
            ...clienteIngresado
        };
        props.onAgregarCliente(clientes);
    };

    const clienteEliminadoHandler = (event) => {
        //const nuevoCliente = props.clientes.filter((cliente) => cliente.nombre !== "Fernando");
        setClienteEliminado(event.target.value);
    };

    const submitHandler = (event) => {
        event.preventDefault();
        props.onEliminarCliente(clienteEliminado);
        setClienteEliminado("");
    };

    return (
        <div>
            <div className="nuevo-cliente">
                <ClienteForm onGuardarCliente={guardaClienteHandler} />
            </div>
            <h2>Últimos 2 clientes añadidos</h2>
            <Card className='clientes'>
                <Cliente
                    nombre={props.clientes[0].nombre}
                    apellidoPat={props.clientes[0].apellidoPaterno}
                    apellidoMat={props.clientes[0].apellidoMaterno}
                    pass={props.clientes[0].password}
                    correo={props.clientes[0].correo}
                    superUsr={props.clientes[0].superusuario}
                />
                <Cliente
                    nombre={props.clientes[1].nombre}
                    apellidoPat={props.clientes[1].apellidoPaterno}
                    apellidoMat={props.clientes[1].apellidoMaterno}
                    pass={props.clientes[1].password}
                    correo={props.clientes[1].correo}
                    superUsr={props.clientes[1].superusuario}
                />
            </Card>

            <div className="nuevo-cliente">
                <Card className='clientes'>
                    <form onSubmit={submitHandler}>
                    <label>Ingrese el nombre del cliente a eliminar: </label>
                        <input
                            type="text"
                            onChange={clienteEliminadoHandler}
                            value={clienteEliminado}
                        />
                        <button type="submit">Eliminar cliente</button>
                    </form>
                </Card>
            </div>
        </div>
    )
};

export default Clientes;