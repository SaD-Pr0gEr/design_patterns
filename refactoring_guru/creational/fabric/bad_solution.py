from dataclasses import dataclass


def get_some_truck_from_db() -> "Truck":
    return Truck(1432432, 'Someone')


def get_some_ship_from_db() -> "Ship":
    return Ship(32131231, 'Some pirate')


@dataclass
class Truck:
    number: int
    driver: str

    def deliver(self, address: str) -> str:
        return (
            f'Груз доставляется по суши(траком) до адреса: {address}'
            f'\nНомер трака: {self.number}'
        )

    def __str__(self):
        return str(self.number)


@dataclass
class Ship:
    number: int
    driver: str

    def deliver(self, address: str) -> str:
        return (
            f'Груз доставляется по море(судном) до адреса: {address}'
            f'\nНомер судна: {self.number}'
        )

    def __str__(self):
        return str(self.number)


@dataclass
class Logistics:

    def get_transport(self, sea: bool) -> Truck | Ship:
        # если будут больше типов транспорта, то проверки и параметры
        # только увеличатся
        if not sea:
            transport = get_some_truck_from_db()
        else:
            transport = get_some_ship_from_db()
        return transport

    def plan_delivery(self, address: str, sea: bool = False) -> str:
        print(
            f'Организуется логистика до адреса {address} '
        )
        transport = self.get_transport(sea)
        print(transport.deliver(address))
        return address


logistics = Logistics()
logistics.plan_delivery('somewhere')
