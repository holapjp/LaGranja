import { createRouter, createWebHistory } from 'vue-router'
import ListPorcino from '@/components/Porcino/ListPorcino.vue'
import EditPorcino from '@/components/Porcino/EditPorcino.vue'
import Clientes from '@/components/clientes/ListCliente.vue'
import Alimentaciones from '@/components/alimentaciones/ListAlimentaciones.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ListPorcinos',
      component: ListPorcino
    },
    {
      path: '/porcinos/:porcinoId/edit',
      name: 'EditPorcino',
      component: EditPorcino
    },
    {
      path: '/clientes',
      name: 'Clientes',
      component: Clientes
    },
    {
      path: '/alimentaciones',
      name: 'Alimentaciones',
      component: Alimentaciones
    },
  ],
  mode: 'history'
})

export default router
