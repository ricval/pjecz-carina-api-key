"""
Exh Exhortos Partes, modelos
"""

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class ExhExhortoParte(Base, UniversalMixin):
    """ExhExhortoParte"""

    GENEROS = {
        "M": "MASCULINO",
        "F": "FEMENINO",
    }

    # Nombre de la tabla
    __tablename__ = "exh_exhortos_partes"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    exh_exhorto_id = Column(Integer, ForeignKey("exh_exhortos.id"), index=True, nullable=False)
    exh_exhorto = relationship("ExhExhorto", back_populates="exh_exhortos_partes")

    # Nombre de la parte, en el caso de persona moral, solo en nombre de la empresa o razón social.
    nombre = Column(String(256), nullable=False)

    # Apellido paterno de la parte. Solo cuando no sea persona moral.
    apellido_paterno = Column(String(256))

    # Apellido materno de la parte, si es que aplica para la persona. Solo cuando no sea persona moral.
    apellido_materno = Column(String(256))

    # 'M' = Masculino,
    # 'F' = Femenino.
    # Solo cuando aplique y se quiera especificar (que se tenga el dato). NO aplica para persona moral.
    genero = Column(Enum(*GENEROS, name="exh_exhortos_partes_generos", native_enum=False), nullable=True)

    # Valor que indica si la parte es una persona moral.
    es_persona_moral = Column(Boolean, nullable=False)

    # Indica el tipo de parte:
    # 1 = Actor, Promovente, Ofendido;
    # 2 = Demandado, Inculpado, Imputado;
    # 0 = No definido o se especifica en tipoParteNombre
    tipo_parte = Column(Integer, nullable=False, default=0)

    # Aquí se puede especificar el nombre del tipo de parte.
    tipo_parte_nombre = Column(String(256))

    @property
    def apellidoPaterno(self):
        """Apellido paterno"""
        return self.apellido_paterno

    @property
    def apellidoMaterno(self):
        """Apellido materno"""
        return self.apellido_materno

    @property
    def esPersonaMoral(self):
        """Es persona moral"""
        return self.es_persona_moral

    @property
    def tipoParte(self):
        """Tipo de parte"""
        return self.tipo_parte

    @property
    def tipoParteNombre(self):
        """Nombre del tipo de parte"""
        return self.tipo_parte_nombre

    @property
    def __repr__(self):
        """Representación"""
        return f"<ExhExhortoParte {self.id}>"
