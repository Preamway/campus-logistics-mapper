import pandas as pd
import folium

def main():
    print("Initializing Big Red Shipping Logistics Mapper...")

    # 1. CREATE MOCK ORDER DATA (Cornell Campus Locations)
    # In real life, this would be an export of your daily work orders
    data = {
        'Order_ID': ['BRS-001', 'BRS-002', 'BRS-003', 'BRS-004', 'BRS-005'],
        'Location': ['North Campus (Dickson)', 'West Campus (Becker)', 'Collegetown', 'Engineering Quad', 'Schoellkopf Field'],
        'Lat': [42.4532, 42.4473, 42.4418, 42.4442, 42.4447],
        'Lon': [-76.4784, -76.4880, -76.4842, -76.4820, -76.4760],
        'Boxes_to_Ship': [12, 5, 8, 2, 15]
    }
    
    df = pd.DataFrame(data)
    print(f"Loaded {len(df)} daily work orders.")

    # 2. INITIALIZE THE MAP
    # Centered roughly on Cornell University coordinates
    campus_map = folium.Map(location=[42.4476, -76.4800], zoom_start=15, tiles="CartoDB positron")

    # 3. PLOT EACH ORDER ON THE MAP
    for index, row in df.iterrows():
        # Create an interactive popup text
        popup_text = f"<b>Order:</b> {row['Order_ID']}<br><b>Items:</b> {row['Boxes_to_Ship']} boxes"
        
        # Add the marker to the map
        folium.Marker(
            location=[row['Lat'], row['Lon']],
            popup=folium.Popup(popup_text, max_width=200),
            tooltip=f"Click for {row['Location']} info",
            icon=folium.Icon(color="red", icon="box", prefix="fa")
        ).add_to(campus_map)

    # 4. SAVE THE MAP AS A WEB PAGE
    output_file = "index.html"
    campus_map.save(output_file)
    print(f"Success! Interactive map saved as {output_file}")

if __name__ == "__main__":
    main()
