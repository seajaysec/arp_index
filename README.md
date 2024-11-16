# The Arp Index - To the Moon
Check stocks on norns (and make music).

A script that turns stock market data into musical sequences. Watch the market move while creating generative arpeggios.

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

2. Create a .env file in the script directory:
   - Add this line, replacing YOUR_KEY with your actual API key:
     `ALPHA_VANTAGE_API_KEY=YOUR_KEY`

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
