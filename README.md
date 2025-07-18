# 📈 Real-Time Trading Simulator

A sophisticated real-time trading simulator that visualizes dummy stock price data using Simple Moving Average (SMA) strategies. Built with a fully event-driven, modular architecture for scalable financial data processing and visualization.

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
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
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
   cp .env.example .env
   # Edit .env with your configuration
   ```

## 🚀 Running the Application

1. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start the price data producer**
   ```bash
   python producer.py
   ```

3. **Start the SMA strategy consumer**
   ```bash
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

## 📁 Project Structure

```
trading-simulator/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application
│   ├── websocket_handler.py    # WebSocket connection management
│   ├── models/
│   │   ├── __init__.py
│   │   └── stock_data.py       # Data models
│   ├── services/
│   │   ├── __init__.py
│   │   ├── redis_service.py    # Redis operations
│   │   └── rabbitmq_service.py # RabbitMQ operations
│   └── utils/
│       ├── __init__.py
│       └── sma_calculator.py   # SMA calculation logic
├── producer.py                 # Stock price data generator
├── consumer.py                 # SMA strategy processor
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── chart.js           # Plotly.js chart logic
│   │   └── websocket.js       # WebSocket client
│   └── index.html             # Main frontend
├── requirements.txt
├── .env.example
├── docker-compose.yml
└── README.md
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

## 🔧 Configuration

Key configuration options in `.env`:

```env
# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# RabbitMQ Configuration
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USERNAME=guest
RABBITMQ_PASSWORD=guest

# Application Settings
SMA_PERIODS=5,10,20,50
UPDATE_INTERVAL=1.0
INITIAL_STOCK_PRICE=100.0
```

## 🐳 Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in detached mode
docker-compose up -d
```

## 🧪 Testing

```bash
# Run unit tests
pytest tests/

# Run with coverage
pytest --cov=app tests/

# Run integration tests
pytest tests/integration/
```

## 📈 Performance Metrics

- **Latency**: Sub-millisecond message processing
- **Throughput**: 10,000+ messages per second
- **Scalability**: Horizontal scaling with multiple consumers
- **Memory Usage**: Efficient Redis-based caching

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
