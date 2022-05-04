# Set initial state of l-system
initial = "AB"

# Rules for the l-system
rules = {
	"A": "AB",
	"B": "A"
}

def l_system(initial, rules, generation):
	current = initial

	for _ in range(0, generation):
		result = ""

		for state in current:
			result += rules.get(state, state)

		current = result

	return current

for i in range(0, 10):
	print( "{}: {}".format(i, l_system(initial, rules, i)) )
