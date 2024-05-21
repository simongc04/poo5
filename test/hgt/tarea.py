class Tarea:
    def __init__(self, id:int, tarea:str, estado:bool) -> None:
        self.id     = id
        self.tarea  = tarea
        self.estado = estado

    #Métodos CRUD
    def read(self):
     return (f"{self.id, self.tarea, self.estado}")
     
    def update(self, tareaNueva,IDNuevo,EstadoNuevo):
        self.tarea = tareaNueva
        self.estado = EstadoNuevo
        self.id = IDNuevo

    def delete(self):
        self.tarea = None
        self.id = None
        self.estado = None