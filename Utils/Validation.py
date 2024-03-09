class Validation:
    def param_data(
        self, data: dict, field: str, _type: str, required=True, max_len=0,
            min_len=0) -> list:
        return {
            "field": field,
            "value": data.get(field, ''),
            "type": _type,
            "required": required,
            "max_len": max_len,
            "min_len": min_len
        }

    def validate(self, list_validation: list) -> None:
        for value in list_validation:
            field = value["field"]
            val = value["value"]
            required = value["required"]
            max_len = value["max_len"]
            min_len = value["min_len"]

            if val == '' and required:
                raise AssertionError(f"El campo {field} es obligatorio")
            elif val == '' and not required:
                continue

            if type(val) != value["type"]:
                raise AssertionError(f"El tipo de dato del campo '{field}'"
                                     f"es incorrecto")

            if min_len != 0 and len(val) < min_len:
                raise AssertionError(f"el campo '{field}' no puede ser menor "
                                     f" de {min_len} caracteres")
            if max_len != 0 and len(val) > max_len:
                raise AssertionError(f"el campo '{field}' no puede ser mayor"
                                     f" de {max_len} caracteres")
