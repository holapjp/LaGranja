<template lang="">
  <b-button variant="outline-primary" @click="showCrearAlimento()"
    >Agregar nueva alimentación</b-button
  >
  <b-modal
    v-model="alimentoModal"
    title="Crear nueva alimentación:"
    hide-footer
  >
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
        <label for="descripcion" class="col-3 col-form-label"
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
          <b-button type="submit" variant="outline-primary" squared
            >Confirmar cambios</b-button
          >
          <b-button
            variant="outline-secondary"
            squared
            @click="showCrearAlimento()"
            >Cancelar</b-button
          >
        </b-button-group>
      </div>
    </form>
  </b-modal>
</template>
<script>
import { usePorcinosAPI } from "@/composables/usePorcinosAPI";
import axios from "axios";
import Swal from "sweetalert2";
import { ref, getCurrentInstance } from "vue";
export default {
  emits: ["nuevoAlimento"],
  setup() {
    const { emit } = getCurrentInstance();
    let alimentoModal = ref(false);

    let form = ref({
      dosis: "",
      descripcion: "",
    });

    const onSubmit = () => {
      const path = "http://localhost:8000/api/v1.0/alimentaciones/";
      axios
        .post(path, {
          dosis: form.value.dosis,
          descripcion: form.value.descripcion
        })
        .then((response) => {
          alimentoModal.value = false;
          form.value = {
            dosis: "",
            descripcion: "",
          };
          Swal.fire({
            title: "Alimentación creada",
            icon: "success",
          });
          emit("nuevoAlimento");
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const showCrearAlimento = () => {
      console.log("Mostrar");
      alimentoModal.value = !alimentoModal.value;
    };

    return {
      form,
      alimentoModal,
      showCrearAlimento,
      emit,
      onSubmit,
    };
  },
};
</script>
