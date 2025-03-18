def user_input():
	print("Stock Data Visualizer")
	print("---------------------")

	# Get the Stock symbol
	while True:
		symbol = input(\nEnter the stock syymbol you are looking for: ").strip().upper()
		if not symbol:
			print("Error: Stock symbol cannot be empty. Please enter a valid stock symbol.")
		elif not symbol.isalpha():
			print("Error: Sockt symbol should only contain letters: Please enter a valid stock symbol.")
			break
	
	# Get the Chart type
	while True:
		print("\nChart Types")
		print("-------------")
		print("1. Bar")
		print("2. Line")
		try:
			chart_type = input(\nEnter the chart type you want (1, 2): ").strip()
			chart_type = input(chart_type)
			if chart_type not in [1, 2]:
				print("Error: Please enter a number 1 or 2.")
			else:
				break
		except ValueError:
			print("Error: Please enter a number 1 or 2.")

