from json import dumps as json_dumbs, loads as json_loads
from Utils.JwtToken import JWTtoken
from Utils.AuthorizerUser import AuthorizerUser


def json_response(statusCode, message, data=[]):
    body = {
        "statusCode": statusCode,
        "msg": message
    }

    if data:
        body["data"] = data

    response = {
        "statusCode": statusCode,
        "body": json_dumbs(body)

    }

    return response


def lamda_response(function):
    def validation(event, context):
        statusCode = 200
        msg = "Ok"
        data = []

        try:
            data = function(event, context)
            if data and type(data) is dict:
                if "statusCode" in data:
                    statusCode = data["statusCode"]

                    if "msg" in data:
                        msg = data["msg"]

                    if "data" in data:
                        data = data["data"]

                    else:
                        data = []
        except Exception as err:
            print(str(err))
            statusCode = 400
            msg = str(err)

        return json_response(statusCode, msg, data)
    return validation


def get_event_data(event: dict) -> dict:

    data = {}

    requestContext = event["requestContext"]
    http = requestContext["http"]

    if event["body"]:
        data = json_loads(event["body"])

    if event["queryStringParameters"]:
        data = event["queryStringParameters"]

    if "access_data" in event:
        data = {
            **event["access_data"],
            **data
        }
    # Get api data
    data["method"] = http["method"]
    data["path"] = http["path"]

    return data


def authorizer(function):

    def validation(event, context):

        statusCode = 200
        msg = "Ok"
        data = []

        try:
            # Validamos el token
            headers = event["headers"]
            print(f"headers: {str(headers)}")
            requestContext = event["requestContext"]
            http = requestContext["http"]

            # Capturamos el "method" y "path"
            method = http["method"]
            path = http["path"]

            # Get id token
            if "authorization" not in headers:
                raise AssertionError("No se tiene el token de acceso.")

            authorization = headers["authorization"]
            token_data = authorization.split("Bearer ")

            if len(token_data) < 1:
                raise AssertionError("No se tiene acceso al token")

            token_id = token_data[1]
            print(f"token_id :{str(token_id)}")

            # Instanciamos la clase JWTtoken
            jwt_token = JWTtoken()
            # Una vez capturado el token, usamos el metodo decode de la clase
            # JWTtoken
            data_token = jwt_token.decode(token_id)
            data_token.pop("exp")

            # Instanciamos la clase "AuthorizerUser"
            auth_user = AuthorizerUser()
            # Creamos una variable result la cual utilizara el metodo
            # "validate_auth" para validar los permisos del usuario
            result = auth_user.validate_auth({
                "user_id": data_token["user_id"],
                "path": path,
                "method": method
            })
            print(f"result: {result}")

            event["access_data"] = data_token

            # funcionamiento de la api
            data = function(event, context)

            if type(data) is dict:

                if "statusCode" in data:
                    statusCode = data["statusCode"]

                    if "msg" in data:
                        msg = data["msg"]

                    if "data" in data:
                        data = data["data"]
                    else:
                        data = []

        except Exception as err:
            print(str(err))
            statusCode = 400
            msg = str(err)

        return json_response(statusCode, msg, data)

    return validation
