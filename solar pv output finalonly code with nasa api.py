import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders if they don't exist
os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# Save CSV
# df.to_csv("data/solar_data.csv", index=False) # This line was misplaced

# -------------------------------
# 1. FETCH DATA FROM NASA API
# -------------------------------
url = "https://power.larc.nasa.gov/api/temporal/hourly/point"
params = {
    "parameters": "ALLSKY_SFC_SW_DWN",
    "community": "RE",
    "longitude": 88,
    "latitude": 25,
    "format": "JSON",
    "start": "20240101",
    "end": "20240101"
}

response = requests.get(url, params=params)
data = response.json()

# -------------------------------
# 2. EXTRACT IRRADIANCE
# -------------------------------
irradiance_dict = data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]

hours = list(range(24))
irradiance = np.array(list(irradiance_dict.values()))

# -------------------------------
# 3. PV PARAMETERS
# -------------------------------
panel_area = 1.6        # m²
efficiency = 0.18       # 18%
performance_ratio = 0.75

# -------------------------------
# 4. CALCULATE POWER OUTPUT
# -------------------------------
power_output = irradiance * panel_area * efficiency * performance_ratio

# -------------------------------
# 5. FIND PEAK
# -------------------------------
peak_power = np.max(power_output)
peak_hour = hours[np.argmax(power_output)]

print(f"Peak Power: {peak_power:.2f} W")
print(f"Peak Hour: {peak_hour}:00")

# -------------------------------
# 6. SAVE DATA
# -------------------------------
df = pd.DataFrame({
    "Hour": hours,
    "Irradiance (W/m²)": irradiance,
    "Power Output (W)": power_output
})

df.to_csv("data/solar_data.csv", index=False)

# -------------------------------
# 7. PLOT IRRADIANCE
# -------------------------------
plt.figure()
plt.plot(hours, irradiance)
plt.title("Solar Irradiance vs Time")
plt.xlabel("Hour")
plt.ylabel("Irradiance (W/m²)")
plt.grid()
plt.savefig("outputs/irradiance_plot.png")
plt.close()

# -------------------------------
# 8. PLOT POWER OUTPUT
# -------------------------------
plt.figure()
plt.plot(hours, power_output)
plt.title("Solar PV Power Output vs Time")
plt.xlabel("Hour")
plt.ylabel("Power (W)")
plt.grid()
plt.savefig("outputs/power_output_plot.png")
plt.close()