<template lang="">
  <b-button variant="outline-primary" @click="showCrearPorcinoModal()"
    >Agregar nuevo porcino</b-button
  >
  <b-modal v-model="PorcinoModal" title="Crear nuevo porcino:" hide-footer>
    <form @submit.prevent="onSubmit()">
      <div class="form-group row">
        <label for="raza" class="col-2 col-form-label">Raza:</label>
        <div class="col-sm-8">
          <input
            type="text"
            placeholder="Example: Yorkshire"
            name="raza"
            class="form-control"
            v-model.trim="form.raza"
          />
        </div>
      </div>
      <div class="form-group row">
        <label for="edad" class="col-2 col-form-label">Edad:</label>
        <div class="col-sm-8">
          <input
            type="number"
            placeholder="0"
            name="edad"
            class="form-control"
            v-model.trim="form.edad"
          />
        </div>
      </div>
      <div class="form-group row">
        <label for="peso" class="col-2 col-form-label">Peso:</label>
        <div class="col-sm-8">
          <input
            type="number"
            placeholder="0"
            name="peso"
            class="form-control"
            v-model.trim="form.peso"
          />
        </div>
      </div>
      <div class="form-group row">
        <label for="cliente" class="col-2 col-form-label">Cliente:</label>
        <div class="col-sm-8">
          <select id="cliente" class="form-control" v-model="form.cliente">
            <option v-for="item in clientes" :key="item.id" :value="item.id">
              {{ item.nombres }} {{ item.apellidos }}
            </option>
          </select>
        </div>
      </div>
      <div class="form-group row">
        <label for="alimentacion" class="col-3 col-form-label"
          >Alimentación:
        </label>
        <div class="col-sm-8">
          <select v-model="form.alimentacion" id="id" class="form-control">
            <option
              v-for="item in alimentaciones"
              :key="item.id"
              :value="item.id"
            >
              {{ item.dosis }}
            </option>
          </select>
        </div>
      </div>
      <div class="rows">
        <b-button-group>
          <b-button type="submit" variant="outline-primary" squared
            >Confirmar cambios</b-button
          >
          <b-button variant="outline-secondary" squared @click="showCrearPorcinoModal()"
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
import { ref, onMounted, getCurrentInstance } from "vue";
export default {
  emits: ['nuevoPorcino'],
  setup() {
    let { getClientes, getAlimentaciones, clientes, alimentaciones } =
      usePorcinosAPI();
    const { emit  } = getCurrentInstance()
    let PorcinoModal = ref(false)

    let form = ref({
      raza: "",
      edad: 0,
      peso: 0,
      cliente: 0,
      alimentacion: 0,
    });

    const onSubmit = () => {
      const path = "http://localhost:8000/api/v1.0/porcinos/";
      axios
        .post(path, {
          raza: form.value.raza,
          edad: form.value.edad,
          peso: form.value.peso,
          clienteId: form.value.cliente,
          alimentacionId: form.value.alimentacion,
        })
        .then((response) => {
          PorcinoModal.value = false;
          form.value = {
            raza: "",
            edad: 0,
            peso: 0,
            cliente: 0,
            alimentacion: 0,
          }
          Swal.fire({
            title: "Porcino creado",
            icon: "success",
          });
          emit("nuevoPorcino")
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const showCrearPorcinoModal = () => {
      console.log("Mostrar");
      PorcinoModal.value = !PorcinoModal.value;
    };

    onMounted(() => {
      getAlimentaciones(), getClientes();
    });

    return {
      form,
      PorcinoModal,
      showCrearPorcinoModal,
      getAlimentaciones,
      getClientes,
      alimentaciones,
      clientes,
      emit,
      onSubmit,
    };
  },
};
</script>
