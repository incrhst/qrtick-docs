# QRTick Fee Calculator (Vite + React)

This project provides a standalone, interactive fee calculator for QRTick, built with React and Vite. It is designed to be embedded as a static HTML page (e.g., `fee-calculator.html`) in your documentation or website.

## Features
- QRTick-branded, interactive fee calculator
- Built with React + TypeScript + Vite
- Outputs a single HTML page and assets for easy deployment

## Setup

### Using the Makefile (Recommended)

A `Makefile` is provided to automate the full workflow:
- Installs dependencies
- Builds the Vite app
- Renames `dist/index.html` to `dist/fee-calculator.html`
- Copies the built HTML and (if present) the `assets/` folder to your project root

**To build and deploy everything:**
```sh
make all
```
This will leave you with `fee-calculator.html` and (if needed) an `assets/` folder in your site root, ready to use.

**To just build and deploy (after dependencies are installed):**
```sh
make deploy
```

The Makefile is robust: it only copies the `assets/` directory if it exists, so you won't get errors if there are no static assets.

## Manual Setup (if not using Makefile)

1. **Install dependencies:**
   ```sh
   npm install
   ```
2. **Development mode:**
   ```sh
   npm run dev
   ```
   Open [http://localhost:5173](http://localhost:5173) to view the calculator locally.
3. **Build for production:**
   ```sh
   npm run build
   ```
   This will output static files to the `dist/` directory.
4. **Deploy to your site:**
   - Rename `dist/index.html` to `fee-calculator.html` and copy to your site root.
   - Copy the `dist/assets/` folder if it exists.
   - Make sure your main site links to `fee-calculator.html`.

## Example Deployment (for plain HTML site)

1. After building, copy these files to your site root:
   - `dist/fee-calculator.html` (rename from `index.html`)
   - `dist/assets/` (all JS/CSS assets, if present)

2. Update your main `index.html` to link to `fee-calculator.html`:
   ```html
   <a href="fee-calculator.html">Try the Fee Calculator</a>
   ```

## License
MIT
