<template>
    <div class="container">
        <h2>Listado de alimentaciones:</h2>
        <b-table :items="alimentaciones" :fields="fields" stripped hover>
            <template #cell(accion)="data">
                <b-button-group>
                    <b-button squared variant="outline-secondary" @click="MostarEditar(data.item.id)">{{ editar
                        }}</b-button>
                    <b-button squared variant="outline-danger" @click="Eliminar(data.item.id)">Eliminar</b-button>
                </b-button-group>
            </template>
        </b-table>
        <editAlimentacion v-if="show" @updateInfo="updateInfo()" @CancelarEditar="OcultarEditar()" :alimentoId="alimentoId">
        </editAlimentacion>
        <newAlimentacion v-if="!show" @nuevoAlimento="getAlimentaciones()"></newAlimentacion>
    </div>
</template>
<script>
import editAlimentacion from '@/components/alimentaciones/EditAlimento.vue';
import { ref, onMounted } from 'vue'
import axios from 'axios'
import swal from 'sweetalert2';
import newAlimentacion from '@/components/alimentaciones/NewAlimento.vue';
import { usePorcinosAPI } from '@/composables/usePorcinosAPI';

export default {
    components: { editAlimentacion, newAlimentacion },
    setup() {
        const { getAlimentaciones, alimentaciones } = usePorcinosAPI()
        const fields = [
            { key: "id", label: "ID" },
            { key: "dosis", label: "Dosis", variant: "success" },
            { key: "descripcion", label: "Descripción de la alimentación", variant: "success" },
            { key: "accion", label: "Acciones" },
        ]
        let editar = ref('Editar')
        let alimentoId = ref(0)
        let show = ref(null)
        let clienteModal = ref(false)

        const MostarEditar = (id) => {
            alimentoId.value = id
            console.log(show.value, editar.value)
            show.value = !show.value
            editar.value = show.value ? 'Cancelar' : 'Editar'
            console.log(id)

        }


        const updateInfo = () => {
            getAlimentaciones()
            OcultarEditar()
        }

        const OcultarEditar = (data) => {
            show.value = data
            editar.value = 'Editar'
        }

        onMounted(() => {
            getAlimentaciones()
        })

        const Eliminar = (alimentoId) => {
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
                    const path = `http://localhost:8000/api/v1.0/alimentaciones/${alimentoId}/`
                    axios.delete(path).then((response) => {
                        console.log(response)
                        getAlimentaciones()
                        swal.fire({
                            title: "Eliminado",
                            text: "Se ha borrado la alimentación correctamente.",
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
            clienteModal.value = !clienteModal.value

        }

        return {
            fields,
            alimentaciones,
            show,
            alimentoId,
            editar,
            MostarEditar,
            OcultarEditar,
            updateInfo,
            Eliminar,
            showCrearPorcinoModal,
            getAlimentaciones,
            clienteModal,
        }
    },
}
</script>
<style lang="">

</style>