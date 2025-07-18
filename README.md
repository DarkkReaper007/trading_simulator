# 📈 Real-Time Trading Simulator

A sophisticated real-time trading simulator that visualizes dummy stock price data using Simple Moving Average (SMA) strategies. Built with a fully event-driven, modular architecture for scalable financial data processing and visualization.

<img width="1902" height="939" alt="image" src="https://github.com/user-attachments/assets/e2f6f6b0-1b24-4bca-b13a-fe93fade2ef7" />


## 🚀 Features

- **Real-time Data Streaming**: Live stock price updates using WebSockets
- **SMA Strategy Implementation**: Automated Simple Moving Average calculations and signals
- **Interactive Visualizations**: Dynamic candlestick charts with SMA overlays using Plotly.js
- **Event-Driven Architecture**: Decoupled components using message queues for scalability
- **Modular Design**: Clean separation of concerns with producer-consumer pattern

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**: Core programming language
- **FastAPI**: High-performance web framework with automatic API documentation
- **RabbitMQ**: Message broker for reliable event streaming
- **Redis**: In-memory data store for caching and session management
- **aio-pika**: Asynchronous RabbitMQ client for Python

### Frontend
- **HTML5/CSS3**: Modern responsive web interface
- **JavaScript (ES6+)**: Client-side logic and WebSocket handling
- **Plotly.js**: Interactive financial charts and visualizations

### Communication
- **WebSockets**: Real-time bidirectional communication
- **REST APIs**: RESTful endpoints for configuration and data access

## 📋 Prerequisites

- Python 3.8 or higher
- Redis server
- RabbitMQ server
- Node.js (for frontend development)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/trading-simulator.git
   cd trading-simulator
   ```

2. **Set up Python environment**
   ```bash
   cd backend
   python -m venv ../venv
   source ../venv/bin/activate  # On Windows: ..\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Install and start Redis**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install redis-server
   sudo systemctl start redis-server
   
   # macOS
   brew install redis
   brew services start redis
   ```

4. **Install and start RabbitMQ**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install rabbitmq-server
   sudo systemctl start rabbitmq-server
   
   # macOS
   brew install rabbitmq
   brew services start rabbitmq
   ```

5. **Configure environment variables**
   ```bash
   cd backend
   cp .env.example .env
   # Edit .env with your configuration
   ```

## 🚀 Running the Application

1. **Start the FastAPI server**
   ```bash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start the price data producer**
   ```bash
   cd backend
   python producer.py
   ```

3. **Start the SMA strategy consumer**
   ```bash
   cd backend
   python consumer.py
   ```

4. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`
   - API documentation available at `http://localhost:8000/docs`

## 📊 Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Price Data    │    │   RabbitMQ      │    │   SMA Strategy  │
│   Producer      │───▶│   Message       │───▶│   Consumer      │
│                 │    │   Queue         │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│     Redis       │    │    FastAPI      │    │   WebSocket     │
│   Data Store    │◀───│   Web Server    │───▶│   Real-time     │
│                 │    │                 │    │   Updates       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Frontend      │
                       │   (Plotly.js)   │
                       │                 │
                       └─────────────────┘
```



## 🎯 Key Features Explained

### Real-time Data Flow
- **Producer**: Generates realistic stock price data with configurable volatility
- **Message Queue**: RabbitMQ ensures reliable delivery and decoupling
- **Consumer**: Processes price data and calculates SMA indicators
- **WebSocket**: Streams updates to connected clients in real-time

### SMA Strategy
- Calculates Simple Moving Averages for multiple periods (5, 10, 20, 50)
- Generates buy/sell signals based on SMA crossovers
- Tracks portfolio performance and P&L

### Interactive Charts
- Real-time candlestick charts with volume indicators
- SMA overlay lines with customizable periods
- Zoom, pan, and hover functionality
- Responsive design for mobile and desktop


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Plotly.js](https://plotly.com/javascript/) for powerful visualization capabilities
- [RabbitMQ](https://www.rabbitmq.com/) for reliable message queuing
- [Redis](https://redis.io/) for high-performance caching

## 📧 Contact

Shasmeet Shinde - [shasmeet.shasmeet@gmail.com](mailto:shasmeet.shasmeet@gmail.com)

Project Link: [https://github.com/DarkkReaper007/trading-simulator](https://github.com/DarkkReaper007/trading-simulator)

---

⭐ Star this repository if you found it helpful!
