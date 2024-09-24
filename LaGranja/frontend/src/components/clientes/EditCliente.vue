<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h3>Editar información de cliente:</h3>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit.prevent="onSubmit()">
                            <div class="form-group row">
                                <label for="cedula" class="col-1 col-form-label">Cédula:</label>
                                <div class="col-sm-8">
                                    <input type="text" name="cedula" class="form-control" v-model.trim="form.cedula">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="nombres" class="col-1 col-form-label">Nombres:</label>
                                <div class="col-sm-8">
                                    <input type="text" name="nombres" class="form-control" v-model.trim="form.nombres">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="apellidos" class="col-1 col-form-label">Apellidos:</label>
                                <div class="col-sm-8">
                                    <input type="text" name="apellidos" class="form-control" v-model.trim="form.apellidos">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="direccion" class="col-1 col-form-label">Dirección:</label>
                                <div class="col-sm-8">
                                    <input type="text" name="direccion" class="form-control" v-model.trim="form.direccion">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="telefono" class="col-1 col-form-label">Teléfono:</label>
                                <div class="col-sm-8">
                                    <input type="text" name="telefono" class="form-control" v-model.trim="form.telefono">
                                </div>
                            </div>
                            <div class="rows">
                                <b-button-group>
                                    <b-button type="submit"  variant="outline-secondary" squared>Confirmar cambios</b-button>
                                    <b-button variant="outline-danger" squared @click="cancelarEditar()">Cancelar</b-button>
                                </b-button-group>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { onMounted, ref, getCurrentInstance } from 'vue';
import swal from 'sweetalert2';
export default {
    props: {
        clienteId: {
            type: Number,
            required: true
        } 
    },
    setup(props) {
        // const route = useRoute();
        const { emit }  = getCurrentInstance()
        const clienteId = props.clienteId

        let form = ref({
            cedula:'',
            nombres:'',
            apellidos:'',
            direccion:'',
            telefono:'',
        })

        const cancelarEditar = () => {
            emit('CancelarEditar',false)
        }

        const onSubmit = () =>{
            console.log('envio del formulario evitado')
            console.log(form.value)
            const path = `http://localhost:8000/api/v1.0/clientes/${clienteId}/`
            axios.put(path, {
                id: clienteId,
                cedula: form.value.cedula,
                nombres: form.value.nombres,
                apellidos: form.value.apellidos,
                direccion: form.value.direccion,
                telefono: form.value.telefono  
            }).then((response) => {
                swal.fire("Cliente actualizado existosamente!","","success")
                emit('updateInfo')
            }).catch((error) => {
                swal.fire("Oops...", "Algo salió mal", "error");
                console.log(error)

            })
        }

        const getCliente = ()=> {
            const path = `http://127.0.0.1:8000/api/v1.0/clientes/${clienteId}/`

            axios.get(path).then((response) => {
                form.value.cedula = response.data.cedula
                form.value.nombres = response.data.nombres
                form.value.apellidos = response.data.apellidos
                form.value.direccion = response.data.direccion
                form.value.telefono = response.data.telefono
            }).catch((error) => {
                console.log(error)
            })
        
        }

        onMounted(() => {
            getCliente()
        })

        return {
            clienteId,
            form,
            cancelarEditar,
            onSubmit,
        }
    }
}
</script>
<style lang="">
</style>