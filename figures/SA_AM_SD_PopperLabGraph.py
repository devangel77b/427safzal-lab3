import matplotlib.pyplot as plt

# Data
x = [0.000, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.060]
y = [0.071, 1.47, 2.94, 4.41, 5.70, 7.35, 8.57, 7.48, 6.18, 5.53, 4.24, 4.66, 4.68]

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o')
plt.xlabel('Displacement (m)')
plt.ylabel('Force (N)')
plt.title('Force vs. Displacement')
plt.grid(True)

# Save
plt.savefig('force_vs_displacement.png', dpi=300, bbox_inches='tight')
plt.savefig('force_vs_displacement.svg', bbox_inches='tight')

plt.show()