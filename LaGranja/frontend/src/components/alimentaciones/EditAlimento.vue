<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h3>Editar información de alimetación:</h3>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <form @submit.prevent="onSubmit()">
              <div class="form-group row">
                <label for="raza" class="col-2 col-form-label">Dosis:</label>
                <div class="col-sm-8">
                  <input
                    type="text"
                    name="Dosis"
                    class="form-control"
                    v-model.trim="form.dosis"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label for="descripcion" class="col-2 col-form-label"
                  >Descripción:</label
                >
                <div class="col-sm-8">
                  <textarea
                    name="descripcion"
                    class="form-control"
                    cols="50"
                    row="100"
                    v-model.trim="form.descripcion"
                  >
          Descripción de la alimentación</textarea
                  >
                </div>
              </div>
              <div class="rows">
                <b-button-group>
                  <b-button type="submit" variant="outline-secondary" squared
                    >Confirmar cambios</b-button
                  >
                  <b-button
                    variant="outline-danger"
                    squared
                    @click="cancelarEditar()"
                    >Cancelar</b-button
                  >
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
import axios from "axios";
import { onMounted, ref, getCurrentInstance } from "vue";
import swal from "sweetalert2";
import { usePorcinosAPI } from "@/composables/usePorcinosAPI.js";
export default {
  props: {
    alimentoId: {
      type: Number,
      required: true,
    },
  },
  setup(props) {
    // const route = useRoute();
    const { emit } = getCurrentInstance();
    const alimentoId = props.alimentoId;

    let form = ref({
      dosis: "",
      descripcion: "",
    });

    const cancelarEditar = () => {
      emit("CancelarEditar", false);
    };

    const onSubmit = () => {
      console.log("envio del formulario evitado");
      console.log(form.value);
      const path = `http://localhost:8000/api/v1.0/alimentaciones/${alimentoId}/`;
      axios
        .put(path, {
          dosis: form.value.dosis,
          descripcion: form.value.descripcion
        })
        .then((response) => {
          swal.fire("Alimentación actualizada existosamente!", "", "success");
          emit("updateInfo");
        })
        .catch((error) => {
          swal.fire("Oops...", "Algo salió mal", "error");
          console.log(error);
        });
    };

    const getAlimentaciones = () => {
      const path = `http://127.0.0.1:8000/api/v1.0/alimentaciones/${alimentoId}/`;

      axios
        .get(path)
        .then((response) => {
          form.value.dosis = response.data.dosis;
          form.value.descripcion = response.data.descripcion;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    onMounted(() => {
        getAlimentaciones();
    });

    return {
      alimentoId,
      form,
      getAlimentaciones,
      cancelarEditar,
      onSubmit,
    };
  },
};
</script>
<style lang=""></style>
