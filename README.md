# Chat Website

This project is a simple chat application built using Flask for the backend and HTML, CSS, and JavaScript for the frontend. It allows users to send and receive messages in real-time.

## Project Structure

```
chat-website
├── static
│   ├── css
│   │   └── styles.css
│   ├── js
│   │   └── scripts.js
├── templates
│   ├── index.html
│   └── chat.html
├── app.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chat-website
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the chat application.

## Features

- Real-time messaging using WebSockets.
- User-friendly interface with a responsive design.
- Simple setup and easy to extend.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.