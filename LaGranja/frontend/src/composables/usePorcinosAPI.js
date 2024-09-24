import axios from "axios"
import { ref } from "vue"

export function usePorcinosAPI() {
    let clientes = ref({})
    let alimentaciones = ref({})
    
    const getClientes = ()=>{
        const path = "http://localhost:8000/api/v1.0/clientes/"
        axios.get(path).then((response) => {
            clientes.value = response.data
        }).catch((error) => {
            console.log(error)
        })
    }

    const getAlimentaciones = ()=>{
        const path = "http://localhost:8000/api/v1.0/alimentaciones/"
        axios.get(path).then((response) => {
            alimentaciones.value = response.data
        }).catch((error) => {
            console.log(error)
        })
    }

    return {
        getClientes,
        getAlimentaciones,
        clientes,
        alimentaciones,

    }

}


