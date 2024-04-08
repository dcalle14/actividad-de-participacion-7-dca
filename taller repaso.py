from dataclasses import dataclass
from typing import List

@dataclass(eq=True, frozen=True)
class Elemento:
    nombre: str

@dataclass
class Conjunto:
    elementos: List[Elemento] = []
    nombre: str = ""
    __contador: int = 0

    def __post_init__(self):
        Conjunto.__contador += 1
        self.__id = Conjunto.__contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elem: Elemento) -> bool:
        return any(e.nombre == elem.nombre for e in self.elementos)

    def agregar_elemento(self, elem: Elemento):
        if not self.contiene(elem):
            self.elementos.append(elem)

    def __add__(self, otro):
        if not isinstance(otro, Conjunto):
            raise ValueError("El objeto a unir debe ser un Conjunto")
        nuevo_conjunto = Conjunto(self.elementos.copy(), self.nombre)
        for elem in otro.elementos:
            nuevo_conjunto.agregar_elemento(elem)
        return nuevo_conjunto

    def unir(self, otro):
        return self + otro

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        if not isinstance(conjunto1, Conjunto) or not isinstance(conjunto2, Conjunto):
            raise ValueError("Los objetos a intersectar deben ser de tipo Conjunto")
        elementos_interseccion = [elem for elem in conjunto1.elementos if conjunto2.contiene(elem)]
        nombre_interseccion = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        return Conjunto(elementos_interseccion, nombre_interseccion)

    def __str__(self):
        elementos_str = ", ".join(elem.nombre for elem in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"
