<template>
    <div class="container">
        <h2>Listado de clientes:</h2>
        <b-table :items="clientes" :fields="fields" stripped hover>
            <template #cell(accion)="data">
                <b-button-group>
                    <b-button squared variant="outline-secondary" @click="MostarEditar(data.item.id)">{{ editar
                        }}</b-button>
                    <b-button squared variant="outline-danger" @click="Eliminar(data.item.id)">Eliminar</b-button>
                </b-button-group>
            </template>
        </b-table>
        <editCliente v-if="show" @updateInfo="updateInfo()" @CancelarEditar="OcultarEditar()" :clienteId="clienteId">
        </editCliente>
        <newCliente v-if="!show" @nuevoCliente="getClientes()"></newCliente>
    </div>
</template>
<script>
import editCliente from '@/components/clientes/EditCliente.vue';
import { ref, onMounted } from 'vue'
import axios from 'axios'
import swal from 'sweetalert2';
import newCliente from '@/components/clientes/NewCliente.vue';

export default {
    components: { editCliente, newCliente },
    setup() {
        const fields = [
            { key: "id", label: "ID" },
            { key: "cedula", label: "Cédula", variant: "info" },
            { key: "nombres", label: "Nombres" , variant: "info"},
            { key: "apellidos", label: "Apellidos" , variant: "info"},
            { key: "direccion", label: "Dirección", variant: "info" },
            { key: "telefono", label: "Teléfono", variant: "info" },
            { key: "accion", label: "Acción" }
        ]
        let editar = ref('Editar')
        let clienteId = ref(0)
        let show = ref(null)
        let clientes = ref([])
        let clienteModal = ref(false)
        const getClientes = () => {
            const path = "http://127.0.0.1:8000/api/v1.0/clientes/"
            axios.get(path).then((response) => {
                clientes.value = response.data
                console.log(clientes)
            }).catch((error) => {
                console.log(error)
            })
        }

        const MostarEditar = (id) => {
            clienteId.value = id
            console.log(show.value, editar.value)
            show.value = !show.value
            editar.value = show.value ? 'Cancelar' : 'Editar'
            console.log(id)

        }

        const updateInfo = () => {
            getClientes()
            OcultarEditar()
        }

        const OcultarEditar = (data) => {
            show.value = data
            editar.value = 'Editar'
        }

        onMounted(() => {
            getClientes()
        })

        const Eliminar = (clienteId) => {
            swal.fire({
                title: "¿Seguro?",
                text: "Una vez eliminada la información de un porcino, no hay vuelta atrás..",
                icon: "warning",
                showCancelButton: true,
                cancelButtonColor: "#3085d6",
                confirmButtonColor: "#d33",
                cancelButtonText: "Cancelar",
                confirmButtonText: "Eliminar"
            }).then((result) => {
                if (result.isConfirmed) {
                    const path = `http://localhost:8000/api/v1.0/clientes/${clienteId}/`
                    axios.delete(path).then((response) => {
                        console.log(response)
                        getClientes()
                        swal.fire({
                            title: "Eliminado",
                            text: "Se ha borrado la información de un cliente.",
                            icon: "success"
                        })
                    }).catch((error) => {
                        console.log(error)
                    })
                }
            });
        }


        const showCrearClienteModal = () => {
            console.log("Mostrar")
            clienteModal.value = !clienteModal.value

        }

        return {
            fields,
            clientes,
            show,
            clienteId,
            editar,
            MostarEditar,
            OcultarEditar,
            updateInfo,
            Eliminar,
            showCrearClienteModal,
            getClientes,
            clienteModal,
        }
    },
}
</script>
<style lang="">

</style>