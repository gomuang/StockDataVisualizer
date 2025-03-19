def user_input():
	print("Stock Data Visualizer")
	print("---------------------")

	# Get the Stock symbol
	while True:
		symbol = input("\nEnter the stock syymbol you are looking for: ").strip().upper()
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
			chart_type = input("\nEnter the chart type you want (1, 2): ").strip()
			chart_type = input(chart_type)
			if chart_type not in [1, 2]:
				print("Error: Please enter a number 1 or 2.")
			else:
				break
		except ValueError:
			print("Error: Please enter a number 1 or 2.")

		# Get the time series
	while True:
		print("\nTime Series")
		print("-------------")
		print("1. Intraday")
		print("2. Daily")
		print("3. Weekly")
		print("4. Monthly")
		try:
			time_series = input("\nEnter the time series you want (1, 2, 3, 4): ").strip()
			time_series = int(time_series)
			if time_series not in [1, 2, 3, 4]:
				print("Error: Please enter a number 1, 2, 3, or 4.")
			else:
				break
		except ValueError:
			print("Error: Please enter a number 1, 2, 3, or 4.")

	# Get the date range
	start_date = None
	end_date = None

	while True:
		try:
			start_date = input("\nEnter the start date (YYYY-MM-DD): ").strip()
			if not start_date:
				print("Error: Start date cannot be empty. Please enter a valid start date.")
			else:
				break
		except ValueError:
			print("Error: Please enter a valid date in the format YYYY-MM-DD.")
	while True:
		try:
			end_date = input("\nEnter the end date (YYYY-MM-DD): ").strip()
			if not end_date:
				print("Error: End date cannot be empty. Please enter a valid end date.")
			else:
				break
		except ValueError:
			print("Error: Please enter a valid date in the format YYYY-MM-DD.")

	return symbol, chart_type, time_series, start_date, end_date

