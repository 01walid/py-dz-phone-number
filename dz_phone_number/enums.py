from enum import IntFlag, unique, Enum
from typing import List


class BaseEnum(IntFlag):
    @classmethod
    def all(cls) -> List[int]:
        return list(map(int, cls.__members__.values()))

    def is_of_equal_value(self, name):
        """
        Some enums have different names but the same value. This compares against
        their value.
        e.g. BATNA and BISKRA are both 33. So `BATNA.is_of_equal_value(BISKRA)` is `True`.
        """
        if self.name == name:
            return True

        list_ = [
            key
            for key, number in self.__class__.__members__.items()
            if number == self.value
        ]

        return name in list_

    def describe(self) -> str:
        """
        Based on the value of this enum. Get any other member with the same
        value. 
        e.g. if self.value is `33` then this returns "class_name: BATNA|BISKRA"
        """
        l = [
            key
            for key, number in self.__class__.__members__.items()
            if number == self.value
        ]
        represents = "|".join(l)
        return f"{self.__class__.__name__}: {represents}"


@unique
class MobileOperator(BaseEnum):

    OOREDOO = 5
    MOBILIS = 6
    DJEZZY = 7


class LandlinePrefix(BaseEnum):
    ADRAR = 49
    CHLEF = 27
    LAGHOUAT = 29
    OUM_EL_BOUAGHI = 32
    BATNA = 33
    BEJAIA = 34
    BISKRA = 33
    BECHAR = 49
    BLIDA = 25
    BOUIRA = 26
    TAMANRASSET = 29
    TEBESSA = 37
    TLEMCEN = 43
    TIARET = 46
    TIZI_OUZOU = 26
    ALGIERS = 21
    ALGIERS_2 = 23
    DJELFA = 27
    JIJEL = 34
    SETIF = 36
    SAIDA = 48
    SKIKDA = 38
    SIDI_BEL_ABBES = 48
    ANNABA = 38
    GUELMA = 37
    CONSTANTINE = 31
    MEDEA = 25
    MOSTAGANEM = 45
    MSILA = 35
    MASCARA = 45
    OUARGLA = 29
    ORAN = 41
    EL_BAYADH = 49
    ILIZI = 29
    BORDJ_BOU_ARRERIDJ = 35
    BOUMERDES = 24
    EL_TAREF = 38
    TINDOUF = 49
    TISSEMSILT = 46
    EL_OUED = 32
    KHENCHELA = 32
    SOUK_AHRAS = 37
    TIPAZA = 24
    MILA = 31
    AIN_DEFLA = 27
    NAAMA = 49
    AIN_TEMOUCHENT = 43
    GHARDAIA = 29
    RELIZANE = 46


class CountryCode(Enum):
    LOCAL = "0"
    GLOBAL_00 = "00213"
    GLOBAL_PLUS = "+213"
