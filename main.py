from pyscript import document

# Create a dictionary of non-metallic elements
non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "HE": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "NE": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "CL": ("Chlorine", 17, 35.45)
}

# Create an event function
def periodic(e):
    element_Name = document.getElementById("element_input").value.strip().upper()

    # Look up dictionary
    var2 = non_metals.get(element_Name, ("Element not found", "-", "-"))

    # Display result
    document.getElementById("div_name").innerHTML = f"""
        Symbol: {element_Name}<br>
        Element: {var2[0]}<br>
        Atomic Number: {var2[1]}<br>
        Atomic Mass: {var2[2]}
    """