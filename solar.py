import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

class SolarPredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.encoders = {}
        self.features = []
        
    def create_sample_data(self):
        """Create realistic solar installation data"""
        np.random.seed(42)
        n = 500
        
        # Generate data
        system_size = np.random.uniform(3, 15, n)
        roof_pitch = np.random.uniform(10, 45, n)
        num_panels = np.random.randint(8, 50, n)
        panel_type = np.random.choice(['Mono', 'Poly', 'Thin'], n, p=[0.6, 0.3, 0.1])
        roof_type = np.random.choice(['Shingle', 'Metal', 'Tile'], n, p=[0.6, 0.2, 0.2])
        complexity = np.random.choice(['Simple', 'Medium', 'Complex'], n, p=[0.4, 0.4, 0.2])
        
        # Calculate labor hours (realistic formula)
        hours = (12 + system_size * 1.5 + num_panels * 0.3 + 
                (roof_pitch - 20) * 0.2 +
                np.where(panel_type == 'Thin', 3, 0) +
                np.where(roof_type == 'Tile', 6, 0) +
                np.where(complexity == 'Medium', 4, 0) +
                np.where(complexity == 'Complex', 10, 0) +
                np.random.normal(0, 2, n))
        
        hours = np.clip(hours, 8, 80)  # Keep realistic
        
        return pd.DataFrame({
            'system_size': np.round(system_size, 1),
            'roof_pitch': np.round(roof_pitch, 1),
            'num_panels': num_panels,
            'panel_type': panel_type,
            'roof_type': roof_type,
            'complexity': complexity,
            'hours': np.round(hours, 1)
        })
    
    def train(self, data_file=None):
        """Train the model"""
        # Load data
        if data_file:
            try:
                if data_file.endswith('.csv'):
                    df = pd.read_csv(data_file)
                else:
                    df = pd.read_excel(data_file)
                print(f"✅ Loaded {len(df)} records from {data_file}")
            except:
                print("❌ File not found. Using sample data.")
                df = self.create_sample_data()
        else:
            df = self.create_sample_data()
            print(f"✅ Created {len(df)} sample records")
        
        # Prepare data
        X = df.drop('hours', axis=1)
        y = df['hours']
        
        # Encode text columns
        for col in X.select_dtypes(include=['object']).columns:
            encoder = LabelEncoder()
            X[col] = encoder.fit_transform(X[col])
            self.encoders[col] = encoder
        
        self.features = X.columns.tolist()
        
        # Train model
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Show accuracy
        score = self.model.score(X_test, y_test)
        print(f"✅ Model trained! Accuracy: {score:.2%}")
        
        return self
    
    def predict_installation(self):
        """Get prediction from user input"""
        print("\n" + "="*50)
        print("🔧 SOLAR INSTALLATION TIME CALCULATOR")
        print("="*50)
        
        # Get user inputs
        try:
            system_size = float(input("System Size (kW) [e.g., 8.5]: ") or "8.5")
            roof_pitch = float(input("Roof Pitch (degrees) [e.g., 30]: ") or "30")
            num_panels = int(input("Number of Panels [e.g., 25]: ") or "25")
            
            print("\nPanel Type options: Mono, Poly, Thin")
            panel_type = input("Panel Type [Mono]: ") or "Mono"
            
            print("Roof Type options: Shingle, Metal, Tile")
            roof_type = input("Roof Type [Shingle]: ") or "Shingle"
            
            print("Complexity options: Simple, Medium, Complex")
            complexity = input("Installation Complexity [Medium]: ") or "Medium"
            
        except KeyboardInterrupt:
            print("\n❌ Cancelled by user")
            return
        except:
            print("❌ Invalid input. Using defaults.")
            system_size, roof_pitch, num_panels = 8.5, 30, 25
            panel_type, roof_type, complexity = "Mono", "Shingle", "Medium"
        
        # Prepare prediction data
        pred_data = pd.DataFrame({
            'system_size': [system_size],
            'roof_pitch': [roof_pitch],
            'num_panels': [num_panels],
            'panel_type': [panel_type],
            'roof_type': [roof_type],
            'complexity': [complexity]
        })
        
        for col in pred_data.select_dtypes(include=['object']).columns:
            if col in self.encoders:
                try:
                    pred_data[col] = self.encoders[col].transform(pred_data[col])
                except:
                    # Use first class if unknown value
                    pred_data[col] = self.encoders[col].transform([self.encoders[col].classes_[0]])
        
        # Make prediction
        hours = self.model.predict(pred_data)[0]
        days = int(hours // 8)
        remaining = int(hours % 8)
        
        # Show results
        print("\n" + "="*50)
        print("🎯 YOUR INSTALLATION ESTIMATE")
        print("="*50)
        
        print(f"📋 Your Project:")
        print(f"   • {system_size} kW system with {num_panels} panels")
        print(f"   • {panel_type} panels on {roof_type} roof")
        print(f"   • {complexity} installation complexity")
        
        print(f"\n⏱️ Time Estimate:")
        print(f"   • Total: {int(hours)} hours")
        if days > 0:
            if remaining > 0:
                print(f"   • Schedule: {days} days + {remaining} hours")
            else:
                print(f"   • Schedule: {days} days")
        else:
            print(f"   • Schedule: {int(hours)} hours (same day)")
        
        # Ask for another prediction
        again = input("\n🔄 Calculate another? (y/n): ")
        if again.lower().startswith('y'):
            self.predict_installation()

def main():
    """Run the solar predictor"""
    print("🌞 SolarSite: Solar Installation Time Predictor")
    print("=" * 50)
    

    predictor = SolarPredictor()
    
    data_file = input("Data file path (or press Enter for demo): ").strip()
    if not data_file:
        data_file = None
    
    predictor.train(data_file)
    
    # Start predictions
    predictor.predict_installation()
    
    print("\n✅ Thanks for using SolarSite!")

if __name__ == "__main__":
    main()