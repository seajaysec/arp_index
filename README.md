# The Arp Index - To the Moon
Turn stock market data into musical sequences. Watch the market move while creating generative arpeggios with Molly the Poly.

## Installation

1. Install Molly the Poly engine in maiden:
   ```
   ;install https://github.com/markwheeler/molly_the_poly/archive/master.zip
   ```

2. Install The Arp Index:
   ```
   ;install https://github.com/seajaysec/arp_index/archive/master.zip
   ```

## Requirements
- norns
- molly_the_poly engine (installed above)
- internet connection
- Alpha Vantage API key (free)

## Setup

1. Get a free API key from Alpha Vantage:
   - Go to https://www.alphavantage.co/support/#api-key
   - Sign up for your key
   - Copy your API key

2. Create your API key file:
   - Copy api.key.sample to api.key
   - Replace the contents with your API key
   - Make sure there are no extra spaces or newlines

## Controls
- E1 : Select company
- E2 : Time span (1d/1m/3m/1y)
- E3 : Number of steps
- K2 : Play/Stop
- K1+K2 : Reset clock
- K3 : Refresh data / Generate new sound

## Features
- Live stock data visualization
- Price-driven musical sequences
- Randomly generated synth presets per stock
- MIDI input/output support
- Multiple time ranges

Data provided by Alpha Vantage (www.alphavantage.co)
