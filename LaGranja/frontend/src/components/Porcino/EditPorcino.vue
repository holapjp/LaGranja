<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h3>Editar información de porcinos:</h3>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit.prevent="onSubmit()">
                            <div class="form-group row">
                                <label for="raza" class="col-1 col-form-label">Raza:</label>
                                <div class="col-sm-8">
                                    <input type="text" placeholder="Example: Yorkshire" name="raza" class="form-control" v-model.trim="form.raza">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="edad" class="col-1 col-form-label">Edad:</label>
                                <div class="col-sm-8">
                                    <input type="number" placeholder="0" name="edad" class="form-control" v-model.trim="form.edad">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="peso" class="col-1 col-form-label">Peso:</label>
                                <div class="col-sm-8">
                                    <input type="number" placeholder="0" name="peso" class="form-control" v-model.trim="form.peso">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="cliente" class="col-1 col-form-label">Cliente:</label>
                                <div class="col-sm-8">
                                    <select id="cliente" class="form-control" v-model="form.cliente">
                                        <option v-for="item in clientes" :key="item.id" :value="item.id">
                                            {{ item.nombres }} {{ item.apellidos }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="alimentacion" class="col-2 col-form-label">Alimentación: </label>
                                <div class="col-sm-8">
                                    <select v-model="form.alimentacion" id="id" class="form-control">
                                        <option v-for="item in alimentaciones" :key="item.id" :value="item.id">
                                            {{ item.dosis }}
                                        </option>
                                    </select>
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
import { usePorcinosAPI }  from '@/composables/usePorcinosAPI.js'
export default {
    props: {
        porcinoId: {
            type: Number,
            required: true
        } 
    },
    setup(props) {
        // const route = useRoute();
        const { getClientes, getAlimentaciones, clientes, alimentaciones } =  usePorcinosAPI()
        const { emit }  = getCurrentInstance()
        const porcinoId = props.porcinoId

        let form = ref({
            raza: '',
            edad: 0,
            peso: 0,
            cliente: 0,
            alimentacion: 0
        })

        const cancelarEditar = () => {
            emit('CancelarEditar',false)
        }

        const onSubmit = () =>{
            console.log('envio del formulario evitado')
            console.log(form.value)
            const path = `http://localhost:8000/api/v1.0/porcinos/${porcinoId}/`
            axios.put(path, {
                id: porcinoId,
                raza: form.value.raza,
                edad: form.value.edad,
                peso: form.value.peso,
                clienteId: form.value.cliente,
                alimentacionId: form.value.alimentacion  
            }).then((response) => {
                swal.fire("Porcino actualizado existosamente!","","success")
                emit('updateInfo')
            }).catch((error) => {
                swal.fire("Oops...", "Algo salió mal", "error");
                console.log(error)

            })
        }

        const getPorcino = ()=> {
            const path = `http://127.0.0.1:8000/api/v1.0/porcinos/${porcinoId}/`

            axios.get(path).then((response) => {
                form.value.raza = response.data.raza
                form.value.edad = response.data.edad
                form.value.peso = response.data.peso
                form.value.cliente = response.data.cliente.id
                form.value.alimentacion = response.data.alimentacion.id

            }).catch((error) => {
                console.log(error)
            })
        
        }

        onMounted(() => {
            getPorcino(),
            getClientes(),
            getAlimentaciones()
        })

        return {
            porcinoId,
            form,
            clientes,
            alimentaciones,
            cancelarEditar,
            onSubmit,
        }
    }
}
</script>
<style lang="">
</style>