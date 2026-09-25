# 🧪 Jacketed CSTR Thermal & Mass Balance Simulation (Python OOP)

An Object-Oriented Python project modeling an industrial Jacketed Continuous Stirred-Tank Reactor (CSTR) with mass and energy balances, agitator dynamics, and thermal heat exchange using Newton's Law of Cooling.

---

## 📌 Features
- **Object-Oriented Architecture:** Uses inheritance with a base `BaseVessel` class extended by `CSTRJacketedReactor`.
- **Thermal Energy Balance:** Calculates weighted equilibrium temperatures during dynamic feed addition.
- **Cooling/Heating Dynamics:** Implements Newton's Law of Cooling:
  $$\Delta T = -k \cdot (T_{\text{reactor}} - T_{\text{jacket}}) \cdot \Delta t$$
- **Operational Logic:** Agitator state directly modulates the overall heat transfer coefficient ($k$).
- **State Monitoring:** Built-in telemetry methods returning structured operating dictionaries.

---

## 🚀 Quick Start

Run the simulation script directly with Python:
```bash
python reactor.py
```
## Example Usage:
```python
from reactor import CSTRJacketedReactor

# Initialize reactor
reactor = CSTRJacketedReactor(
    vessel_id="R-101",
    capacity=500.0,
    current_volume=200.0,
    temperature=85.0,
    jacket_temp=20.0
)

# Start agitator and run thermal step for 2 minutes
reactor.toggle_agitator()
reactor.simulate_thermal_step(time_minutes=2.0)

# Add cold feed stream (50 L at 15 °C)
reactor.add_material(volume=50.0, temp=15.0)

print(reactor.get_status())
```

## 👨‍💻 Author
Mehrshad Abbasi
