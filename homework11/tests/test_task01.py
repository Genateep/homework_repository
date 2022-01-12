from homework11.task01 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


class ColorsEnumNoMeta:
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnumNoMeta:
    __keys = ("XL", "L", "M", "S", "XS")


def test_creation_attr_from_keys():
    assert not hasattr(SizesEnumNoMeta, "XL")
    assert not hasattr(ColorsEnumNoMeta, "RED")

    assert hasattr(SizesEnum, "XL")
    assert SizesEnum.XL == "XL"

    assert hasattr(ColorsEnum, "RED")
    assert ColorsEnum.RED == "RED"
