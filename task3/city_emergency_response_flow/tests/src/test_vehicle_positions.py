import yaml
import osmnx as ox
import matplotlib.pyplot as plt
import os

# Load the YAML file
yaml_file_path = os.path.join(os.getcwd(), "tests/vehicle_positions/police_vehicles.yaml")
with open(yaml_file_path, "r") as file:
    data = yaml.safe_load(file)

# Define the bounding box for Cádiz
cadiz_location = "Cádiz, Spain"
graph = ox.graph_from_place(cadiz_location, network_type="all")
gdf_edges = ox.graph_to_gdfs(graph, nodes=False)  # Extract edges for plotting

# Prepare the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the base map
gdf_edges.plot(ax=ax, linewidth=0.5, color="gray", alpha=0.7)

# Plot the vehicle waypoints
for vehicle in data['police_vehicles']:
    lat = vehicle['location']['latitude']
    lon = vehicle['location']['longitude']
    vehicle_type = vehicle['type']
    color = {
        "Police Car": "blue",
        "Motorcycle": "green",
        "Police Van": "purple",
        "Armored Vehicle": "red"
    }.get(vehicle_type, "black")
    ax.scatter(lon, lat, c=color, label=vehicle_type, edgecolors="black", s=100)

# Add a legend and adjust the plot
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))  # Remove duplicate labels
ax.legend(by_label.values(), by_label.keys(), loc="upper left")
ax.set_title("Police Vehicles in Cádiz", fontsize=16)
plt.axis("off")

# Save to PNG
output_file = os.path.join(os.getcwd(), "cadiz_police_vehicles_map.png")
plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.show()
