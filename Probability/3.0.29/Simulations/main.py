import numpy as np
import matplotlib.pyplot as plt


def p(x):
    return (1 / np.sqrt(np.pi)) * np.exp(-x**2)

a, b = 0.6, 0.8
h = b - a

p_a = p(a)
p_b = p(b)


area = (h / 2) * (p_a + p_b)
print(f"Calculated Area (Trapezoidal Rule): {area:.4f}")

x_curve = np.linspace(0, 1.5, 500)
y_curve = p(x_curve)

plt.figure(figsize=(8, 5))
plt.plot(x_curve, y_curve, label=r'$p(x) = \frac{1}{\sqrt{\pi}}e^{-x^2}$', color='blue')

x_trap = [a, a, b, b]
y_trap = [0, p_a, p_b, 0]
plt.fill(x_trap, y_trap, color='red', alpha=0.3, label=f'Trapezoid Area $\\approx$ {area:.3f}')
plt.plot([a, b], [p_a, p_b], color='red', linestyle='--', linewidth=2) # Top edge

plt.title("Trapezoidal Rule Approximation")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

