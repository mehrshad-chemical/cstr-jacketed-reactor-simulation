class BaseVessel:
    def __init__(self, vessel_id: str, capacity: float, current_volume: float = 0.0, temperature: float = 25.0):
        self.vessel_id = vessel_id
        self.capacity = capacity
        self.current_volume = current_volume
        self.temperature = temperature

    def add_material(self, volume: float, temp: float) -> bool:
        if self.current_volume + volume > self.capacity:
            print(f"Error: Not enough space in {self.vessel_id}!")
            return False
        
    
        new_total_volume = self.current_volume + volume
        if new_total_volume > 0:
            self.temperature = ((self.current_volume * self.temperature) + (volume * temp)) / new_total_volume
        
        self.current_volume += volume
        return True 

    def get_status(self) -> dict:
        percent_full = (self.current_volume / self.capacity) if self.capacity > 0 else 0
        return {
            "vessel_id": self.vessel_id,
            "volume": self.current_volume,
            "temperature": self.temperature,
            "percent_full": percent_full 
        }

class CSTRJacketedReactor(BaseVessel):
    def __init__(self, vessel_id, capacity, current_volume=0.0, temperature=25.0, jacket_temp=25.0, agitator_on=False, heat_transfer_coeff=0.5):
        super().__init__(vessel_id, capacity, current_volume, temperature)
        self.jacket_temp = jacket_temp
        self.agitator_on = agitator_on
        self.heat_transfer_coeff = heat_transfer_coeff

    def toggle_agitator(self) -> bool:
        self.agitator_on = not self.agitator_on # این خط جادویی وضعیت رو عوض می‌کنه
        return self.agitator_on

    def set_jacket_temperature(self, target_temp: float) -> bool:
        if -10.0 <= target_temp <= 150.0:
            self.jacket_temp = target_temp
            return True
        print("Error: Jacket temperature out of range (-10 to 150).")
        return False

    def simulate_thermal_step(self, time_minutes: float) -> float:
        if self.current_volume <= 0:
            return self.temperature

        k = self.heat_transfer_coeff if self.agitator_on else (self.heat_transfer_coeff / 2)
        delta_t = -k * (self.temperature - self.jacket_temp) * time_minutes
        self.temperature += delta_t
        return self.temperature

    def get_status(self):
        status = super().get_status()
        status.update({
            "jacket_temp": self.jacket_temp,
            "agitator_on": self.agitator_on
        })
        return status

if __name__ == "__main__":
  #creating reactor with a capacity of 500 liters
    reactor = CSTRJacketedReactor(
        vessel_id="R-101",
        capacity=500.0,
        current_volume=200.0,
        temperature=85.0,
        jacket_temp=20.0
    )

    print("initial condition:", reactor.get_status())
    #turn on the agitator
    reactor.toggle_agitator()
    print("trun on the ogitator:", reactor.agitator_on)

    # cooling simulation within 2 minutes
    reactor.simulate_thermal_step(time_minutes=2.0)
    print("Reactor temperature after 2minutes of cooling:", reactor.temperature)

    # addition of cold feed (50 liters at 15C)
    reactor.add_material(volume=50.0, temp=15.0)
    print("final codition after feed injection:", reactor.get_status())

