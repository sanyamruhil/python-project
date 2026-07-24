import matplotlib.pyplot as plt

# Initialize lists to store data
names = []
bmis = []
categories = []

# Get the total number of people from the user
num_people = int(input("Enter the number of people: "))

# Collect data using a loop
for i in range(num_people):
    print(f"\n--- Person {i+1} ---")
    name = input("Enter name: ")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    
    # Calculate BMI
    bmi = round(weight / (height ** 2), 2)
    
    # Determine health category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
        
    # Append values to lists
    names.append(name)
    bmis.append(bmi)
    categories.append(category)
    
    print(f"{name}'s BMI is {bmi} ({category})")

# Calculate statistics using built-in functions
min_bmi = min(bmis)
max_bmi = max(bmis)
avg_bmi = round(sum(bmis) / len(bmis), 2)

# Find names associated with min and max BMI
min_person = names[bmis.index(min_bmi)]
max_person = names[bmis.index(max_bmi)]

# Display statistics
print("\n================ STATISTICS ================")
print(f"Minimum BMI: {min_bmi} ({min_person})")
print(f"Maximum BMI: {max_bmi} ({max_person})")
print(f"Average BMI: {avg_bmi}")
print("============================================")

# Assign colors to bars based on their BMI category
colors = []
for cat in categories:
    if cat == "Underweight": colors.append('skyblue')
    elif cat == "Normal weight": colors.append('green')
    elif cat == "Overweight": colors.append('orange')
    else: colors.append('red')

# Set up the plot
plt.figure(figsize=(10, 6))
bars = plt.bar(names, bmis, color=colors, edgecolor='black', width=0.5)

# Add BMI text labels on top of each bar
for bar in bars:
    y_value = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, y_value + 0.3, f'{y_value}', ha='center', va='bottom', fontweight='bold')

# Draw a reference line for the calculated average BMI
plt.axhline(y=avg_bmi, color='purple', linestyle='--', linewidth=1.5, label=f'Avg BMI ({avg_bmi})')

# Graph customization
plt.title('BMI Comparison Chart', fontsize=14, fontweight='bold')
plt.xlabel('Names', fontsize=12)
plt.ylabel('BMI Values', fontsize=12)
plt.ylim(0, max(bmis) + 5)
plt.grid(axis='y', linestyle=':', alpha=0.5)
plt.legend()

# Render graph
plt.tight_layout()
plt.show()