# ELIXIR TECHNOLOGY

## Overview
ELIXIR TECHNOLOGY is a Python + Kivy geophysical data analysis and visualization application. Originally designed as an Android app for reading Arduino sensor data via Bluetooth Classic, it provides 2D heatmap, 4D voxel visualization, and real-time pointer mode for underground data analysis.

## Project Architecture

### Language & Framework
- **Language**: Python 3.11
- **UI Framework**: Kivy 2.3.0
- **Dependencies**: numpy, Pillow (see requirements.txt)
- **Build System**: Buildozer (for Android APK generation, see buildozer.spec)

### Directory Structure
```
src/
├── main.py              # App entry point (ElixirApp class)
├── assets/              # Icons and images (AI-generated)
│   ├── elixir_logo.png  # App logo
│   ├── icon_*.png       # UI icons (underground, pointer, bluetooth, 3d, etc.)
├── screens/
│   ├── splash_screen.py # Animated splash with logo fade-in and glow effect
│   ├── main_menu.py     # Main menu with card-based mode selection
│   ├── underground.py   # Underground imaging (heatmap, grid, 4D voxel, scanning)
│   └── pointer.py       # Real-time pointer/gauge mode with modern gauge
├── components/
│   ├── bluetooth_manager.py  # Bluetooth Classic connection (mock on non-Android)
│   ├── grid_manager.py       # Grid creation and scan management
│   ├── heatmap.py            # 2D heatmap widget (golden grid theme)
│   ├── voxel_view.py         # 4D voxel visualization with layer selection
│   ├── depth_calculator.py   # Magnetic gradiometer depth calculation
│   ├── data_io.py            # CSV import/export
│   └── surface3d.py          # 3D surface visualization (placeholder)
├── utils/
│   ├── constants.py
│   ├── helpers.py
│   └── theme.py         # Color theme constants (black + gold)
arduino/
└── sensor_code/
    └── sensor_code.ino   # Arduino sensor firmware
buildozer.spec            # Android build configuration
```

### Theme
- **Background**: Pure black (#0A0A0A) with dark card surfaces (#1A1A1A)
- **Primary Color**: Gold (#FFD700) for text, borders, accents
- **Status Colors**: Green (#00E676) success, Red (#FF5252) danger, Blue (#448AFF) info
- **UI Style**: Card-based layout with rounded corners, golden borders, icon-enhanced buttons

### Running the App
The app runs as a VNC desktop application on Replit using the workflow:
```
cd /home/runner/workspace/src && python main.py
```

### Key Features
- **Underground Imaging Mode**: Bluetooth scanning with configurable grid, zigzag/parallel scan patterns, 2D heatmap, depth calculation
- **4D Voxel Visualization**: Interactive 3D+depth voxel renderer with layer selection, rotation, zoom
- **Pointer Mode**: Real-time circular gauge with tick marks, sweep indicator, pulse animation, color-coded values
- **Data I/O**: CSV export/import for scan data
- **Mock Bluetooth**: On non-Android platforms, generates random sensor data for testing
- **Animated Splash**: Logo fade-in with golden glow animation

## User Preferences
- Turkish language UI (app text is in Turkish)
- Modern dark theme with black background and gold accents
- Icon-enriched UI with descriptive labels
- Eye-friendly (non-straining) color scheme
