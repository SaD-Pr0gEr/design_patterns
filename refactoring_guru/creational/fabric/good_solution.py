from abc import ABC, abstractmethod
from dataclasses import dataclass


def get_some_truck_from_db() -> "Truck":
    return Truck(1432432, Driver('someone', 'alex', 20))


def get_some_ship_from_db() -> "Ship":
    return Ship(32131231, Driver('pirate', 'alex sparrow', 30))


@dataclass
class Driver:
    name: str
    surname: str
    age: int


@dataclass
class Transport:
    number: int
    driver: Driver

    def deliver(self, address: str) -> str:
        return (
            f'Груз доставляется в адрес: {address}\n'
            f'Номер транспорта: {self.number}\n'
            f'Водитель: {self.driver.name}'
        )


@dataclass
class Truck(Transport):
    def deliver(self, address: str) -> str:
        txt = super().deliver(address)
        return txt + '\nГруз доставляется по суше на траке'


@dataclass
class Ship(Transport):
    def deliver(self, address: str) -> str:
        txt = super().deliver(address)
        return txt + '\nГруз доставляется по морю на корабле'


class Logistics(ABC):

    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self, address: str) -> None:
        print(f'Организуется доставка до {address}')
        transport = self.create_transport()
        print(transport.deliver(address))


class RoadLogistics(Logistics):

    def create_transport(self) -> Truck:
        return get_some_truck_from_db()


class SeaLogistics(Logistics):

    def create_transport(self) -> Ship:
        return get_some_ship_from_db()


sea_logistics = SeaLogistics()
road_logistics = RoadLogistics()
sea_logistics.plan_delivery('Nowhere')
print('-' * 50)
road_logistics.plan_delivery('Knowhere')
