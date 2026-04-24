# AI-Enhanced-Solar-PV-Output-Analysis
AI-powered solar PV output analysis using NASA real-time data, with visualization, peak detection, and performance insights.

AI-powered solar PV output analysis using NASA real-time data, with visualization, peak detection, and performance insights.


📌 Abstract
This project presents a data-driven analysis of solar photovoltaic (PV) output using real-time irradiance data from the NASA POWER API.
The system:


Processes hourly solar radiation data


Computes PV power output


Identifies peak generation periods


Visualizes performance trends


It demonstrates how satellite data can be used for accurate solar energy assessment and optimization.

🚀 Features


📡 Real-time solar data fetching (NASA API)


⚡ PV power output calculation


🔝 Peak power & peak hour detection


📊 Data visualization (irradiance & output)


💾 CSV data storage for reuse



🌍 Project Location


📍 Malda, India (Latitude & Longitude based analysis)



🛰️ Data Source


NASA POWER API


Parameter used: ALLSKY_SFC_SW_DWN


Key Features:


Satellite-based measurement


Hourly resolution


Global accessibility



⚙️ Methodology
1️⃣ Data Collection


API request using requests


Data retrieved in JSON format


Extracted hourly irradiance (0–23)


2️⃣ Data Processing


Converted into NumPy arrays


Structured using Pandas


Indexed hour-wise


3️⃣ PV System Modeling
Formula used:
P = G × A × η × PR
Where:


G = Solar irradiance (W/m²)


A = Panel area (1.6 m²)


η = Efficiency (18%)


PR = Performance ratio (0.75)



4️⃣ Peak Detection


Peak Power = max(power_output)


Peak Hour = argmax(power_output)



5️⃣ Data Storage
data/solar_data.csv
✔ Reusable
✔ Easy analysis
✔ Integration-ready

6️⃣ Visualization
Generated plots:


🌞 Solar Irradiance vs Time


⚡ PV Power Output vs Time


Saved in:
outputs/irradiance_plot.png  outputs/power_output_plot.png

📊 Results & Analysis
🌞 Irradiance Observations


Follows daily cycle


Zero at night


Peaks at midday


⚡ Power Output


Directly proportional to irradiance


Maximum at peak sunlight hours


Influenced by efficiency & losses



🔝 Peak Insights


Identifies maximum generation capacity


Helps in:


Load planning


Storage optimization


Grid integration





📂 Output Files
FileDescriptionsolar_data.csvProcessed datasetirradiance_plot.pngSunlight variationpower_output_plot.pngPV performance

🧠 Applications


Solar system design


Energy forecasting


Peak load management


Renewable energy research



⚠️ Limitations


Single-day analysis


No temperature/shading losses


Fixed efficiency


No battery or load modeling



🔮 Future Work


📅 Yearly analysis


🤖 AI-based forecasting


🔋 Battery integration


🌍 Multi-location comparison (e.g., Berlin)


📊 Interactive dashboard



🏁 Conclusion
This project demonstrates the practical use of NASA satellite data for solar PV analysis.
It highlights how data-driven modeling improves renewable energy planning and optimization.

🔑 Keywords
Solar PV, NASA API, Irradiance, Renewable Energy, Peak Power, Data Analysis

📜 License
This project is licensed under the MIT License.

👤 Author
Oihika Arpit
🎓 Renewable Energy Enthusiast | Data-Driven Energy Analyst

⭐ Support
If you found this project useful:
⭐ Star this repo
🍴 Fork it
📢 Share it

