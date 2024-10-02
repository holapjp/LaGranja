import graphene
from graphene_django import DjangoObjectType
from LaGranja.models import Porcino,Alimentacion,Cliente

class PorcinoType(DjangoObjectType):
    class Meta:
        model = Porcino
        fields = ("id","raza","edad","peso","alimentacion","cliente")


class ClienteType(DjangoObjectType):
    class Meta:
        model = Cliente
        fields = ("id", "cedula", "nombres", "apellidos","direccion","telefono")  


class AlimentacionType(DjangoObjectType):
    class Meta:
        model = Alimentacion
        fields = ("id", "dosis", "descripcion")


class createPorcinoMutation(graphene.Mutation):
    class Meta:
        model = Porcino
    
    class Arguments:
        raza = graphene.String()
        edad = graphene.Int()
        peso =  graphene.Float()
        alimentacion = graphene.ID()
        cliente = graphene.ID()
        
    porcino = graphene.Field(PorcinoType)
    
    def mutate(self, info, raza, edad, peso, alimentacion, cliente):
        porcino = Porcino(raza=raza, edad=edad, peso=peso, alimentacion_id=alimentacion, cliente_id=cliente)
        porcino.save()
        return createPorcinoMutation(porcino=porcino)
        




class createClienteMutation (graphene.Mutation):
    class Meta: 
        model = Cliente
        
    class Arguments:
        cedula = graphene.String()
        nombres = graphene.String()
        apellidos = graphene.String()
        direccion = graphene.String()
        telefono = graphene.String()
        
    cliente = graphene.Field(ClienteType)
    
    def mutate(self, info, cedula, nombres, apellidos, direccion, telefono):
        cliente =  Cliente(cedula=cedula,nombres=nombres,apellidos=apellidos, direccion=direccion, telefono=telefono)
        cliente.save()
        return createClienteMutation(cliente=cliente)
        



class createAlimentacionMutation(graphene.Mutation):
    class Meta:
        model = Alimentacion
    
    class Arguments():
        dosis = graphene.String()
        descripcion = graphene.String()
    
    alimentacion = graphene.Field(AlimentacionType)
    
    def mutate(self,info, dosis, descripcion):
        alimentacion = Alimentacion(dosis=dosis, descripcion=descripcion)
        alimentacion.save()
        return createAlimentacionMutation(alimentacion=alimentacion)



class deleteAlimentacionMutation(graphene.Mutation):
    class Meta:
        model = Alimentacion
    
    
    class Arguments:
        id = graphene.ID(required=True)
    
    message = graphene.String()
    
    def mutate(self, info, id):
        alimentacion = Alimentacion.objects.get(pk=id)
        alimentacion.delete()
        return deleteAlimentacionMutation(message=f"Alimentacion con id {id} eliminada exitosamente")
    
    
    
    
    
class deleteClienteMutation(graphene.Mutation):
    class Meta:
        model = Cliente
        
    class Arguments:
        id = graphene.ID(required=True)
        
    message = graphene.String()
        
    def mutate(self, info, id):
        cliente = Cliente.objects.get(pk=id)
        cliente.delete()
        return deleteClienteMutation(message=f"Cliente con id {id} eliminado exitosamente")



class deletePorcinoMutation(graphene.Mutation):
    class Meta:
        model = Porcino
        
    class Arguments:
        id = graphene.ID(required=True)
        
    message = graphene.String()
    
    def mutate(self, info, id):
        porcino = Porcino.objects.get(pk=id)
        porcino.delete()
        return deletePorcinoMutation(message=f"Porcino con id {id} eliminado exitosamente")
    




class updateAlimentacionMutation(graphene.Mutation):
    class Meta:
        model = Alimentacion
    
    class Arguments:
        id = graphene.ID(required=True)
        dosis = graphene.String()
        descripcion = graphene.String()
    
    alimentacion = graphene.Field(AlimentacionType)
    
    def mutate(self, info, id, dosis, descripcion):
        alimentacion = Alimentacion.objects.get(pk=id)
        alimentacion.dosis = dosis
        alimentacion.descripcion = descripcion
        alimentacion.save()
        return updateAlimentacionMutation(alimentacion=alimentacion)
        


class updateClienteMutation(graphene.Mutation):
    class Meta:
        model = Cliente
        
    class Arguments:
        id = graphene.ID(required=True)
        cedula = graphene.String()
        nombres = graphene.String()
        apellidos = graphene.String()
        direccion = graphene.String()
        telefono = graphene.String()
        
    cliente = graphene.Field(ClienteType)
    
    def mutate(self, info, id, cedula, nombres, apellidos, direccion, telefono):
        cliente = Cliente.objects.get(pk=id)
        cliente.cedula = cedula
        cliente.nombres = nombres
        cliente.apellidos = apellidos
        cliente.direccion = direccion
        cliente.telefono = telefono
        cliente.save()
        return updateClienteMutation(cliente=cliente)
    


class updatePorcinoMutation(graphene.Mutation):
    class Meta:
        model = Porcino
    
    class Arguments:
        id = graphene.ID(required=True)
        raza = graphene.String(required=False)
        edad = graphene.Int(required=False)
        peso = graphene.Float(required=False)
        alimentacion = graphene.ID(required=False)
        cliente = graphene.ID(required=False)
    
    porcino = graphene.Field(PorcinoType)
    
    def mutate(self, info, id, raza=None, edad=None, peso=None, alimentacion=None, cliente=None):
        porcino = Porcino.objects.get(pk=id)
        
        if raza:
            porcino.raza = raza
        if edad:
            porcino.edad = edad
        if peso:
            porcino.peso = peso
        if alimentacion:
            porcino.alimentacion_id = alimentacion
        if cliente:   
            porcino.cliente_id = cliente
        
        porcino.save()
        return updatePorcinoMutation(porcino=porcino)



class Query(graphene.ObjectType):

    porcinos = graphene.List(PorcinoType)
    porcino =  graphene.Field(PorcinoType, id= graphene.ID())


    clientes =  graphene.List(ClienteType)
    cliente = graphene.Field(ClienteType,id=graphene.ID())

    alimentaciones = graphene.List(AlimentacionType)
    alimentacion = graphene.Field(AlimentacionType,id=graphene.ID())


    def resolve_alimentaciones(self, info):
        return Alimentacion.objects.all()
    


    # Resolver
    def resolve_clientes(self, info):
        return Cliente.objects.all()
    
    def resolve_porcinos(self, info):
        return Porcino.objects.all()
    
    def resolve_porcino(self, info, id):
        return Porcino.objects.get(pk=id)
    
    def resolve_cliente(self, info, id):
        return Cliente.objects.get(pk=id)
    
    def resolve_alimentacion(self, info, id):
        return Alimentacion.objects.get(pk=id)



class Mutation(graphene.ObjectType):
    #creaciones
    create_cliente = createClienteMutation.Field()
    create_porcino = createPorcinoMutation.Field()
    create_alimentacion = createAlimentacionMutation.Field()
    
    
    #eliminaciones
    delete_alimentacion = deleteAlimentacionMutation.Field()
    delete_cliente = deleteClienteMutation.Field()
    delete_porcino = deletePorcinoMutation.Field()
    
    #actualizaciones
    update_alimentacion = updateAlimentacionMutation.Field()
    update_cliente = updateClienteMutation.Field()
    update_porcino = updatePorcinoMutation.Field()





schema = graphene.Schema(query=Query,mutation=Mutation)