class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = [0, 0]) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        for i in self.coords:
            self.coords[i] + step

    def go_back(self, step: int = 1) -> None:
        for i in self.coords:
            self.coords[-i] + step

    def go_right(self, step: int = 1) -> None:
        for i in self.coords:
            self.coords[i] + step

    def go_left(self, step: int = 1) -> None:
        for i in self.coords:
            self.coords[-i] + step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self, name: str, weight: int, coords: list = [0, 0, 0]
    ) -> None:
        super().__init__(name, weight)
        self.coords = coords

    def go_up(self) -> None:
        for i in self.coords:
            self.coords[i] + 1

    def go_down(self) -> None:
        for i in self.coords:
            self.coords[i] - 1


class DeliveryDrone(FlyingRobot):
    def __init__(
            self, name: str, weight: int, max_load_weight: int,
            current_load: Cargo = None, coords: list = [0, 0, 0]
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
        else:
            pass

    def unhook_load(self) -> None:
        self.current_load = None
