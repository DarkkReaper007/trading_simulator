let prices = [];
let timestamps = [];
let signals = [];
const socket = new WebSocket("ws://localhost:8000/ws");

socket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    const time = new Date().toLocaleTimeString();

    prices.push(data.price);
    timestamps.push(time);
    signals.push(data.signal);

    if (prices.length > 50) {
        prices.shift();
        timestamps.shift();
        signals.shift();
    }

    const trace = {
        x: timestamps,
        y: prices,
        type: 'scatter',
        mode: 'lines+markers',
        line: { color: 'cyan' },
        marker: {
            color: signals.map(signal =>
                signal === "buy" ? "green" :
                signal === "sell" ? "red" : "gray"
            ),
            size: 10
        }
    };

    Plotly.newPlot("chart", [trace], {
        paper_bgcolor: "#0f0f0f",
        plot_bgcolor: "#0f0f0f",
        font: { color: "white" }
    });
};

function changeStrategy(strategy) {
    socket.send(JSON.stringify({ strategy }));
}
