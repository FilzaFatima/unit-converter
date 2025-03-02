import streamlit as st

# Title
st.title("My Advanced Unit Converter 🔄")

# Select unit type
unit_type = st.selectbox("Select Unit Type", [
    "Length", "Area", "Data Transfer Rate", "Digital Storage", "Energy",
    "Frequency", "Fuel Economy", "Mass", "Plane Angle", "Pressure",
    "Speed", "Time", "Volume", "Temperature"
])

# Conversion Logic
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_area(value, from_unit, to_unit):
    conversion_factors = {
        "Square Meter": 1, "Square Kilometer": 0.000001, "Square Foot": 10.7639, 
        "Square Yard": 1.19599, "Acre": 0.000247105, "Hectare": 0.0001
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_data_transfer_rate(value, from_unit, to_unit):
    conversion_factors = {
        "Bit/s": 1, "Kilobit/s": 0.001, "Megabit/s": 0.000001, 
        "Gigabit/s": 1e-9, "Terabit/s": 1e-12, "Byte/s": 0.125
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_digital_storage(value, from_unit, to_unit):
    conversion_factors = {
        "Byte": 1, "Kilobyte": 0.001, "Megabyte": 0.000001, 
        "Gigabyte": 1e-9, "Terabyte": 1e-12
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_energy(value, from_unit, to_unit):
    conversion_factors = {
        "Joule": 1, "Kilojoule": 0.001, "Calorie": 0.239006, 
        "Kilocalorie": 0.000239006, "Watt-hour": 0.000277778
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_frequency(value, from_unit, to_unit):
    conversion_factors = {
        "Hertz": 1, "Kilohertz": 0.001, "Megahertz": 0.000001, 
        "Gigahertz": 1e-9
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_fuel_economy(value, from_unit, to_unit):
    conversion_factors = {
        "Kilometers per Liter": 1, "Miles per Gallon": 2.35215
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_mass(value, from_unit, to_unit):
    conversion_factors = {
        "Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_plane_angle(value, from_unit, to_unit):
    conversion_factors = {
        "Degree": 1, "Radian": 0.0174533
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_pressure(value, from_unit, to_unit):
    conversion_factors = {
        "Pascal": 1, "Bar": 1e-5, "PSI": 0.000145038
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_speed(value, from_unit, to_unit):
    conversion_factors = {
        "Meter per Second": 1, "Kilometer per Hour": 3.6, 
        "Mile per Hour": 2.23694, "Knot": 1.94384
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_time(value, from_unit, to_unit):
    conversion_factors = {
        "Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        "Liter": 1, "Milliliter": 1000, "Cubic Meter": 0.001, 
        "Gallon": 0.264172, "Pint": 2.11338
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

# User Input
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

unit_options = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Area": ["Square Meter", "Square Kilometer", "Square Foot", "Square Yard", "Acre", "Hectare"],
    "Data Transfer Rate": ["Bit/s", "Kilobit/s", "Megabit/s", "Gigabit/s", "Terabit/s", "Byte/s"],
    "Digital Storage": ["Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"],
    "Energy": ["Joule", "Kilojoule", "Calorie", "Kilocalorie", "Watt-hour"],
    "Frequency": ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"],
    "Fuel Economy": ["Kilometers per Liter", "Miles per Gallon"],
    "Mass": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Plane Angle": ["Degree", "Radian"],
    "Pressure": ["Pascal", "Bar", "PSI"],
    "Speed": ["Meter per Second", "Kilometer per Hour", "Mile per Hour", "Knot"],
    "Time": ["Second", "Minute", "Hour", "Day"],
    "Volume": ["Liter", "Milliliter", "Cubic Meter", "Gallon", "Pint"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From", unit_options[unit_type])
to_unit = st.selectbox("To", unit_options[unit_type])

if st.button("Convert"):
    conversion_function = globals()[f"convert_{unit_type.lower().replace(' ', '_')}"]
    result = conversion_function(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
