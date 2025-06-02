# OpenFrontPY

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="resources/images/OpenFrontLogoDark.svg">
    <source media="(prefers-color-scheme: light)" srcset="resources/images/OpenFrontLogo.svg">
    <img src="resources/images/OpenFrontLogo.svg" alt="OpenFrontIO Logo" width="300">
  </picture>
</p>

[](https://crowdin.com/project/openfront-mls)

OpenFront is an online real-time strategy game focused on territorial control and alliance building. Players compete to expand their territory, build structures, and form strategic alliances in various maps based on real-world geography.

This (OpenFrontPY) is a fork of OpenFront.io this fork aims to replace the server with fastapi while still allowing for easy modifications to the source code

# OpenFront - Licensing

This project uses a dual-licensing approach:

- Code in the `server/` and `core/` directory is licensed under MIT
- Client code (in the `client/` directory) is licensed under GPL v3

## 🌟 Features

- **Real-time Strategy Gameplay**: Expand your territory and engage in strategic battles
- **Alliance System**: Form alliances with other players for mutual defense
- **Multiple Maps**: Play across various geographical regions including Europe, Asia, Africa, and more
- **Resource Management**: Balance your expansion with defensive capabilities
- **Cross-platform**: Play in any modern web browser

## 📋 Prerequisites

- [npm](https://www.npmjs.com/) (v10.9.2 or higher)
- A modern web browser (Chrome, Firefox, Edge, etc.)
- Python (3.11 or higher)
- FastApi[Standard] through pip

## 🚀 Bundling And interpreting the source code
to compile the application use 
```bash
npm run build-dev
```

## Running the Client
```bash
fastapi run client.py
```
