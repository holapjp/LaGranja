<template>
    <div class="container">
        <h2>Listado de porcinos:</h2>
        <b-table :items="porcinos" :fields="fields" stripped hover>
            <template #cell(dosis)='data'>
                {{ data.item.alimentacion.dosis }}
            </template>
            <template #cell(descripcion)='data'>
                {{ data.item.alimentacion.descripcion }}
            </template>
            <template #cell(cliente)='data'>
                {{ data.item.cliente.nombres }} {{ data.item.cliente.apellidos }}
            </template>
            <template #cell(accion)="data">
                <b-button-group>
                    <b-button squared variant="outline-secondary" @click="MostarEditar(data.item.id)">{{ editar
                        }}</b-button>
                    <b-button squared variant="outline-danger" @click="Eliminar(data.item.id)">Eliminar</b-button>
                </b-button-group>
            </template>
        </b-table>
        <EditPorcino v-if="show" @updateInfo="updateInfo()" @CancelarEditar="OcultarEditar()" :porcinoId="porcinoId">
        </EditPorcino>
        <NewPorcinoModal v-if="!show" @nuevoPorcino="getPorcinos()"></NewPorcinoModal>
    </div>
</template>
<script>
import EditPorcino from '@/components/Porcino/EditPorcino.vue';
import { ref, onMounted } from 'vue'
import axios from 'axios'
import swal from 'sweetalert2';
import NewPorcinoModal from '@/components/Porcino/NewPorcinoModal.vue';

export default {
    components: { EditPorcino, NewPorcinoModal },
    setup() {
        const fields = [
            { key: "id", label: "ID" },
            { key: "raza", label: "Raza" },
            { key: "edad", label: "Edad" },
            { key: "peso", label: "Peso" },
            { key: "dosis", label: "Dosis", variant: "success" },
            { key: "descripcion", label: "Descripción de la alimentación", variant: "success" },
            { key: "cliente", label: "Cliente", variant: "info" },
            { key: "accion", label: "Acción" }
        ]
        let editar = ref('Editar')
        let porcinoId = ref(0)
        let show = ref(null)
        let porcinos = ref([])
        let PorcinoModal = ref(false)
        const getPorcinos = () => {
            const path = "http://127.0.0.1:8000/api/v1.0/porcinos/"
            axios.get(path).then((response) => {
                porcinos.value = response.data
                console.log(porcinos)
            }).catch((error) => {
                console.log(error)
            })
        }

        const MostarEditar = (id) => {
            porcinoId.value = id
            console.log(show.value, editar.value)
            show.value = !show.value
            editar.value = show.value ? 'Cancelar' : 'Editar'
            console.log(id)

        }


        const updateInfo = () => {
            getPorcinos()
            OcultarEditar()
        }

        const OcultarEditar = (data) => {
            show.value = data
            editar.value = 'Editar'
        }

        onMounted(() => {
            getPorcinos()
        })

        const Eliminar = (porcinoId) => {
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
                    const path = `http://localhost:8000/api/v1.0/porcinos/${porcinoId}/`
                    axios.delete(path).then((response) => {
                        console.log(response)
                        getPorcinos()
                        swal.fire({
                            title: "Eliminado",
                            text: "Se ha borrado la información de un porcino.",
                            icon: "success"
                        })
                    }).catch((error) => {
                        console.log(error)
                    })
                }
            });
        }


        const showCrearPorcinoModal = () => {
            console.log("Mostrar")
            PorcinoModal.value = !PorcinoModal.value

        }

        return {
            fields,
            porcinos,
            show,
            porcinoId,
            editar,
            MostarEditar,
            OcultarEditar,
            updateInfo,
            Eliminar,
            showCrearPorcinoModal,
            getPorcinos,
            PorcinoModal,
        }
    },
}
</script>
<style lang="">

</style>