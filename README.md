# World News — 18 November 2026

An original, text-and-shapes newspaper front page summarizing six verified stories from Wednesday, 18 November 2026. The APEC summit in Shenzhen leads the page; five compact dispatches cover the Gulf, Ukraine, US politics, technology, health, and weather.

## Stories

- **APEC, Shenzhen:** Xi Jinping meets Vladimir Putin; Donald Trump joins them for a three-way summit on Thursday.
- **Gulf:** Iranian drones hit Kuwait and Bahrain; the US strikes a missile site on Qeshm Island.
- **Ukraine:** The Kerch Bridge partly collapses after Ukrainian drone and missile attacks.
- **USA:** Democrat Mary Peltola wins the Alaska Senate seat; Democrats take a 56–44 majority.
- **Tech:** Nvidia revenue doubles to $115.8bn; the board rejects former chief Jensen Huang's return as CEO.
- **Health / Weather:** The US loses its measles-free status after 26 years (5,400+ cases, 10 deaths; Ebola in DR Congo tops 11,000), and Cyclone Akvan nears India's east coast.

## Run

Requires Python 3 with Pillow 10.2.0 to redraw the PNG. Run `python3 draw_image.py` from this directory. The make.fun entry point uses Node 22 and only the standard library; it copies the committed `entry.png` byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`):

```sh
node main.ts
```

## Sources

- Open Chronicle, “Global News Brief,” 18 Nov 2026
- Horizon, “World news and markets for 18 November 2026”
- Reuters, “Trump's historic meeting with Xi, Putin headlines Asia trip,” 18 Nov 2026
- NPR News Now, 3am ET, 18 Nov 2026
- Daily News, “Iran Strikes Kuwait & Bahrain, Kerch Bridge Hit Again,” 18 Nov 2026
