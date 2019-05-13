from math import *

def rk4_system(f1, f2, f1_actual, f2_actual, t, y1, y2, p, h = None):
	n = int((p-t)/h)

	print(f't\t\t|\tu1\t\t\t|\tExact u1\t\t|\tu2\t\t\t|\tExact u2')
	print("-"*130)
	print(f'{t:.3f}\t\t|\t{y1:.9f}\t\t|\t{f1_actual(t):.9f}\t\t|\t{y2:.9f}\t\t|\t{f2_actual(t):.9f}')

	for i in range(n):
		k11 = h*f1(t, y1, y2)
		k12 = h*f2(t, y1, y2)

		k21 = h*f1(t + h/2, y1 + k11/2, y2 + k12/2)
		k22 = h*f2(t + h/2, y1 + k11/2, y2 + k12/2)

		k31 = h*f1(t + h/2, y1 + k21/2, y2 + k22/2)
		k32 = h*f2(t + h/2, y1 + k21/2, y2 + k22/2)

		k41 = h*f1(t + h, y1 + k31, y2 + k32)
		k42 = h*f2(t + h, y1 + k31, y2 + k32)

		y1 = y1 + (k11 + 2*k21 + 2*k31 + k41)/6
		y2 = y2 + (k12 + 2*k22 + 2*k32 + k42)/6

		t += h

		actual1 = f1_actual(t)
		actual2 = f2_actual(t)

		print(f'{t:.3f}\t\t|\t{y1:.9f}\t\t|\t{actual1:.9f}\t\t|\t{y2:.9f}\t\t|\t{actual2:.9f}')

	print("-"*130)

def main():
	# Define these functions depending on the problem.
	f1 = lambda t, u1, u2: u2
	f2 = lambda t, u1, u2: -16.085*u1

	f1_analytical = lambda t: t
	f2_analytical = lambda t: t

	t0 = float(input("t0 = "))
	y0_1 = float(input("y0_1 = "))
	y0_2 = float(input("y0_2 = "))
	p = float(input("Evaluation point = "))
	h = float(input("Enter Step-Size: "))

	rk4_system(f1, f2, f1_analytical, f2_analytical, t0, y0_1, y0_2, p, h)

if __name__ == '__main__':
	main()
