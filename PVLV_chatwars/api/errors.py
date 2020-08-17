class GamesErrors:

    @staticmethod
    def build_error(code: int, message: str):
        return {
            'errors:': [
                {
                    "code": code,
                    'description': message
                },
            ]
        }


class BillErrors:
    NO_MONEY = GamesErrors.build_error(100, 'no enough money in user bill')


class PlantErrors:
    NOTHING_PLANTED = GamesErrors.build_error(200, 'nothing planted')
    ALREADY_PLANTED = GamesErrors.build_error(201, 'already planted')
    REPLANT_TIMEOUT = GamesErrors.build_error(202, 'wait 10 min before replant')
