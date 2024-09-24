<template lang="">
  <b-button variant="outline-primary" @click="showCrearCliente()"
    >Agregar nuevo cliente</b-button
  >
  <b-modal v-model="ClienteModal" title="Crear nuevo porcino:" hide-footer>
    <form @submit.prevent="onSubmit()">
      <div class="form-group row">
        <label for="cedula" class="col-2 col-form-label">Cédula:</label>
        <div class="col-sm-8">
          <input
            type="text"
            name="cedula"
            class="form-control"
            v-model.trim="form.cedula"
          />
        </div>
      </div>
      <div class="form-group row">
        <label for="nombres" class="col-2 col-form-label">Nombres:</label>
        <div class="col-sm-8">
          <input
            type="text"
            name="nombres"
            class="form-control"
            v-model.trim="form.nombres"
          />
        </div>
      </div>
      <div class="form-group row">
        <label for="apellidos" class="col-2 col-form-label">Apellidos:</label>
        <div class="col-sm-8">
          <input
            type="text"
            name="apellidos"
            class="form-control"
            v-model.trim="form.apellidos"
          />
        </div>
      </div>
      <div class="form-group row">
        <label for="direccion" class="col-2 col-form-label">Dirección:</label>
        <div class="col-sm-8">
          <input
            type="text"
            name="direccion"
            class="form-control"
            v-model.trim="form.direccion"
          />
        </div>
      </div>
      <div class="form-group row">
        <label for="telefono" class="col-2 col-form-label">Teléfono:</label>
        <div class="col-sm-8">
          <input
            type="text"
            name="telefono"
            class="form-control"
            v-model.trim="form.telefono"
          />
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
            @click="showCrearCliente()"
            >Cancelar</b-button
          >
        </b-button-group>
      </div>
    </form>
  </b-modal>
</template>
<script>
import axios from "axios";
import Swal from "sweetalert2";
import { ref, getCurrentInstance } from "vue";
export default {
  emits: ["nuevoCliente"],
  setup() {
    const { emit } = getCurrentInstance();
    let ClienteModal = ref(false);

    let form = ref({
      cedula: "",
      nombres: "",
      apellidos: "",
      direccion: "",
      telefono: "",
    });

    const onSubmit = () => {
      const path = "http://localhost:8000/api/v1.0/clientes/";
      axios
        .post(path, {
          cedula: form.value.cedula,
          nombres: form.value.nombres,
          apellidos: form.value.apellidos,
          direccion: form.value.direccion,
          telefono: form.value.telefono,
        })
        .then((response) => {
          ClienteModal.value = false;
          form.value = {
            cedula: "",
            nombres: "",
            apellidos: "",
            direccion: "",
            telefono: "",
          };
          Swal.fire({
            title: "Cliente creado",
            icon: "success",
          });
          emit("nuevoCliente");
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const showCrearCliente = () => {
      console.log("Mostrar");
      ClienteModal.value = !ClienteModal.value;
    };

    return {
      form,
      ClienteModal,
      showCrearCliente,
      emit,
      onSubmit,
    };
  },
};
</script>
