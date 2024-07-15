
GPS TOLL BASED SYSTEM STIMULATION USING PYTHON


This project simulates vehicle movements and toll payments on a highway using Flask, SimPy, and Socket.IO. The simulation visualizes the route and toll gates on a map and dynamically updates vehicle positions and toll payments.

Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

Project Overview

The India Highway Toll Simulation is an interactive simulation project that demonstrates vehicle interactions with toll gates on an Indian highway route. The project leverages Flask for serving the web interface, SimPy for simulation logic, and Socket.IO for real-time updates between the server and client.

Features

- Real-time vehicle movement simulation
- Dynamic toll gate interactions and charges
- Visualization of the highway route and toll gates on a map
- Detailed logging of toll payments and vehicle movements
- Calculation of distances traveled by each vehicle

Installation

Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

Steps

1. Clone the repository:**

    sh
    git clone https://github.com/your-username/india-highway-toll-simulation.git
    

2. Navigate to the project directory:**

    sh
    cd india-highway-toll-simulation
  

3. Install the dependencies:**

   sh
    pip install -r requirements.txt
    

4. Run the application:**

    sh
    python app.py
   

Usage

Once the application is running, open your web browser and go to `http://127.0.0.1:5000/` to view the simulation.

 Simulation Details

- Vehicles: The simulation generates random vehicles (cars, trucks, buses) that travel along the predefined route.
- Toll Gates: Vehicles interact with toll gates along the route, and charges are applied based on vehicle type.
- Distance Calculation: The simulation calculates the distance traveled by each vehicle and the distance to the next point in the route.

File Structure


/india-highway-toll-simulation
├── app.py                     # Main application script
├── requirements.txt           # List of dependencies
├── static
│   └── style.css              # CSS for styling the web page
├── templates
│   └── index.html             # HTML template for the web page
└── README.md                  # Project documentation


 app.py

This is the main script that runs the Flask application, handles the simulation logic with SimPy, and manages real-time communication using Socket.IO. It also includes distance calculation for each vehicle.

requirements.txt

Contains the list of dependencies required for the project.

static/style.css

CSS file for styling the web interface.

 templates/index.html

HTML template for rendering the web interface.

Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

 Steps to Contribute

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Author

Swayam Pandey

Feel free to reach out for any questions or feedback!

