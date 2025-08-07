# 🌞 SolarSite - Solar Installation Time Predictor

A simple AI-powered tool to predict solar panel installation time based on project specifications.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🚀 Features

- **Simple Input**: Just enter your project details
- **Accurate Predictions**: AI model trained on installation data
- **Time Estimates**: Get hours and work days needed
- **No Technical Jargon**: User-friendly interface
- **Works Offline**: No internet required after download

## 📋 Requirements

- Python 3.7 or higher
- Required packages (install with pip):

```bash
pip install pandas numpy scikit-learn
```

## 🛠️ Installation

1. **Clone or Download**
   ```bash
   git clone https://github.com/yourusername/solarsite-predictor.git
   cd solarsite-predictor
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Program**
   ```bash
   python solar_predictor.py
   ```

## 💡 How to Use

1. Run the program
2. Enter your project details:
   - System size (kW)
   - Roof pitch (degrees)
   - Number of panels
   - Panel type (Mono/Poly/Thin)
   - Roof type (Shingle/Metal/Tile)
   - Installation complexity (Simple/Medium/Complex)
3. Get instant time estimates!

## 📊 Example Output

```
🎯 YOUR INSTALLATION ESTIMATE
==============================================
📋 Your Project:
   • 8.5 kW system with 25 panels
   • Mono panels on Shingle roof
   • Medium installation complexity

⏱️ Time Estimate:
   • Total: 28 hours
   • Schedule: 3 days + 4 hours
```

## 🔧 Using Your Own Data

Want to use your own installation data? Easy!

1. Prepare a CSV file with columns: `system_size`, `roof_pitch`, `num_panels`, `panel_type`, `roof_type`, `complexity`, `hours`
2. Run the program and enter your file path when prompted
3. The AI will train on your data for more accurate predictions

## 🤝 Contributing

Found a bug or want to add features? 

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🎯 About

Created to help solar installers and project managers estimate installation time more accurately. Uses machine learning to analyze project factors and predict labor hours needed.

## 📞 Support

Having issues? 
- Open an [issue]([(https://github.com/AIRAM-023/solarsite-predictor)/issues)] on GitHub
- Check the documentation above
- Make sure all requirements are installed

---

⭐ **Star this repo if you find it helpful!** ⭐
